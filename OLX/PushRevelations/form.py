from django import forms
from PushRevelations.models import Revelation, Gallery
from Catalog.models import Category

def create_choise():
    choise = []
    categories = Category.objects.all()
    print(categories)
    for category in categories:
        choise.append((category.slug, category.name))
    return tuple(choise)

class PushForm(forms.ModelForm):
    class Meta:
        model = Revelation
        fields = ['category', 'name', 'description', 'price', 'image', 'image_2', 'image_3']

