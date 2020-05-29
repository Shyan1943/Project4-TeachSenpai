from django import forms
from pyuploadcare.dj.forms import ImageField
from .models import Profile


class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ('username', 'email',  'profiledesc', 'profileimg')