from django.test import TestCase
from django.utils import timezone

from model_mommy import mommy

from .models import Whatever

# models test
"""
class WhateverTest(TestCase):

    def create_whatever(self, title="only a test", body="yes, this is only a test"):
        return Whatever.objects.create(title=title, body=body, created_at=timezone.now())

    def test_whatever_creation(self):
        w = self.create_whatever()
        self.assertTrue(isinstance(w, Whatever))
        self.assertEqual(w.__unicode__(), w.title)
"""


class WhateverTestMommy(TestCase):

    def test_whatever_creation_mommy(self):
        what = mommy.make(Whatever)
        self.assertTrue(isinstance(what, Whatever))
        self.assertEqual(what.__unicode__(), what.title)
