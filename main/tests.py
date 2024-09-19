from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.utils import timezone
from .models import MoodEntry

class MainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 302)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/skibidi/')
        self.assertEqual(response.status_code, 404)

    def test_strong_mood_user(self):
        now = timezone.now()
        user = User.objects.create_user(username='testuser', password='12345')
        mood = MoodEntry.objects.create(
          user = user,
          mood="Happy",
          time = now,
          feelings = "I'm happy, even though my clothes are soaked from the rain :(",
          mood_intensity = 8,
          #sadness_level = 2
        )
        self.assertTrue(mood.is_mood_strong)

    def test_main_template_uses_correct_page_title(self):
        response = Client().get("/")
        html_response = response.content.decode("utf8")
        self.assertIn("PBD Mental Health Tracker", html_response)