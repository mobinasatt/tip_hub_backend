# Django packages
from django.db import models
from django.utils.translation import gettext_lazy as _
# third party apps
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor.fields import RichTextField
# Local apps
from accounts.models import User


class Category(MPTTModel):
    name = models.CharField(max_length=100, verbose_name=_('نام'))
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                            related_name="children", verbose_name=_('فرزند'))
    is_child = models.BooleanField(default=False, verbose_name=_('فرزند است؟'))
    slug = models.SlugField(unique=True, null=True, blank=True, allow_unicode=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('زمان ساخت'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('زمان بروزرسانی'))

    class Meta:
        verbose_name = _('دسته بندی')
        verbose_name_plural = _('دسته بندی ها')

    def __str__(self):
        return self.name


class Video(models.Model):
    master = models.ForeignKey(User, on_delete=models.CASCADE, related_name='videos',
                               verbose_name=_('استاد'))
    title = models.CharField(max_length=100, unique=True, verbose_name=_('عنوان ویدئو'))
    slug = models.SlugField(unique=True, null=True, blank=True, allow_unicode=True)
    category = models.ManyToManyField(Category, related_name='cvideos',
                                      verbose_name=_('دسته بندی ها'))
    about_video = RichTextField(verbose_name=_('درباره ویدئو'))
    views = models.PositiveBigIntegerField(default=1, verbose_name=_('بازدید'))
    video = models.FileField(upload_to='videos/', verbose_name=_('ویدئو'))
    image = models.ImageField(upload_to='videos/images/', verbose_name=_('عکس نمایشی'))
    time = models.IntegerField(default=1, verbose_name=_('زمان ویدئو'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('زمان ساخت'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('زمان بروزرسانی'))

    class Meta:
        verbose_name = _('ویدئو')
        verbose_name_plural = _('ویدئو ها')

    def __str__(self):
        return self.title[:20]

    def video_view(self):
        self.views += 1
        self.save()
