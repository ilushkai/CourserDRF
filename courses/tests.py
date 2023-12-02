
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from courses.models import *
from users.models import User


class CoursesTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            email="admin@adm.ru", password="1q2w!Q@W", is_active=True, is_superuser=True
        )
        self.user.save()
        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(
            title='Course1',
            description='Desc'
        )

        self.lesson = Lesson.objects.create(
            title='Lesson1',
            description='Desc',
            course=self.course
        )

    def test_get_list(self):
        """Test for getting list of lessons"""

        response = self.client.get(
            reverse('courses:lesson-list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK

        )

        self.assertEqual(
            response.json(),
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [{'course': 'Course1', 'title': 'Lesson1'}]
            }
        )

    def test_lesson_create(self):
        """ Test for lesson create """

        data = {
            'title': 'Lesson2',
            'course': self.course.id
        }

        response = self.client.post(
            reverse('courses:lesson-create'),
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_lesson_delete(self):
        """Test for delete lesson"""

        url = reverse('courses:lesson-delete', kwargs={'pk': self.lesson.pk})

        response = self.client.delete(url)

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_sub_create(self):
        """ Test for create sub """

        data = {
            'user': self.user,
            'is_active': True
        }

        response = self.client.post(
            reverse('courses:subscriptions'),
            data=data
        )

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)