from django import forms
from django.contrib.auth.models import User
from .models import Task


class NewTaskForm(forms.ModelForm):
    due_date = forms.DateField(widget=forms.SelectDateWidget())
    performers = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.SelectMultiple,
    )

    class Meta:
        model = Task
        fields = [
            'category',
            'tag',
            'title',
            'description',
            'due_date',
            'performers',
        ]
