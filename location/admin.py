from django.contrib import admin

from location.models import Position



class positionAdmin(admin.ModelAdmin):

	list_display = ('id', 'latitude', 'longitude', 'phone', 'count')

	search_field = ['phone']



admin.site.register(Position, positionAdmin)
