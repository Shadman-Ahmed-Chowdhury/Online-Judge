from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.core.validators import RegexValidator

# Create your models here.

class Problem(models.Model): 

	OPTIONS = (
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    )
	title = models.CharField(max_length=150)
	code = models.CharField(max_length=20, 
		unique=True, 

		validators=[RegexValidator('^[\w-]+$', ('Problem code cannot have white space and can have only hyphens between letters and numbers'))])
	description = RichTextField(blank=False)
	input_format = RichTextField(blank=False)
	constraints = RichTextField(blank=False)
	output_format = RichTextField(blank=False)
	types = models.CharField(max_length=50)
	difficulty = models.CharField(max_length=10, choices=OPTIONS, default='Easy')
	sample_input1 = RichTextField(blank=False, default='Empty')
	sample_input2 = RichTextField(blank=False, default='Empty')
	sample_output1 = RichTextField(blank=False, default='Empty')
	sample_output2 = RichTextField(blank=False, default='Empty')
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	created_date = models.DateTimeField(default=timezone.now)

	def __str__(self): 
		return self.title

	def get_absolute_url(self):
		return reverse('judge:problem-detail', kwargs={"pk": self.pk, "code": self.code}) 

	

