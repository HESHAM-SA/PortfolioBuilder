# portfolios/templatetags/portfolio_tags.py

from django import template
import re

register = template.Library()

@register.filter(name='embed_youtube_url')
def embed_youtube_url(value):
    """
    Converts a standard YouTube watch URL to an embeddable URL.
    Handles various YouTube URL formats (e.g., youtu.be, /watch?v=, /embed/).
    
    Args:
        value (str): The original YouTube URL.
        
    Returns:
        str: The embeddable YouTube URL or the original value if no match is found.
    """
    if not isinstance(value, str):
        return value

    # Regex to extract the video ID from various YouTube URL formats
    youtube_regex = (
        r'(https?://)?(www\.)?'
        '(youtube|youtu|youtube-nocookie)\.(com|be)/'
        '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')

    match = re.search(youtube_regex, value)

    if match:
        video_id = match.group(6)
        return f"https://www.youtube.com/embed/{video_id}"
    
    return value


@register.filter(name='get_item')
def get_item(dictionary, key):
    """
    Allows dictionary key lookup using a variable in a Django template.
    
    Usage: {{ my_dictionary|get_item:my_variable_key }}
    
    Args:
        dictionary (dict): The dictionary to look up.
        key: The key to retrieve the value for.
        
    Returns:
        The value associated with the key, or None if the key doesn't exist.
    """
    return dictionary.get(key)