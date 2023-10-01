from django import forms
from django.core import validators

year_choices = (
  ('freshman', 'Freshman'),
  ('sophomore', 'Sophomore'),
  ('junior', 'Junior'),
  ('senior', 'Senior'),
)

class StudentForm(forms.Form):
  first_name = forms.CharField(
    max_length=30, 
    widget=forms.TextInput(attrs={'class': 'form-control'})
  )
  last_name = forms.CharField(
    max_length=30,
    required=False,
    widget=forms.TextInput(attrs={'class': 'form-control'})
  )
  hobby = forms.CharField(max_length=40, required=False)
  year = forms.ChoiceField(choices=year_choices, initial=year_choices[0][0])
  is_cr = forms.BooleanField(initial=False, required=False, label='class representative')
  registration_number = forms.IntegerField()


  # def clean_first_name(self):
  #   first_name = self.cleaned_data.get('first_name')
  #   if first_name and len(first_name) < 3:
  #     raise forms.ValidationError('Length must be greater than 3')
  #   return first_name

  # def clean_hobby(self):
  #   hobby = self.cleaned_data.get('hobby')
  #   if hobby:
  #     return hobby
  #   else:
  #     raise forms.ValidationError('ThiS Field is required')

  def clean(self):
    cleaned_data = super().clean()
    first_name = cleaned_data.get('first_name')
    hobby = cleaned_data.get('hobby')

    errors = {}
    if first_name and len(first_name) < 3:
      errors['first_name'] = 'Length must be greater than 3'

    if not hobby:
      errors['hobby'] = 'This field is required'

    if errors:
      raise forms.ValidationError(errors)

    return cleaned_data      


def name_should_start_with_a(name):
  if name[0] != 'a':
    raise forms.ValidationError('Name must start with a')

class UserForm(forms.Form):
  name = forms.CharField(
    error_messages={'required': 'Please enter your name'}
  )
  email = forms.EmailField(
    error_messages={'required': 'Please enter your email'},
    min_length=2,
    max_length=50
  )
  password = forms.CharField(widget=forms.PasswordInput())
  confirm_password = forms.CharField(widget=forms.PasswordInput())

  def clean(self):
    cleaned_data = super().clean()
    password = self.cleaned_data.get('password')
    confirm_password = self.cleaned_data.get('confirm_password')

    if password != confirm_password:
      raise forms.ValidationError("Both password didn't match")
