from django.contrib import admin
from account.models import Account, VendorAccount, BloggerAccount
# from django.contrib.auth.admin import UserAdmin


# Register your models here.


class AccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'contact_number', 'last_login')
    search_fields = ('email', 'contact_number', 'name', 'id')
    readonly_fields = ()
    ordering = ('email',)
    filter_horizontal = ()
    list_filter = ()


class VendorAdmin(admin.ModelAdmin):
    list_display = ('vendor', 'plan', 'gst',)
    search_fields = ('plan', 'gst', 'shop_name')
    readonly_fields = ()
    ordering = ('plan',)
    filter_horizontal = ()
    list_filter = ()


admin.site.register(Account, AccountAdmin)
admin.site.register(VendorAccount, VendorAdmin)
admin.site.register(BloggerAccount)

# admin.site.register(Account)
# admin.site.register(VendorAccount)
