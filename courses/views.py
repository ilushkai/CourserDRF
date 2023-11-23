from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import viewsets, generics
from courses.serializers import *
from courses.models import *


### ViewSets for Course ###
class CourseViewSet(viewsets.ModelViewSet):
    default_serializer = CourseSerializer
    queryset = Course.objects.annotate(lessons_count=Count('course'))
    serializers = {
        'list': CourseListSerializer,
        'retrieve': CourseDitailSerializer
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)



### generics CRUD for Lesson ####

# Create

class LessonCreateAPIView(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


# List
class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonListSerializer

# Ditail
class LessonRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonDitailSerializer


# Update
class LessonUpdateAPIView(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

# Delete


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()



### generics CRUD for Payments ####

# Create

class PaymentsListAPIView(generics.ListAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'lesson')
    ordering_fields = ('date_of_payment', 'payment_method',)
