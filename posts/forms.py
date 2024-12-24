# from django import forms
# from django.template.defaultfilters import title
#
#
# class PostForm(forms.Form):
#     image = forms.ImageField()
#     title = forms.CharField()
#     description = forms.CharField()
#
#   def clean(self):
#         data = self.cleaned_data
#         if data.get("title") == data.get("description"):
#          raise forms.ValidationError("title and description must be different")
#         return data
#
