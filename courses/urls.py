from courses.apps import CoursesConfig
from rest_framework.routers import DefaultRouter
from courses.views import *
from django.urls import path

app_name = CoursesConfig.name


router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')


urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-retrive'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-upadate'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson-delete'),
    ] + router.urls