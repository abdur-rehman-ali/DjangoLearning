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


  def clean_first_name(self):
    first_name = self.cleaned_data.get('first_name')
    if first_name and len(first_name) < 3:
      raise forms.ValidationError('Length must be greater than 3')
    return first_name

  def clean_hobby(self):
    hobby = self.cleaned_data.get('hobby')
    if hobby:
      return hobby
    else:
      raise forms.ValidationError('ThiS Field is required')

