from django import forms
from .models import User
from django.core.exceptions import ValidationError

import re
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
name_regex = re.compile(r'^[a-zA-Z\s]+$')

class Userform (forms.ModelForm):
    class Meta:
        model = User
        fields = ("name", "email")
    
    def clean(self):
        data = super(Userform, self).clean()
        name = data.get("name")
        email = data.get("email")

        if (len(name) < 2):
            raise ValidationError(
                "Name must be at least two characters long"
            )
        elif not name_regex.match(name):
            raise ValidationError(
                "Name must contain only letters and spaces"
            )
        
        if not email_regex.match(email):
            raise ValidationError(
                "Not a valid email format"
            )