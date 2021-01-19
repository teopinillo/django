from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post, User

class PostModelTest (TestCase):
    def setUp (self):
        self.user = get_user_model().objects.create_user (
            username='testuser',
            email = 'test@email.com',
            password='secret'
        )
        self.post = Post.objects.create ( 
            author = self.user,
            title = 'post test title',
            body = 'post test body'
            )

    def test_string_reprsentation (self):
        
        self.assertEqual(f'{self.post.title}', 'post test title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'post test body')

    def test_body_content ( self ):
        post = Post.objects.get (id=1)
        expected_object_name = f'{post.body}'
        self.assertEqual (expected_object_name, 'post test body')

    def test_post_list_view (self):
        response = self.client.get (reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'post test body')
        self.assertTemplateUsed(response,'blog/index.html')
    
    def test_post_detail_view (self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000')
        self.assertEqual (response.status_code, 200)
        self.assertEqual (no_response.status_code, 301)
        self.assertContains (response, 'post test title')
        self.assertTemplateUsed (response, 'blog/post_detail.html')

class HomePageViewTest (TestCase):
    def setUp (self):        
        self.user = get_user_model().objects.create_user (
            username='testuser_22',
            email = 'test_2@email.com',
            password='secret_2'
        )
        self.post = Post.objects.create ( 
            author = self.user,
            title = 'post test title 2',
            body = 'post test body 2'
            )

    def test_view_url_exists_at_proper_location ( self):
        resp = self.client.get('/')
        self.assertEqual (resp.status_code, 200)

    def test_view_url_by_name ( self):
        resp = self.client.get (reverse ('index'))
        self.assertEqual (resp.status_code, 200)

    def test_view_uses__correct_ytemplate (self):
        resp = self.client.get (reverse ('index'))
        self.assertEqual (resp.status_code, 200)
        self.assertTemplateUsed (resp, 'blog/index.html')

"""
class TemplateTestClass(TestCase):
    def setUp(self):
        # Setup run before every test method.
        pass

    def tearDown(self):
        # Clean up run after every test method.
        passindexlo

    def test_something_that_will_pass(self):
        self.assertFalse(False)

    def test_something_that_will_fail(self):
        self.assertTrue(False)

    self.assertContains(response, 'post test body')
"""