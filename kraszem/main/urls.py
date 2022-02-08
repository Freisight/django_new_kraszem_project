from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('cottages/<int:direct>/<int:cottage_id>/', views.village, name="cottage")
    # path('news/', views.news, name="news"),
    # path('news/<slug:cat>/', views.newsCat, name="news"),
    # re_path(r'^archive/(?P<year>[0-9]{4})/', views.archive, name="archive")
]

