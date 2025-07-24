# portfolios/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import PermissionDenied
from .models import Portfolio
from .forms import TimelineEventForm 
from collections import defaultdict
from .models import Portfolio, TimelineEvent



def landing_page(request):
    # This view handles both showing the form and processing its submission.
    
    if request.method == 'POST':
        # This block runs when the user submits the form.
        full_name = request.POST.get('full_name')
        title = request.POST.get('title')

        # Create a new Portfolio object in the database
        portfolio = Portfolio.objects.create(
            full_name=full_name,
            title=title,
        )
        # The .save() method in our model automatically creates the slug!

        # --- SESSION LOGIC ---
        # This is the key to our no-auth system. We store the slug of the
        # portfolio the user just created in their browser session.
        if 'editable_portfolios' not in request.session:
            request.session['editable_portfolios'] = []
        
        request.session['editable_portfolios'].append(portfolio.slug)
        request.session.modified = True # Important! Tell Django we changed the session.

        # Redirect the user to the dashboard page for their new portfolio.
        # We will create this 'dashboard' URL in the next step.
        return redirect('dashboard', slug=portfolio.slug)

    # This runs when the user first visits the page (a GET request).
    # We just show them the empty form.
    return render(request, 'portfolios/landing.html')


# portfolios/views.py

# ... (imports and other views are here) ...

# portfolios/views.py


# ... (other imports and views) ...

def dashboard(request, slug):
    portfolio = get_object_or_404(Portfolio, slug=slug)

    if slug not in request.session.get('editable_portfolios', []):
        raise PermissionDenied("You do not have permission to edit this portfolio.")

    # Fetch all events, making sure they are ordered correctly
    events_queryset = portfolio.events.all().order_by('-start_date')

    # --- NEW: Group events by year ---
    grouped_events = defaultdict(list)
    for event in events_queryset:
        grouped_events[event.start_date.year].append(event)
    
    # Convert defaultdict to a regular dict to be used in the template
    # and sort it by year in descending order.
    grouped_events_sorted = dict(sorted(grouped_events.items(), reverse=True))

    context = {
        'portfolio': portfolio,
        # Pass the new grouped and sorted dictionary to the template
        'grouped_events': grouped_events_sorted,
    }
    return render(request, 'portfolios/dashboard.html', context)


def add_timeline_event(request, slug):
    portfolio = get_object_or_404(Portfolio, slug=slug)

    # --- PERMISSION CHECK --- (Crucial for security)
    if slug not in request.session.get('editable_portfolios', []):
        raise PermissionDenied("You cannot add events to this portfolio.")

    if request.method == 'POST':
        form = TimelineEventForm(request.POST, request.FILES)
        if form.is_valid():
            # Create the event object but don't save to the database yet
            event = form.save(commit=False)
            # Associate it with the correct portfolio
            event.portfolio = portfolio
            # Now save it to the database
            event.save()
            # Redirect back to the dashboard
            return redirect('dashboard', slug=portfolio.slug)
    else:
        # If it's a GET request, just create an empty form
        form = TimelineEventForm()

    context = {
        'form': form,
        'portfolio': portfolio,
    }
    return render(request, 'portfolios/event_form.html', context)

# portfolios/views.py
from collections import defaultdict
from datetime import date # Make sure this is imported

# ... other imports ...

def public_portfolio_view(request, slug):
    portfolio = get_object_or_404(Portfolio, slug=slug)
    
    events_queryset = portfolio.events.all().order_by('-start_date')
    
    # --- NEW, IMPROVED GROUPING LOGIC ---
    grouped_events = defaultdict(list)
    
    # Find the min and max years from all events
    first_year = None
    last_year = date.today().year # Default to the current year

    if events_queryset.exists():
        for event in events_queryset:
            # Group by END year. If no end date, use today's year.
            year_to_group_by = event.end_date.year if event.end_date else date.today().year
            grouped_events[year_to_group_by].append(event)
            
            # Track the overall date range of the timeline
            if first_year is None or event.start_date.year < first_year:
                first_year = event.start_date.year
            if event.end_date and event.end_date.year > last_year:
                last_year = event.end_date.year
    
    # --- NEW: Create a complete list of all years to display ---
    all_years_to_display = []
    if first_year:
        # Generate a list of all years from last to first (e.g., [2024, 2023, 2022])
        all_years_to_display = list(range(last_year, first_year - 1, -1))

    # --- Pass both the events and the full year list to the template ---
    context = {
        'portfolio': portfolio,
        'grouped_events': grouped_events,
        'all_years': all_years_to_display,
    }
    return render(request, 'portfolios/public_portfolio.html', context)


# portfolios/views.py

# ... (other views) ...

def about_page(request):
    return render(request, 'portfolios/about.html')

def contact_page(request):
    return render(request, 'portfolios/contact.html')


# portfolios/views.py
# ... import PortfolioEditForm at the top ...
from .forms import TimelineEventForm, PortfolioEditForm

# ... add this new view function ...
def edit_portfolio(request, slug):
    portfolio = get_object_or_404(Portfolio, slug=slug)

    if slug not in request.session.get('editable_portfolios', []):
        raise PermissionDenied("You cannot edit this portfolio profile.")

    if request.method == 'POST':
        # IMPORTANT: Pass request.FILES to the form for file uploads
        form = PortfolioEditForm(request.POST, request.FILES, instance=portfolio)
        if form.is_valid():
            form.save()
            return redirect('dashboard', slug=portfolio.slug)
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

    # --- SECURITY CHECK ---
    # Ensure the user has permission and that the event belongs to this portfolio.
    if slug not in request.session.get('editable_portfolios', []) or event.portfolio != portfolio:
        raise PermissionDenied("You do not have permission to edit this event.")

    if request.method == 'POST':
        # The 'instance=event' is the key part that tells the form
        # to UPDATE the existing event, not create a new one.
        form = TimelineEventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('dashboard', slug=portfolio.slug)
    else:
        # Pre-populate the form with the event's current data.
        form = TimelineEventForm(instance=event)

    context = {
        'form': form,
        'portfolio': portfolio,
        'is_editing': True, # Pass a flag to the template
    }
    return render(request, 'portfolios/event_form.html', context)


def delete_timeline_event(request, slug, event_id):
    portfolio = get_object_or_404(Portfolio, slug=slug)
    event = get_object_or_404(TimelineEvent, id=event_id)

    # --- SECURITY CHECK ---
    if slug not in request.session.get('editable_portfolios', []) or event.portfolio != portfolio:
        raise PermissionDenied("You do not have permission to delete this event.")

    if request.method == 'POST':
        # If the form is submitted, delete the event and redirect.
        event.delete()
        return redirect('dashboard', slug=portfolio.slug)
    
    # If it's a GET request, show the confirmation page.
    context = {
        'event': event,
        'portfolio': portfolio,
    }
    return render(request, 'portfolios/event_confirm_delete.html', context)