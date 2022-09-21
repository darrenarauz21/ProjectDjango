from django import forms
from .models import Profile, BlogPost, ReviewPost

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio','instagram','image', )
     
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'slug', 'content', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Titulo del Blog'}),
            'slug': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Copie el título sin espacios y con un guión en el medio'}),
            'content': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Contenido del Blog'}),
        }
class ReviewPostForm(forms.ModelForm):
    class Meta:
        model = ReviewPost
        fields = ('title', 'slug', 'content', 'image')
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Titulo de la Review'}),
            'slug': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Copie el título sin espacios y con un guión en el medio'}),
            'contenido': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Contenido de la Review'}),
        }
	