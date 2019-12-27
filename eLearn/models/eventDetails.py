from django.db import models
from .events import Events

class EventDetails(object):
	"""docstring for EventDetails, descrip events details and program"""
	event = models.ForeignKey(Events, on_delete = models.CASCADE)
	title = models.CharField(max_length = 60)
	startTime = models.DateTimeField(null = True, blank = True)
	endTime = models.DateTimeField(null = True, blank = True)
	pic = models.fileField(upload_to = 'uploads/events/%Y/%m/%d/')
