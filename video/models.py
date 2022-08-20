# Django packages
from django.db import models
from django.utils.translation import gettext_lazy as _
# third party apps
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor.fields import RichTextField
# Local apps
from accounts.models import User
from extensions.utils import jalali_converter


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

    def jalali_date(self):
        return jalali_converter(self.created)
    jalali_date.short_description = 'زمان ساخت'


class Comment(MPTTModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments',
                             verbose_name=_('کاربر'))
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='video_comments',
                              verbose_name=_('ویدئو'))
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                            related_name='children', verbose_name=_('والد'))
    body = models.TextField(max_length=400, verbose_name=_('متن'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('تاریخ ساخت'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('تاریخ بروزرسانی'))

    class Meta:
        verbose_name = _('نظرات')
        verbose_name_plural = _('نظرات')

    def __str__(self):
        return self.body[:20]


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_likes',
                             verbose_name='کاربر')
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='video_likes',
                              verbose_name='ویدئو')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت')

    class Meta:
        verbose_name = 'لایک'
        verbose_name_plural = 'لایک ها'
        ordering = ['-created']

    def __str__(self):
        return f"{self.user.fullname} - {self.video.title}"

    def jalali_date(self):
        return jalali_converter(self.created)
    jalali_date.short_description = 'زمان ساخت'
