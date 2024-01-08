from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('create/', views.create_property, name='create_property'),
    path('property/<int:property_id>/', views.property_detail, name='property_detail'),
    path('propertieslist/', views.property_list, name='property_list'),
    # path('tanent/create/', views.create_tenant, name='create_tenant'),
    # URL for creating a tenant
    path('tenant/create/', views.create_tenant, name='create_tenant'),

    # URL pattern to display tenant profile details by passing tenant_id as a parameter
    path('tenant/profile/<int:tenant_id>/', views.tenant_profile, name='tenant_profile'),
    path('tenants/', views.tenant_list, name='tenant_list'),
    path('assign_tenant/<int:tenant_id>/', views.assign_tenant, name='assign_tenant'),
	]