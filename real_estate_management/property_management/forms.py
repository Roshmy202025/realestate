from django import forms
from .models import Property, Unit, Tenant, TenantAssignment

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = '__all__'

class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = '__all__'
        exclude = ['property']


class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ['name', 'address', 'document_proofs']  

# class TenantForm(forms.ModelForm):
#     class Meta:
#         model = Tenant
#         fields = '__all__'

# class AgreementForm(forms.ModelForm):
#     class Meta:
#         model = Agreement
#         fields = '__all__'


class TenantAssignmentForm(forms.ModelForm):
    class Meta:
        model = TenantAssignment
        fields = ['tenant', 'unit', 'agreement_end_date', 'monthly_rent_date']
        exclude = ['tenant']
        # fields = '__all__'