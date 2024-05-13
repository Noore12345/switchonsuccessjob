from django import forms
from .models import Job,JobApplication

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'salary','experience','location','skills', 'requirements', 'responsibilities', 'qualifications', 'is_available']


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['name', 'email', 'phone', 'location']
        
