import uuid

from django.db import models


class Book(models.Model):
    """本モデル"""

    class Meta:
        db_table = 'book'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(verbose_name='タイトル', max_length=20)
    price = models.IntegerField(verbose_name='価格', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)

    def __str__(self):
        return self.title


class Book2(models.Model):
    """本モデル"""

    class Meta:
        db_table = 'book2'

    title = models.CharField(verbose_name='タイトル', max_length=20)
    price = models.IntegerField(verbose_name='価格', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)

    def __str__(self):
        return self.title


class JobOffer(models.Model):
    company_name = models.CharField(max_length=50)
    company_email = models.EmailField()
    job_title = models.CharField(max_length=60)
    job_description = models.TextField()
    salary = models.PositiveIntegerField()
    prefectures = models.CharField(max_length=35)
    city = models.CharField(max_length=35)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.company_name
