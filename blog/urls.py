from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
 # post views
 path('', views.index, name='index'),
 path('list/', views.post_list, name='post_list'),
 path('<int:year>/<int:month>/<int:day>/<slug:post>/',views.post_detail,name='post_detail'),
 path('category/<int:id>/',views.category,name="category"),
 path('about/',views.about,name="about"),
]