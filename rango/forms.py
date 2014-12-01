from django import forms
from rango.models import Page, Category


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text='Please enter the category name.')
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = 'name',


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text='Please enter the title of the page.')
    url = forms.URLField(max_length=200, help_text='Please enter the URL of the page.')
    views = forms.IntegerField(widget=forms.HiddenInput, initial=0)

    class Meta:
        model = Page

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        # we can either exclude the category field
        exclude = ('category',)

    def clean(self):
        cleaned_data = super().clean()
        url = cleaned_data.get('url')
        # TODO: This part doesn't get called because of Javascript.
        #       Or maybe because of Chrome.  Hard to say hard to say.
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

        return cleaned_data
