from django import forms
from django.contrib.auth.models import User
from .models import Todo
from django.core.exceptions import ValidationError


class TodoForm(forms.ModelForm):
    # Override due_date to use an HTML5 datetime-local input
    due_date = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={
            "type": "datetime-local",
            "placeholder": "Select due date and time",
        }, format="%Y-%m-%dT%H:%M"),
        input_formats=["%Y-%m-%dT%H:%M"],
    )

    class Meta:
        model = Todo
        fields = ["title", "task_image", "due_date"]
        widgets = {
            "title": forms.TextInput(attrs={
                "placeholder": "Enter task title"
            }),
            "task_image": forms.ClearableFileInput(attrs={
                "accept": "image/*"
            }),
        }


class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(
        required=True,
        help_text="Enter your email address"
    )
    
    class Meta:
        model = User
        fields = ["username", "email"]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Enter your username'
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Enter your email address'
        })
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            raise ValidationError("This email address is already in use. Please use a different one.")
            
        return email


class UpdateTaskForm(forms.ModelForm):
    due_date = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={
            "type": "datetime-local",
            "placeholder": "Select due date and time",
        }, format="%Y-%m-%dT%H:%M"),
        input_formats=["%Y-%m-%dT%H:%M"],
    )

    class Meta:
        model = Todo
        fields = ["title", "task_image", "due_date"]
        widgets = {
            "title": forms.TextInput(attrs={
                "placeholder": "Enter task title"
            }),
            "task_image": forms.ClearableFileInput(attrs={
                "accept": "image/*",
                "class": "file-input"
            }),
        }
    
    # This save method will now correctly handle the old image file
    def save(self, commit=True):
        # Get the existing task object from the database
        task = super().save(commit=False)
        
        try:
            # Check if a new image was uploaded and it's different from the old one
            old_task = Todo.objects.get(pk=task.pk)
            if old_task.task_image and old_task.task_image != task.task_image:
                # Delete the old image file
                old_task.task_image.delete(save=False)
        except Todo.DoesNotExist:
            # This happens if it's a new task, which isn't the case for an update form
            pass

        if commit:
            task.save()
        return task

