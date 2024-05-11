from django.contrib import admin
from .models import Books , Review, Author, BookAuthor, CategoryBooks, Language
# Register your models here.

admin.site.register(CategoryBooks)
admin.site.register(Books)
admin.site.register(Author)
admin.site.register(BookAuthor)
admin.site.register(Review)
admin.site.register(Language)