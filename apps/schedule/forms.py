from django import forms
from .models import SchedulePost, Platform


class SchedulePostCreateForm(forms.ModelForm):
    post_title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Title",
                "class": "form-control",
            }
        )
    )

    post_content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Content",
                "class": "form-control",
                "rows": 3,
            }
        )
    )

    platform = forms.ChoiceField(
        choices=Platform.choices,
        widget=forms.Select(
            attrs={
                "class": "form-control",
            }
        )
    )

    schedule_time = forms.DateTimeField(
        input_formats=['%Y-%m-%d %H:%M'],
        widget=forms.DateTimeInput(
            attrs={
                "class": "form-control",
                "type": "datetime-local",
            }
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
    
    def save(self, user, commit=True):
        instance = super(SchedulePostCreateForm, self).save(commit=False)
        instance.username = user
        if commit:
            instance.save()
        return instance
    
    class Meta:
        model = SchedulePost
        fields = ["post_title", "platform", "post_content", "schedule_time"]
