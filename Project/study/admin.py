from django.contrib import admin
from .models import Subject, Questions , Test, Result

# Register your models here.
admin.site.register(Subject)
admin.site.register(Questions)
admin.site.register(Test)
admin.site.register(Result)