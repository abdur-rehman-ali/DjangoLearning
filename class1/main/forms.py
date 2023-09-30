from django import forms

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

