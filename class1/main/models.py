from django.db import models

# Create your models here.
YEAR_IN_SCHOOL_CHOICES = [
  ('1st', 'First'),
  ('2nd', 'Second'),
  ('3rd', 'Third'),
  ('4th', 'Fourth')
]

class Student(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30, blank=True)
  hobby = models.CharField(max_length=40, null=True)
  year = models.CharField(max_length=4, choices=YEAR_IN_SCHOOL_CHOICES, default=YEAR_IN_SCHOOL_CHOICES[0][0])
  is_cr = models.BooleanField(default= False, verbose_name='class representative')
  registration_number = models.IntegerField(unique=True)
  created_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f'{self.id}'
