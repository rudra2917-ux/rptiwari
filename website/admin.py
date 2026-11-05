from django.contrib import admin

from .models import ContactMessage

admin.site.site_header = 'R.P. Consultant & Engineers – Admin'
admin.site.site_title = 'RPCE Admin'
admin.site.index_title = 'Website management'


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'service', 'project_stage', 'capacity_tpd', 'location', 'created_at', 'is_read')
    list_filter = ('service', 'project_stage', 'machinery', 'is_read', 'created_at')
    search_fields = ('name', 'phone', 'email', 'company', 'message')
    list_editable = ('is_read',)
    readonly_fields = ('created_at',)
