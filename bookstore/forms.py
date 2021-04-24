from django import forms
from .models import *


class BookForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple())

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
            }),
            # 'categories': forms.CheckboxSelectMultiple(attrs={
            #     'class': 'form-control',
            # })
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
