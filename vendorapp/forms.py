from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib import auth

from vendorapp.models import *
from ckeditor.widgets import CKEditorWidget


    

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product

        fields = [
            'title',
            'product_description',
            'tags',
            'sales_location',
            'category',
            'seller_name',
            'image',
            'price',
            'available',
            'updated',
            'is_published',
            ]


    def clean_category(self):
        category = self.cleaned_data.get('category')

        if not category:
            raise forms.ValidationError("category is required")
        return category


    def save(self, commit=True):
        product = super(ProductForm, self).save(commit=False)
        if commit:
            
            product.save()
        return product




class ProductSalesForm(forms.ModelForm):#was JobApplyForm
    class Meta:
        model = Shopper
        fields = ['product']

class ProductWishlistForm(forms.ModelForm):
    class Meta:
        model = Product_Wishlist
        fields = ['product']




class ProductEditForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = [
            'title',
            'product_description',
            'tags',
            'sales_location',
            'category',
            'seller_name',
            'image',
            'price',
            'available',
            'updated'
            ]

    def clean_category(self):
        category = self.cleaned_data.get('category')

        if not category:
            raise forms.ValidationError("Category is required")
        return category


    def save(self, commit=True):
        product = super(ProductEditForm, self).save(commit=False)
      
        if commit:
            product.save()
        return product

