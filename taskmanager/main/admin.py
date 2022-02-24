from django.contrib import admin
from .models import News
from .models import Todo


admin.site.register(News)
admin.site.register(Todo)