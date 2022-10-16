from django.test import TestCase
from django.conf import settings

from ...models import Group, Post, User


class PostModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='auth')
        cls.group = Group.objects.create(
            title='Тестовая группа',
            slug='Тестовый слаг',
            description='Тестовое описание',
        )
        cls.post = Post.objects.create(
            author=cls.user,
            text='Тестовый пост который длинный',
        )
        cls.field_str = {
            cls.post.text[:settings.TEST_NUMBER]: str(cls.post),
            cls.group.title: str(cls.group),
        }
        cls.field_verboses = {
            'text': 'Текст поста',
            'pub_date': 'Дата публикации',
            'author': 'Автор',
            'group': 'Группа',
        }
        cls.field_help_texts = {
            'text': 'Введите текст поста',
            'group': 'Группа, к которой будет относиться пост',
        }

    def test_models_have_correct_object_names(self):
        """Проверяем, что у моделей корректно работает __str__."""
        for field, expected_value in self.field_str.items():
            self.assertEqual(field, expected_value)

    def test_verbose_name(self):
        """verbose_name в полях совпадает с ожидаемым."""
        for field, expected_value in self.field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(
                    self.post._meta.get_field(field).verbose_name,
                    expected_value)

    def test_help_text(self):
        """help_text в полях совпадает с ожидаемым."""
        for field, expected_values in self.field_help_texts.items():
            with self.subTest(field=field):
                self.assertEqual(
                    self.post._meta.get_field(field).help_text,
                    expected_values)
