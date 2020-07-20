from django  import forms
from .models import Problem


class ProblemModelForm(forms.ModelForm):
	class Meta: 
		model = Problem 
		exclude = ['created_date', 'author']