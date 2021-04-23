from django.contrib import admin

# Register your models here.
from .models import Question,student,Quiz

admin.site.register(Question),
admin.site.register(student),
admin.site.register(Quiz),