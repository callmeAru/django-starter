from django.db import models

class Database(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128) 

    def str(self):
        return self.email