from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Reviewer Name'
            }),
            'review': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'review'
            }),
        }
