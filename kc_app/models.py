from django.db import models

class FeedModel(models.Model):
	name=models.CharField(max_length=200)
	clg=models.CharField(max_length=200)
	phone=models.IntegerField()
	message=models.CharField(max_length=500)
