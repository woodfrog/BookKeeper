from django.test import TestCase

from .models import Group, Person, Record, Bill


class GroupMethodsTest(TestCase):
    def test_add_a_person(self):
        g = Group(group_name='test')
        g.save()
        p = Person(name='test')
        p.save()
        g.add_a_person(p)
        self.assertEqual(g.record_set.count(), 1)
        self.assertEqual(g.record_set.all()[0].group, g)
        self.assertEqual(g.record_set.all()[0].person, p)
        self.assertEqual(p.groups.all()[0], g)
