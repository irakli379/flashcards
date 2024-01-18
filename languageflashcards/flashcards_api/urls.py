from django.urls import path
from .views import (FlashcardsList, FlashcardsDetail, FlashcardsListDetailFilter,
                    CreateFlashcard, AdminFlashcardDetail, EditFlashcard, DeleteFlashcard)

app_name = 'flashcards_api'

urlpatterns = [
    path('<int:pk>', FlashcardsDetail.as_view(), name='detailcreate'),
    path('', FlashcardsList.as_view(), name='listcreate'),
    path('search/custom/', FlashcardsListDetailFilter.as_view(), name='flashcards_search'),
    # Flashcard Admin URLs
    path('admin/create/', CreateFlashcard.as_view(), name='createflashcard'),
    path('admin/flashcarddetail/<int:pk>/', AdminFlashcardDetail.as_view(), name='admindetailflashcard'),
    path('admin/edit/<int:pk>/', EditFlashcard.as_view(), name='editflashcard'),
    path('admin/delete/<int:pk>/', DeleteFlashcard.as_view(), name='deleteflashcard'),
]