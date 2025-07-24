# portfolios/templatetags/portfolio_tags.py

from django import template
import re  # Import the regular expressions module

register = template.Library()

@register.filter
def embed_youtube_url(value):
    """
    Converts a regular YouTube URL (including shorts, etc.) to an embeddable URL.
    Returns the original value if it's not a recognizable YouTube link.
    """
    if not isinstance(value, str):
        return value

    # Regex to find the video ID from various YouTube URL formats
    youtube_regex = (
        r'(https?://)?(www\.)?'
        '(youtube|youtu|youtube-nocookie)\.(com|be)/'
        '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')

    match = re.search(youtube_regex, value)

    if match:
        video_id = match.group(6)
        return f"https://www.youtube.com/embed/{video_id}"
    
    # If no match is found, return the original URL
    return value


@register.filter
def get_item(dictionary, key):
    """Allows dictionary lookup using a variable in a template."""
    return dictionary.get(key)