from rest_framework import serializers
from rest_framework.fields import SerializerMethodField, IntegerField
from rest_framework.relations import SlugRelatedField
from pay.models import Payments
from courses.models import Course, Lesson, Subscription
from courses.validators import validator_banned_links


########################## Courses serializers ###

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


# List
class CourseListSerializer(serializers.ModelSerializer):
    lessons_count = IntegerField()

    class Meta:
        model = Course
        fields = ('title', 'lessons_count',)


# Ditail
class CourseDitailSerializer(serializers.ModelSerializer):
    lessons_this_course = SerializerMethodField()

    def get_lessons_this_course(self, course):
        return LessonListSerializer(Lesson.objects.filter(course=course), many=True).data

    class Meta:
        model = Course
        fields = '__all__'  # ('title', 'description', 'preview', 'lessons_this_course')


########################## Lessons serializers ###

class LessonSerializer(serializers.ModelSerializer):
    link = serializers.CharField(validators=[validator_banned_links], default=None)
    class Meta:
        model = Lesson
        fields = '__all__'  # ('title', 'description', 'preview' ,'link' ,'course')


# list
class LessonListSerializer(serializers.ModelSerializer):
    course = SlugRelatedField(slug_field='title', queryset=Course.objects.all())

    class Meta:
        model = Lesson
        fields = ('title', 'course')


# ditail
class LessonDitailSerializer(serializers.ModelSerializer):
    course = CourseDitailSerializer()
    lessons_count = SerializerMethodField()

    def get_lessons_count(self, lesson):
        return Lesson.objects.filter(course=lesson.course).count()

    class Meta:
        model = Lesson
        fields = ('title', 'course', 'lessons_count')



########################## Payments serializers ###

class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'  # ('user', 'date_of_payment', 'paid_course' ,'paid_lesson' ,'payment_sum', 'payment_method')


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'

        extra_kwargs = {
            'user': {'required': False}
        }