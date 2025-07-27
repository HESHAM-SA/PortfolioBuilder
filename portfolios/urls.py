# portfolios/urls.py

from django.urls import path
from . import views

app_name = 'portfolios'

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('about/', views.about_page, name='about'),
    path('contact/', views.contact_page, name='contact'),
    path('portfolio/<slug:slug>/', views.public_portfolio_view, name='public_portfolio'),
    path('portfolio/<slug:slug>/edit/', views.dashboard, name='dashboard'),
    path('portfolio/<slug:slug>/events/add/', views.add_timeline_event, name='add_event'),
    path('portfolio/<slug:slug>/events/<int:event_id>/edit/', views.edit_timeline_event, name='edit_event'),
    path('portfolio/<slug:slug>/events/<int:event_id>/delete/', views.delete_timeline_event, name='delete_event'),
    path('portfolio/<slug:slug>/edit-profile/', views.edit_portfolio, name='edit_portfolio'),
]