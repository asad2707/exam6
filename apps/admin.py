from django.contrib import admin

from apps.models import Book


# Register your models here.


@admin.register(Book)
class ModelNameAdmin(admin.ModelAdmin):
    pass
