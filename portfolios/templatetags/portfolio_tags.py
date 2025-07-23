# portfolios/templatetags/portfolio_tags.py
from django import template

register = template.Library()

@register.filter
def embed_youtube_url(value):
    """Converts a regular YouTube URL to an embeddable URL."""
    if "youtube.com/watch?v=" in value:
        video_id = value.split('v=')[1].split('&')[0]
        return f"https://www.youtube.com/embed/{video_id}"
    # Return the original URL if it's not a standard YouTube link
    return value