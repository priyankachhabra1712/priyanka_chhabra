from django import forms
from .models import Contacts


class formCon(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ["contact_name", "contact_email", "contact_notes"]

    def clean_email(self):
        email = self.cleaned_data.get('contact_email')

        # Validate email format
        if not email or '@' not in email:
            raise forms.ValidationError("Enter a valid email address.")

        return email


