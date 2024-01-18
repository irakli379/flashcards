from django.contrib import admin
from .models import Flashcard
# from .models import WordClass, Language, Category


# @admin.register(models.Flashcard)
# class AuthorAdmin(admin.ModelAdmin)
# admin.site.register(WordClass),
# admin.site.register(Language),
# admin.site.register(Category),

admin.site.register(Flashcard)
