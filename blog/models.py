from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=150)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self): # this makes title is displayed in django admin page instead of 'object 1, object 2, etc.'
        return self.title

    def summary(self):
        return self.body[:100] + '...'

    def pub_date_pretty(self):
        return  self.pub_date.strftime('%b %e %Y')

