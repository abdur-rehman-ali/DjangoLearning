from django.shortcuts import render
from main.forms import StudentForm

def index(request):
  if request.method == 'POST':
    form = StudentForm(request.POST)
    if form.is_valid():
      first_name          = form.cleaned_data['first_name']
      last_name           = form.cleaned_data['last_name']
      hobby               = form.cleaned_data['hobby']
      year                = form.cleaned_data['year']
      is_cr               = form.cleaned_data['is_cr']
      registration_number = form.cleaned_data['registration_number']
  else: 
    form = StudentForm()
  context = {
    'form': form
  }
  template_name = 'main/index.html'
  return render(request, template_name, context)
