from django import forms

from catalog.models import Product
forbidden_products = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

class StyleFormMixin:
    def __init__(self, **args):
        super().__init__(**args)
        for field_name, field in self.fields.items():
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
