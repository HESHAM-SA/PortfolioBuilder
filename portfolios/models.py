# portfolios/models.py

from django.db import models
from django.utils.text import slugify
import uuid

class Portfolio(models.Model):
    full_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    email = models.EmailField(blank=True)
    linkedin_url = models.URLField(blank=True)

    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.full_name) or "portfolio"
            unique_id = uuid.uuid4().hex[:6]
            self.slug = f"{base_slug}-{unique_id}"
        super().save(*args, **kwargs)

class TimelineEvent(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='events')
    
    EVENT_TYPE_CHOICES = [
        ('work', 'Work Experience'),
        ('education', 'Education'),
        ('project', 'Project'),
    ]
    event_type = models.CharField(max_length=20, choices=EVENT_TYPE_CHOICES, default='work')
    
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    event_image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True, help_text="Optional: A link to a YouTube or Vimeo video.")
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.title} at {self.company}"