from django.db import models
from django.db.models import Model


class Article(Model):
    class Meta:
        db_table = 'article'

    name = models.CharField(null=False, blank=False, max_length=255)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)
    content_mockup = models.TextField(null=False, blank=False)
    category = models.ForeignKey('CategoryArticle', on_delete=models.RESTRICT, null=False)

    def __str__(self):
        return self.name

class CategoryArticle(Model):
    class Meta:
        db_table = 'category_article'

    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
