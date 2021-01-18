from django.test import TestCase
from .models import Post, User

class PostModelTest (TestCase):
    def setUp (self):
        user = User.object.create ()
        Post.objects.create ( author = user, body = 'just a text')

    def test_body_content ( self ):
        post = Post.objects.get (id=1)
        expected_object_name = f'{[post.body]}'
        self.assertEqual (expected_object_name, 'just a text')

class HomePageViewTest (TestCase):
    def setUp (self):
        Post.objects.create (body='Test text for HomePageView')

    def test_view_url_exists_at_proper_location ( self):
        resp = self.client.get('/')
        self.assertEqual (resp.status_code, 200)

    def test_view_url_by_name ( self):
        resp = self.client.get (reverse ('home'))
        self.assertEqual (resp.status_code, 200)

    def test_view_uses__correct_ytemplate (self):
        resp = self.client.get (reverse ('home'))
        self.assertEqual (resp.status_code, 200)
        self.assertTemplateUsed (resp, 'home.html')

class TemplateTestClass(TestCase):
    def setUp(self):
        # Setup run before every test method.
        pass

    def tearDown(self):
        # Clean up run after every test method.
        pass

    def test_something_that_will_pass(self):
        self.assertFalse(False)

    def test_something_that_will_fail(self):
        self.assertTrue(False)