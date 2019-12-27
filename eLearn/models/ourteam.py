from django.db import models

class ourTeam(object):
	"""docstring for ourTeam, Aryid team members"""
	FullName = models.CharField(max_length = 60)
	description = models.TextField(null = True)
	JobTitle = models.CharField(max_length = 60)
	pic = models.filefield(upload_to = 'uploads/ourTeam/%Y/%m/%d/')
	status = models.BooleanField(default = True)
