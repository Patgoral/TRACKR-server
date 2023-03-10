from django.db import models
from django.contrib.auth import get_user_model


class Attendee(models.Model):
  name = models.CharField(max_length=100)
  date = models.DateField()
  time = models.TimeField()
  owner = models.ForeignKey(
    get_user_model(), 
    on_delete=models.CASCADE
  )

  def __str__(self):
    return f"'{self.name}' finished on {self.date} at {self.time}"

  def as_dict(self):
    return {
        'id': self.id,
        'name': self.name,
        'date': self.date,
        'time': self.time,
     
    }