from django.urls import path
#from core import views
from core.views import HomePageView,TeacherListView, TeacherCreateView

urlpatterns = [
    #path('', views.home, name='home')
    path('',HomePageView.as_view(), name='home'),
    path('teacher/list/', TeacherListView.as_view(),name='teacher.index'),
    path('teacher/create/',TeacherCreateView.as_view(),name='teacher.create'),
]