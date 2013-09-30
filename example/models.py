from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=255, null=False, blank=False)
    content = models.TextField(blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'articles'
        ordering = ['-timestamp']

    def __unicode__(self):
        return self.title
