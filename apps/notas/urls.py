from django.urls import path
from .views import AnswerView

urlpatterns = [
    path('answer/test/<int:test_id>/', AnswerView.as_view()),
]