from rest_framework import filters, generics, permissions
from flashcards.models import Flashcard
from .serializers import FlashcardSerializer
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAdminUser, DjangoModelPermissionsOrAnonReadOnly


class FlashcardsUserWritePermission(BasePermission):
    # maybe other users should 'import the card and change its 'completed' field
    message = 'Only the author can edit the flashcard.'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user


class FlashcardsList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Flashcard.objects.all()
    serializer_class = FlashcardSerializer


class FlashcardsDetail(generics.RetrieveUpdateDestroyAPIView, FlashcardsUserWritePermission):
    permission_classes = [FlashcardsUserWritePermission]
    queryset = Flashcard.objects.all()
    serializer_class = FlashcardSerializer


class FlashcardsListDetailFilter(generics.ListAPIView):
    queryset = Flashcard.objects.all()
    serializer_class = FlashcardSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^word', '^translation']
    # '^language__name', '^author__user_name', '^word_class__name', '^category__name', '^translation_language'


# CRUD operations for user
class CreateFlashcard(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Flashcard.objects.all()
    serializer_class = FlashcardSerializer


class AdminFlashcardDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Flashcard.objects.all()
    serializer_class = FlashcardSerializer


class EditFlashcard(generics.RetrieveUpdateAPIView, FlashcardsUserWritePermission):
    permission_classes = [permissions.IsAuthenticated, FlashcardsUserWritePermission]
    serializer_class = FlashcardSerializer
    queryset = Flashcard.objects.all()


class DeleteFlashcard(generics.RetrieveDestroyAPIView, FlashcardsUserWritePermission):
    permission_classes = [permissions.IsAuthenticated, FlashcardsUserWritePermission]
    serializer_class = FlashcardSerializer
    queryset = Flashcard.objects.all()
