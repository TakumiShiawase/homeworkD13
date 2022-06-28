from django.contrib import admin
from .models import Author, Category, News, Answer
 
 
admin.site.register(Category)
admin.site.register(News)
admin.site.register(Author)
admin.site.register(Answer)