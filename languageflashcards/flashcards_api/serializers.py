from rest_framework import serializers
from flashcards.models import Flashcard


class FlashcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields = ('id', 'word', 'translation') # 'word_class',  'definition',  'translated_definition',
                # 'language', 'translation_language', 'category', 'author', 'status', 'completed', 'image'
