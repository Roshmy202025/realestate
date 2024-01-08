from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import LoginForm, PropertyForm, UnitForm,TenantForm, TenantAssignmentForm
from .models import Property, Tenant, TenantAssignment ,Unit



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None and user.is_staff:
                login(request, user)
               	properties = Property.objects.all()
               	tenants = Tenant.objects.all()
               	return render(request, 'property_list.html', {'properties': properties, 'tenants': tenants})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def create_property(request):
    if request.method == 'POST':
        property_form = PropertyForm(request.POST)
        unit_form = UnitForm(request.POST)

        if property_form.is_valid() and unit_form.is_valid():
            property_instance = property_form.save()
            unit_instance = unit_form.save(commit=False)
            unit_instance.property = property_instance
            unit_instance.save()
            property_instance = property_form.save()
            return redirect('property_detail', property_id=property_instance.id)

    else:
        property_form = PropertyForm()
        unit_form = UnitForm()

    return render(request, 'create_property.html', {'property_form': property_form, 'unit_form': unit_form})





def property_detail(request, property_id):
    property_obj = Property.objects.get(pk=property_id)
    units = property_obj.units.all()
    context = {
        'property_obj': property_obj,
        'units': units
    }
    return render(request, 'property_detail.html', context)

def property_list(request):
    properties = Property.objects.all()  # Retrieve all properties from the database
    tenants = Tenant.objects.all()
    return render(request, 'property_list.html', {'properties': properties, 'tenants': tenants})


def create_tenant(request):
    if request.method == 'POST':
        tenant_form = TenantForm(request.POST, request.FILES)
        if tenant_form.is_valid():
            tenant_instance = tenant_form.save()  # Save the tenant instance to the database
            return redirect('tenant_profile', tenant_id=tenant_instance.id)  # Redirect to the tenant profile

    else:
        tenant_form = TenantForm()

    return render(request, 'tenant_create.html', {'tenant_form': tenant_form})



def tenant_profile(request, tenant_id):
    tenant = Tenant.objects.get(id=tenant_id)
    tenant_assignments = TenantAssignment.objects.filter(tenant=tenant)
    return render(request, 'tenant_profile.html', {'tenant': tenant, 'tenant_assignments': tenant_assignments})


def tenant_list(request):
    tenants = Tenant.objects.all()
    return render(request, 'tenant_list.html', {'tenants': tenants})




def assign_tenant(request, tenant_id):
    properties = Property.objects.all()  # Fetch all properties
    units = Unit.objects.all()  # Fetch all units
    tenant_obj = get_object_or_404(Tenant, id=tenant_id)
    if request.method == 'POST':
        form = TenantAssignmentForm(request.POST)
   
        if form.is_valid():
        
            unit_id = request.POST.get('unit')
            agreement_end_date = form.cleaned_data['agreement_end_date']
            monthly_rent_date = form.cleaned_data['monthly_rent_date']
            
            unit_obj = get_object_or_404(Unit, id=unit_id)
            tenant_obj = get_object_or_404(Tenant, id=tenant_id)

            tenant_assignment = TenantAssignment.objects.create(
                tenant=tenant_obj,
                unit=unit_obj,
                agreement_end_date=agreement_end_date,
                monthly_rent_date=monthly_rent_date
            )

            tenant_assignments = TenantAssignment.objects.filter(tenant=tenant_obj)
            return render(request, 'tenant_profile.html', {'tenant': tenant_obj, 'tenant_assignments': tenant_assignments})

        else:
        	print (form.errors)
    else:
        tenant_obj = Tenant.objects.get(id=tenant_id)
        form = TenantAssignmentForm(initial={'tenant': tenant_obj.id})
        print ("Not inside")
        print (tenant_obj.name)

    return render(request, 'assign_tenant.html', {'form': form, 'properties': properties, 'units': units, 'tenant_obj': tenant_obj})