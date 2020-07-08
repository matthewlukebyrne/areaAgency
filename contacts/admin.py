from django.contrib import admin

# Register your contact models here.
# Contacts that will be enquired will be listed here on the admin area
# Contacts Admin Customization
# Enquiry Data


from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title', 'email', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'title')
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)
