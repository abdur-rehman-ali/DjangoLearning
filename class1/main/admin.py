from django.contrib import admin
from main.models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
  list_display = ['id', 'first_name', 'last_name', 'hobby', 'year', 'is_cr', 'registration_number']
  search_fields = ('first_name', 'hobby')
  list_filter = ('last_name', 'year')
  ordering = ('-created_at',)
