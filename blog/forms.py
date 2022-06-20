from django import forms
from .models import Post, Category

#choices = [('Cats', 'Cats'), ('Dogs', 'Dogs')]
choices = Category.objects.all().values_list('name', 'name')

choice_list =[]

for item in choices:
    choice_list.append(item)

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Post
        fields = ('title', 'category', 'author', 'body', 'image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            #'image': forms.Select(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'image', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            #'category': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            #'image': forms.Select(attrs={'class': 'form-control'}),
        }
