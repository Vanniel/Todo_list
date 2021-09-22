from django import urls
from django.conf.urls import url
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from base.views import  TaskList, DeleteView, CustomLoginView,TaskCreate,TaskDetail



class TestUrls(SimpleTestCase):
    def test_login_url_is_resolved(self):
     url = reverse('list')
     self.assertEquals(resolve(url).func, TaskList)


    def test_add_url_resolves(self):
        url = reverse('add')
        self.assertEquals(resolve(url).func.view_class, TaskCreate )

    def test_detail_url_resolves(self):
        url=reverse('details', args=['some-slug'])
        self.assertEquals(resolve(url).func, TaskDetail )