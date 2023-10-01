from django.shortcuts import render
from main.forms import StudentForm, UserForm

def index(request):
  if request.method == 'POST':
    form = UserForm(request.POST)
    if form.is_valid():
      name          = form.cleaned_data['name']
      email         = form.cleaned_data['email']
  else: 
    form = UserForm()
  context = {
    'form': form
  }
  template_name = 'main/index.html'
  return render(request, template_name, context)
