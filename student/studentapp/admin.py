from django.contrib import admin
from .models import student,score
# Register your models here.

class studentAdmin(admin.ModelAdmin):
    list_display=('name','sex','birth','email','phone')
    list_filter=('name','sex')
    search_fields=('name',)


admin.site.register(student,studentAdmin)
admin.site.register(score)