from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . models import *
# Register your models here.


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at', 'subscribed')
    list_filter = ('subscribed', 'subscribed_at')
    search_fields = ('email',)
    list_per_page = 20

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('title', 'sent_at')
    search_fields = ('title',)
    list_per_page = 20