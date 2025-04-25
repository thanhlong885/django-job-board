from django import forms
from .models import Application
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'email', 'message', 'resume']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.attrs = {'enctype': 'multipart/form-data'}
        self.helper.add_input(Submit('submit', 'Submit Application', css_class='bg-indigo-600 text-white px-4 py-2 rounded hover:bg-indigo-500'))
