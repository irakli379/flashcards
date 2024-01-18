from django.db import models
# from django.contrib.auth.models import User
from django.utils import timezone
from languageflashcards import settings
from django.utils.translation import gettext_lazy as _


# def upload_to(instance, filename):
#     return f"flashcards/{filename}"
#
#
# class Category(models.Model):
#     name = models.CharField(max_length=99, unique=True)
#
#     def __str__(self):
#         return self.name
#
#
# class WordClass(models.Model):
#     options = (
#         ('noun', 'Noun'),
#         ('verb', 'Verb'),
#         ('adjective', 'Adjective'),
#         ('adverb', 'Adverb'),
#     )
#
#     name = models.CharField(max_length=99, choices=options, null=False)
#
#     def __str__(self):
#         return self.name
#
#
# class Language(models.Model):
#     """Model representing a Language (e.g. English, French, Japanese, etc.)"""
#     name = models.CharField(max_length=99,
#                             unique=True,
#                             help_text="Enter the language (e.g. English, French, Japanese etc.)")
#
#     def __str__(self):
#         return self.name


class Flashcard(models.Model):

    # word_class = models.ForeignKey(WordClass, on_delete=models.PROTECT)
    # language = models.ForeignKey(Language, on_delete=models.PROTECT)
    # translation_language = models.CharField(max_length=99)
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True, null=True)
    #
    # published = models.DateTimeField(default=timezone.now)
    #
    # options = (
    #     ('private', 'Private'),
    #     ('public', 'Public'),
    # )
    #
    # status = models.CharField(max_length=15, choices=options, default='private')
    # completed = models.BooleanField(default=False)

    word = models.CharField(max_length=99, unique=True)
    definition = models.TextField(max_length=333, unique=True, blank=True, null=True)

    translation = models.CharField(max_length=99, unique=True)
    translated_definition = models.TextField(max_length=333, unique=True, blank=True, null=True)

    class Meta:
        ordering = ('-word',)

    def __str__(self):
        return self.word
