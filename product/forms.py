from django import forms
from product.models import Product

# class ProductForm(forms.Form):
#     name = forms.CharField()
#     price = forms.CharField()
#     fullname = forms.CharField()

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ("status", "remarks", "user", )
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for i in self.visible_fields():
    #         i.field.widget.attrs["class"] = "form-control"

# class ExampleForm(forms.Form):
#     # Your declared form fields here
#     ...

#     def __init__(self, *args, **kwargs):
#         super(ExampleForm, self).__init__(*args, **kwargs)
#         for visible in self.visible_fields():
#             visible.field.widget.attrs['class'] = 'form-control'
