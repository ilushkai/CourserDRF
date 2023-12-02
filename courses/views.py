from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from rest_framework.response import Response
from courses.paginators import CoursePaginator
from courses.permissions import IsModerator, IsOwner
from courses.serializers import *
from courses.models import *


### ViewSets for Course ###
class CourseViewSet(viewsets.ModelViewSet):
    default_serializer = CourseSerializer
    pagination_class = CoursePaginator
    queryset = Course.objects.annotate(lessons_count=Count('course'))
    serializers = {
        'list': CourseListSerializer,
        'retrieve': CourseDitailSerializer
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [IsAuthenticated, IsOwner]
        else:
            permission_classes = [IsAdminUser | IsOwner]
        return [permission() for permission in permission_classes]



### generics CRUD for Lesson ####

# Create

class LessonCreateAPIView(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsAdminUser | IsModerator ]


# List
class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonListSerializer
    pagination_class = CoursePaginator
    permission_classes = [IsAuthenticated]

# Ditail
class LessonRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonDitailSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsAdminUser | IsOwner]

# Update
class LessonUpdateAPIView(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsAdminUser | IsOwner]

# Delete


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser | IsOwner]



### generics CRUD for Payments ####

# Create

class PaymentsListAPIView(generics.ListAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'lesson')
    ordering_fields = ('date_of_payment', 'payment_method',)


class SubscriptionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        course_pk = self.kwargs.get('course_pk')

        serializer = self.get_serializer(data={'user': request.user.pk, 'course': course_pk})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'Вы подписались на курс.'}, status=status.HTTP_201_CREATED)


