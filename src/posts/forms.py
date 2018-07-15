from django import forms
from .models import Post

class PostCreateForm(forms.ModelForm):
	name = forms.CharField()		
	content = forms.CharField(widget=forms.Textarea)	
	
	class Meta:
		model = Post
		fields = {
			'name',
			'category',
			'content',
			'logo',
			'image',
			'ticker',
		}