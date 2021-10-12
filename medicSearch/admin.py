from django.contrib import admin
from .models import *
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('user','role', 'specialtiesList','addressesList',)

    def specialtiesList(self, obj):
        return [i.name for i in obj.specialties.all()]
    def addressesList(self,obj):
        return [i.name for i in obj.addresses.all()]

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Address)
admin.site.register(DayWeek)
admin.site.register(Rating)
admin.site.register(Speciality)
