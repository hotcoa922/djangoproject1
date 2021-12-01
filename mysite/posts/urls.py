from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', view=views.post_list, name='list'),
    path('create/', view=views.post_create, name='create'),
    path('<int:pk>/update/', view=views.post_update, name='update'),
    path('<int:pk>/delete/', view=views.post_delete, name='delete'),
    path('<int:pk>/detail/', view=views.post_detail, name='detail'),
]