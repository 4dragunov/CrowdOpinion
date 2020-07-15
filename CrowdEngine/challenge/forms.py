from django import forms
from .models import Category, Challenge
from django.core.exceptions import ValidationError

class CategoryForm(forms.ModelForm):
    # title = forms.CharField(max_length=50)
    # slug = forms.CharField(max_length=50)
    #
    # title.widget.attrs.update({'class' : 'form-control'})
    # slug.widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = Category
        fields = ['title', 'slug']    #'__all__'

        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'slug' : forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Адрес не может быть "Create"')


        if Category.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Адрес уже существует. Он должен быть уникальным. У нас есть адрес "{}"'.format(new_slug))

        return new_slug


    # def save(self):
    #     new_category = Category.objects.create(title=self.cleaned_data['title'],
    #                                            slug = self.cleaned_data['slug']
    #                                            )
    #     return new_category

class ChallengeForm(forms.ModelForm):

    class Meta:
        model = Challenge
        fields = ['title', 'slug', 'body', 'categories' ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),
            'categories': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Адрес не может быть "Create"')

        return new_slug