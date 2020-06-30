from django import forms
from project1app.models import Client,Owner,Restaurant,Review,Reservation

class NewUserForm(forms.ModelForm):
    class Meta:
        model=Client
        fields='__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields='__all__'

class ReserveForm(forms.ModelForm):
    class Meta:
        model=Reservation
        fields='__all__'
