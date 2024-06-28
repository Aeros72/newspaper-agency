from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from newspaper.models import Topic, Newspaper, Redactor


class ModelTests(TestCase):
    def test_topic_str(self):
        topic = Topic.objects.create(
            name="Test Topic",
        )

        self.assertEqual(str(topic), topic.name)

    def test_newspaper_str(self):
        topic = Topic.objects.create(
            name="Test Topic",
        )

        newspaper = Newspaper.objects.create(
            title="Test Title",
            content="Test Content",
            published_date=datetime.now(),
            topic=topic,
        )

        self.assertEqual(str(newspaper), newspaper.title)

    def test_redactor_str(self):
        redactor = get_user_model().objects.create(
            username="test",
            first_name="test_fn",
            last_name="test_ln"
        )

        self.assertEqual(
            str(redactor),
            f"{redactor.username} ({redactor.first_name} {redactor.last_name})"
        )

    def test_create_redactor_with_years_of_experience(self):
        username = "test"
        years_of_experience = 15

        redactor = get_user_model().objects.create(
            username=username,
            years_of_experience=years_of_experience
        )

        self.assertEqual(username, redactor.username)
        self.assertEqual(years_of_experience, redactor.years_of_experience)

    def test_get_absolute_url(self):
        redactor = Redactor.objects.create(
            username="test_user",
            first_name="test_fn",
            last_name="test_ln",
            years_of_experience=15
        )

        expected_url = reverse("newspaper:redactor-detail", kwargs={"pk": redactor.pk})
        self.assertEqual(redactor.get_absolute_url(), expected_url)
