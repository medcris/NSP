from django.test import TestCase,Client
from django.shortcuts import reverse
from accounts.models import UserProfile
from django.contrib.auth.models import User
# Create your tests here.

class TestViews(TestCase):
	def setUp(self):
		self.client = Client()
		self.user_object = User.objects.create(username="testing",
											   password="testing")
		self.client.force_login(self.user_object)

	def test_views_200(self):
		pathnames = ["home","view_profile","change_profile_picture",
					"registersucess","signup","view_people",
					"password_reset_complete","password_reset_done",
					"reset_password","change_password","edit_profile"]
		for pathname in pathnames:
			url = reverse(pathname)
			response = self.client.get(url)
			self.assertEqual(response.status_code,200)

	def test_follow_user_view_get(self):
		url = reverse("follow_user",args=[self.user_object.id])
		response = self.client.get(url)
		self.assertEqual(response.status_code,302)
		self.assertEqual(response.url,reverse("view_friend",args=[self.user_object.username]))
