from django.contrib import admin
from my_app.models import AwsBucketModel
# Register your models here.
class BucketAdmin(admin.ModelAdmin):
    list_display = ['name', 'link', 'file']

admin.site.register(AwsBucketModel, BucketAdmin)
