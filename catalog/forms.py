from django import forms

from catalog.models import Product, Version

forbidden_products = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

class StyleFormMixin:
    def __init__(self, **args):
        super().__init__(**args)
        for field_name, field in self.fields.items():
            if field_name != 'activae_version':
                field.widget.attrs['class'] = 'form-control'

class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'price', 'creation_date')

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        for item in forbidden_products:
            if item in cleaned_data:
                raise forms.ValidationError(f'Имя продукта не должно содержать слово {item} ')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        for item in forbidden_products:
            if item in cleaned_data:
                raise forms.ValidationError(f'Описание продукта не должно содержать слово {item} ')

        return cleaned_data

class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

    def clean_is_active(self):
        cleaned_data = self.object.cleaned_data['active_version']
        if len(Version.objects.filter(active_version=True)) > 0 and cleaned_data is True:
            raise forms.ValidationError('Одна версия должна быть активной')
        return cleaned_data



