from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import Property, Unit
from .models import CustomUser, Tenant, TenantAssignment ,Unit

admin.site.register(CustomUser)
admin.site.register(Property)
admin.site.register(Unit)
admin.site.register(Tenant)
admin.site.register(TenantAssignment)