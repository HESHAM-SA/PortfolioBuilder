from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import PermissionDenied
from .models import Portfolio, TimelineEvent
from .forms import TimelineEventForm, PortfolioEditForm
from collections import defaultdict
from datetime import date

def landing_page(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        title = request.POST.get('title')

        portfolio = Portfolio.objects.create(
            full_name=full_name,
            title=title,
        )

        if 'editable_portfolios' not in request.session:
            request.session['editable_portfolios'] = []
        
        request.session['editable_portfolios'].append(portfolio.slug)
        request.session.modified = True

        return redirect('portfolios:dashboard', slug=portfolio.slug)

    return render(request, 'portfolios/landing.html')

def dashboard(request, slug):
    portfolio = get_object_or_404(Portfolio, slug=slug)

    if slug not in request.session.get('editable_portfolios', []):
        raise PermissionDenied("You do not have permission to edit this portfolio.")

    events_queryset = portfolio.events.all().order_by('-start_date')
    grouped_events = defaultdict(list)
    for event in events_queryset:
        grouped_events[event.start_date.year].append(event)
    
    grouped_events_sorted = dict(sorted(grouped_events.items(), reverse=True))

    context = {
        'portfolio': portfolio,
        'grouped_events': grouped_events_sorted,
    }
    return render(request, 'portfolios/dashboard.html', context)

def add_timeline_event(request, slug):
    portfolio = get_object_or_404(Portfolio, slug=slug)

    if slug not in request.session.get('editable_portfolios', []):
        raise PermissionDenied("You cannot add events to this portfolio.")

    if request.method == 'POST':
        form = TimelineEventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.portfolio = portfolio
            event.save()
            return redirect('portfolios:dashboard', slug=portfolio.slug)
    else:
        form = TimelineEventForm()

    context = {
        'form': form,
        'portfolio': portfolio,
    }
    return render(request, 'portfolios/event_form.html', context)

def public_portfolio_view(request, slug):
    portfolio = get_object_or_404(Portfolio, slug=slug)
    events_queryset = portfolio.events.all().order_by('-start_date')
    
    grouped_events = defaultdict(list)
    first_year = None
    last_year = date.today().year

    if events_queryset.exists():
        for event in events_queryset:
            year_to_group_by = event.end_date.year if event.end_date else date.today().year
            grouped_events[year_to_group_by].append(event)
            
            if first_year is None or event.start_date.year < first_year:
                first_year = event.start_date.year
            if event.end_date and event.end_date.year > last_year:
                last_year = event.end_date.year
    
    all_years_to_display = []
    if first_year:
        all_years_to_display = list(range(last_year, first_year - 1, -1))

    context = {
        'portfolio': portfolio,
        'grouped_events': grouped_events,
        'all_years': all_years_to_display,
    }
    return render(request, 'portfolios/public_portfolio.html', context)

def about_page(request):
    return render(request, 'portfolios/about.html')

def contact_page(request):
    return render(request, 'portfolios/contact.html')

def edit_portfolio(request, slug):
    portfolio = get_object_or_404(Portfolio, slug=slug)

    if slug not in request.session.get('editable_portfolios', []):
        raise PermissionDenied("You cannot edit this portfolio profile.")

    if request.method == 'POST':
        form = PortfolioEditForm(request.POST, request.FILES, instance=portfolio)
        if form.is_valid():
            form.save()
            return redirect('portfolios:dashboard', slug=portfolio.slug)
    else:
        form = PortfolioEditForm(instance=portfolio)

    context = {
        'form': form,
        'portfolio': portfolio
    }
    return render(request, 'portfolios/portfolio_form.html', context)

def edit_timeline_event(request, slug, event_id):
    portfolio = get_object_or_404(Portfolio, slug=slug)
    event = get_object_or_404(TimelineEvent, id=event_id)

    if slug not in request.session.get('editable_portfolios', []) or event.portfolio != portfolio:
        raise PermissionDenied("You do not have permission to edit this event.")

    if request.method == 'POST':
        form = TimelineEventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('portfolios:dashboard', slug=portfolio.slug)
    else:
        form = TimelineEventForm(instance=event)

    context = {
        'form': form,
        'portfolio': portfolio,
        'is_editing': True,
    }
    return render(request, 'portfolios/event_form.html', context)

def delete_timeline_event(request, slug, event_id):
    portfolio = get_object_or_404(Portfolio, slug=slug)
    event = get_object_or_404(TimelineEvent, id=event_id)

    if slug not in request.session.get('editable_portfolios', []) or event.portfolio != portfolio:
        raise PermissionDenied("You do not have permission to delete this event.")

    if request.method == 'POST':
        event.delete()
        return redirect('portfolios:dashboard', slug=portfolio.slug)
    
    context = {
        'event': event,
        'portfolio': portfolio,
    }
    return render(request, 'portfolios/event_confirm_delete.html', context)