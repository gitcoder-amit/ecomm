from django.db import models

class Dryfruit(models.Model):
    name=models.CharField(max_length=30)
    desc=models.TextField()
    price=models.IntegerField(default=0)
    cr_date=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='images//',default='')

    def __str__(self):
        return self.name
