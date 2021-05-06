from django.urls import path

from .views import BookmarkListView, BookmarkCreateView, BookmarkUpdateView, BookmarkDetailView, BookmarkDeleteView

app_name = 'bookmark'


urlpatterns = [
    path('', BookmarkListView.as_view(), name='list'),  # {% url 'bookmark:list' %}
    path('add/', BookmarkCreateView.as_view(), name='add'),  #{% url 'bookmark:add' %}
    path('detail/<int:pk>', BookmarkDetailView.as_view(), name='detail'),  # {% url 'bookmark:detail' %}
    path('update/<int:pk>', BookmarkUpdateView.as_view(), name='update'),  # {% url 'bookmark:update' %}
    path('delete/<int:pk>', BookmarkDeleteView.as_view(), name='delete'),  # {% url 'bookmark:delete' %}
]