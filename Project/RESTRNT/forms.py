from django.forms import ModelForm
from .models import *
from .views import*

class CategoryForm(ModelForm):
    class Meta:
        model=Category
        fields='__all__'
        
class PostForm(ModelForm):
    
    class Meta:
        model = Post
        fields = ('title','sub_title','description','category','img')

class ProductCategoryForm(ModelForm):
    
    class Meta:
        model = ProductCategory
        fields = '__all__'

class ProductForm(ModelForm):
    
    class Meta:
        model = Product
        fields = '__all__'

