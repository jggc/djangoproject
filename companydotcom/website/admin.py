from django.contrib import admin

# Register your models here.
from .models import Tag, NewsEntry, Publisher, Product, Job

admin.site.register(Tag)
admin.site.register(NewsEntry)
admin.site.register(Publisher)
admin.site.register(Product)
admin.site.register(Job)

