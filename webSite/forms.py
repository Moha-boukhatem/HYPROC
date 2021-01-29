from django.forms import ModelForm
from .models import *

class userform(ModelForm):
    class Meta :
        model = utilisateur
        fields= '__all__'
