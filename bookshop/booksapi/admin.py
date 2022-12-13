from django.contrib import admin
from .models import Book, Language, Genre, PublishingHouse, Author

# Register your models here.
admin.site.register(Book)
admin.site.register(Language)
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(PublishingHouse)



