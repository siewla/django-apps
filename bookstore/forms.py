from django import forms
from .models import *


class BookForm(forms.ModelForm):
    # cover = forms.FileField(widget=form)
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Book Title'
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Book Author'
            }),
            'price': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Book Price',
                'type': 'number'
            }),
            'published_year': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Book Year'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Book Description'
            }),
            'cover': forms.FileInput(attrs={
                'class': 'form-control',
            })
        }
