from django.urls import path
from django.views.generic import TemplateView

app_name = 'flashcards'

urlpatterns = [
    path('', TemplateView.as_view(template_name='flashcards/index.html'))
]