from django.db import models

class Whatever(models.Models):
    title = models.CharField(max_lenght=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title
