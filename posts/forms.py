from django import forms
from django.template.defaultfilters import title


class PostForm(forms.Form):
    image = forms.ImageField()
    title = forms.CharField()
    description = forms.CharField()


    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        description = cleaned_data.get("description")

        if title and description and title.lower() == description.lower():
            # data = self.cleaned_data
            # title = self.cleaned_data.get('title')
            # description = self.cleaned_data.get('description')
            # if data.get("title") == data.get("description"):
            raise forms.ValidationError("title and description must be different")
        return cleaned_data


    def clean_title(self):
        title = self.cleaned_data['title']
        if "python" in title.lower():
            raise forms.ValidationError("Title must not contain python")
        return title



    def clean_description(self):
        description = self.cleaned_data['description']
        if len(description) < 3:
            raise forms.ValidationError("Description must be at least 3 characters")
        return description
