from django.test import SimpleTestCase

from app import calc


class CalcTest(SimpleTestCase):

    def test_add_number(self):
        res = calc.add(10, 20)
        self.assertEqual(res, 30)
