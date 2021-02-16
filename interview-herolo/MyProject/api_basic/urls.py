from django.urls import path
from .views import ArticleAPIView, ArticleDetails, GenericAPIView, GetSpecificAuthor, GetSpecificAuthorUnread
urlpatterns = [
    path('all_message/', ArticleAPIView.as_view()),
    path('message/<int:id>/', ArticleDetails.as_view()),
    path('new_message/', ArticleAPIView.as_view()),
    path('message/<int:id>/delete', GenericAPIView.as_view()),
    path('get_specific_user/<str:sender>/', GetSpecificAuthor.as_view()),
    path('get_specific_user_unread/<str:sender>/<read>/', GetSpecificAuthorUnread.as_view()),

]