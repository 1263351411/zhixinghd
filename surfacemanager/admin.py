from django.contrib import admin
from .models import Publication

# Register your models here.

class PublicationAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs

    list_display = ('id', 'author', 'paper_title', 'conference')
    list_filter = ('id','author','paper_title')
    fk_fields = ('id','author','paper_title')

admin.site.register(Publication,PublicationAdmin)
