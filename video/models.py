# Django packages
from django.db import models
# third party apps
from mptt.models import MPTTModel, TreeForeignKey
# Local apps
from accounts.models import User


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                            related_name='child')
    is_parent = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, null=True, blank=True, allow_unicode=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Video(models.Model):
    master = models.ForeignKey(User, on_delete=models.CASCADE, related_name='videos')
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, null=True, blank=True, allow_unicode=True)
    category = models.ManyToManyField(Category, related_name='cvideos')
    about_video = models.TextField()
    views = models.IntegerField()
    video = models.FileField(upload_to='videos/')
    image = models.ImageField(upload_to='videos/images/')
    time = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title[:20]
