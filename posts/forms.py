from django import forms

from posts.models import Category


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

class SearchForm(forms.Form):
     search = forms.CharField(
           required=False,
         max_length=100,
         widget=forms.TextInput(attrs={"placeholder": "Поиск",'class': 'form-control'}),
)

Category = forms.ModelChoiceField(
    queryset=Category.objects.all(),
    required=False,
    widget=forms.Select(attrs={"class": "form-control"}),
)
orderings = (
        ("created_at", "По дате создания"),
        ("updated_at", "По дате изменения"),
        ("rate", "По оценке"),
        ("-created_at", "По дате создания по убыванию"),
        ("-updated_at", "По дате изменения по убыванию"),
        ("-rate", "По оценке по убыванию"),

)
orderings = forms.ChoiceField(
    choices=orderings, required=False, widget=forms.Select(attrs={"class": "form-control"}),
)