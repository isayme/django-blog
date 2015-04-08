# -*- coding: utf-8 -*-

from django.test import TestCase
from models import Category, Tag

# Create your tests here.
class CategoryTest(TestCase):
    def setUp(self):
        Category.objects.create(name=u'Default', description=u'默认分类')
        Category.objects.create(name=u'技术', description=u'技术文章')
        Category.objects.create(name=u'日记')

    def test_exists(self):
        obj1 = Category.objects.get(name=u'日记')
        obj2 = Category.objects.get(name=u'技术')

        self.assertEquals(Category.objects.all().count(), 3)
        self.assertEquals(obj1.description, u'')
        self.assertEquals(obj2.description, u'技术文章')

class TagTest(TestCase):
    def setUp(self):
        Tag.objects.create(name=u'linux', description=u'linux~~')
        Tag.objects.create(name=u'Django', description=u'a python framework')

    def test_exists(self):
        obj1 = Tag.objects.get(name=u'Django')
        obj2 = Tag.objects.get(name=u'linux')

        self.assertEquals(Tag.objects.all().count(), 2)
        self.assertEquals(obj1.description, u'a python framework')
        self.assertNotEquals(obj2.description, u'result')


from trie import Trie

class TrieTest(TestCase):
    def setUp(self):
        self.trie = Trie()
        self.trie.insert(u'测试1')
        self.trie.insert(u'abcd')
        self.trie.insert(u'5678')
        self.trie.insert(u'你')


    def test_exists(self):
        self.assertEquals(self.trie.match(u'测试2'), False)
        self.assertEquals(self.trie.match(u'测试1'), True)

        self.assertEquals(self.trie.match(u'我'), False)
        self.assertEquals(self.trie.match(u'你'), True)

        self.assertEquals(self.trie.match(u'abcdefg'), True)
        self.assertEquals(self.trie.match(u'567'), False)

    def test_delete(self):
        self.assertEquals(self.trie.delete(u'测试2'), False)
        self.assertEquals(self.trie.match(u'测试1'), True)
        self.assertEquals(self.trie.delete(u'测试1'), True)
        self.assertEquals(self.trie.match(u'测试1'), False)

        self.trie.insert(u'1234')
        self.trie.insert(u'12345678')
        self.trie.insert(u'123456789')
        self.assertEquals(self.trie.delete(u'1234'), True)
        self.assertEquals(self.trie.match(u'12345678'), True)

        self.assertEquals(self.trie.delete(u'123456789'), True)
        self.assertEquals(self.trie.match(u'12345678'), True)
