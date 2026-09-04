from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(About)
admin.site.register(Skills)
admin.site.register(Education)
admin.site.register(Experience)
@admin.register(portfolio)
class PortfolioAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'is_published', 'sort_order')
	list_filter = ('category', 'is_published')
	search_fields = ('title', 'desc')
	list_editable = ('is_published', 'sort_order')
	ordering = ('sort_order', 'title')
admin.site.register(Service)