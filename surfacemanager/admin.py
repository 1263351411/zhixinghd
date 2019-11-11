from django.contrib import admin
from .models import Publication,Democard

# Register your models here.

class PublicationAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs

    list_display = ('id', 'author', 'paper_title', 'conference')
    list_filter = ('id','author','paper_title')
    fk_fields = ('id','author','paper_title')

class DemocardAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs

    list_display = ('id', 'project_name', 'project_ico', 'project_description','url_outer','url_intranet')
    list_filter = ('id', 'project_name', 'project_ico','url_outer','url_intranet')
    fk_fields = ('id', 'project_name', 'project_ico','url_outer','url_intranet')

admin.site.register(Publication,PublicationAdmin)
admin.site.register(Democard,DemocardAdmin)
