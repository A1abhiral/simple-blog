from django import forms
from theblog.models import Post,Category

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for i in choices:
    choice_list.append(i)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','author','category','body')

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control',}),
            'author' : forms.TextInput(attrs={'class':'form-control','value':'','id':'elder','type':'hidden'}),
            #'author' : forms.Select(attrs={'class':'form-control',}),
            'category' : forms.Select(choices=choice_list,attrs={'class':'form-control',}),
            'body' : forms.Textarea(attrs={'class':'form-control',}),


        } 

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','body')

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control',}),
            'body' : forms.Textarea(attrs={'class':'form-control',}),


        }                 