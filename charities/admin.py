from django.contrib import admin
from .models import Charity


# Register your models here.
class CharityAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'url',
        'image'
    )

    ordering = ('name',)



admin.site.register(Charity, CharityAdmin)
