from django.test import TestCase

from newspaper.forms import (RedactorCreationForm,
                             RedactorYearUpdateForm,
                             NewspaperSearchForm,
                             TopicSearchForm,
                             RedactorSearchForm)


class FormsTest(TestCase):
    def test_redactor_creation_form_with_firstname_lastname_years_of_experience(self):
        form_data = {
            "username": "test_user",
            "password1": "test_password",
            "password2": "test_password",
            "first_name": "test_name",
            "last_name": "test_surname",
            "years_of_experience": 15
        }
        form = RedactorCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_form_valid(self):
        form_data = {
            "years_of_experience": 15,
        }
        form = RedactorYearUpdateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        form_data = {
            "years_of_experience": -2,
        }
        form = RedactorYearUpdateForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_newspaper_search_form(self):
        form = NewspaperSearchForm(
            data={
                "title": "test"
            }
        )
        self.assertTrue(form.is_valid())

    def test_topic_search_form(self):
        form = TopicSearchForm(
            data={
                "name": "Test"
            }
        )
        self.assertTrue(form.is_valid())

    def test_redactor_search_form(self):
        form = RedactorSearchForm(
            data={
                "username": "test_username"
            }
        )
        self.assertTrue(form.is_valid())
