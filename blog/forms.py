from django import forms

from blog.models import Article

class ArticleForms(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'

    def clean_title(self):
        arr_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        # cleaned_data = self.cleaned_data[fields]
        for item in arr_words:
            cleaned_data = self.cleaned_data['title']
            if item in cleaned_data:
                raise forms.ValidationError('Ошибка загрузки запрещенных продуктов!')
        return cleaned_data

    def clean_content(self):

        arr_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        # cleaned_data = self.cleaned_data[fields]
        for item in arr_words:
            cleaned_data = self.cleaned_data['content']
            if item in cleaned_data:
                raise forms.ValidationError('Ошибка загрузки запрещенных продуктов!')
        return cleaned_data