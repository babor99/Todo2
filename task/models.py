from django.db import models


# username: babor
# email: babor@gmail.com
# pass: 8872

# # Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
