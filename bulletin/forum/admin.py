from django.contrib import admin

# Register your models here.
from .models import Thread, Choice, Post

admin.site.register(Thread)
admin.site.register(Choice)
admin.site.register(Post)
