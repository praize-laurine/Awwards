from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Project(models.Model):
    title = models.TextField(max_length = 30)
    image = models.ImageField(upload_to = 'index/', blank=True)
    url_link = models.URLField(max_length=200)
    description = models.TextField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='', null=True ,related_name='author')
    date_craeted= models.DateField(auto_now_add=True )

    
     def save_project(self):
        self.save()

    @classmethod
    def all_projects(cls) :
        projects = cls.objects.all()
        return projects


    @classmethod
    def search_by_title(cls,search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects


     

    def __str__(self):
        return self.title