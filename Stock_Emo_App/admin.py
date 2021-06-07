from django.contrib import admin
from .models import *

# admin 추가
admin.site.register(Stock)
admin.site.register(Member)