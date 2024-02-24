from django.db import models

# Create your models here.
class Lyb(models.Model):
  title = models.CharField(max_length=100)
  author = models.CharField(max_length=50)
  content = models.TextField()
  posttime = models.DateTimeField(auto_now_add=True)

  class Meta:
    db_table = 'd_lyb'