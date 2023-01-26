from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        "название",
        help_text="введите название группы "
                  "(макс. 200 символов)",
        max_length=200,
    )
    slug = models.SlugField(
        "адрес",
        help_text="введите уникальный адрес группы",
        unique=True,
    )
    description = models.TextField(
        "описание",
        help_text="введите описание сообщества",
    )

    def __str__(self) -> str:
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        related_name='posts', blank=True, null=True
    )

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        help_text="пользователь, который подписывается",
        related_name="follower",
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="following",
        help_text="автор на кого подписываются",
        verbose_name="Автор",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['following', 'user'],
                                    name='unique_follow'),
            models.CheckConstraint(check=~models.Q(following=models.F('user')),
                                   name='cant_follow_yourself'),
        ]
