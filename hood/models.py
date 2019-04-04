from django.db import models
# from django.contrib.auth.models import Admin
import datetime

# Create your models here.

class NeighbourHood(models.Model):
    # admin = models.OneToOneField(Admin, on_delete=models.CASCADE,primary_key=True)
    neighbourhood_name = models.CharField(max_length=30)
    neighbourhood_location = models.CharField(max_length=30)
    occupants_count = models.CharField(max_length =200)
    

    def __str__(self):
        return self.neighbourhood_name

#     def save_profile(self):
#         self.save()

#     def delete_profile(self):
#         self.delete()

#     @classmethod
#     def get_profile(cls):
#         profile = cls.objects.all()
#         return profile
    
#     def update_bio(self,bio):
#         self.bio = bio
#         self.save()
        
#     @classmethod
#     def search_by_name(cls,search_term):
#         profile = cls.objects.filter(name__icontains=search_term)
#         return profile
    
class User(models.Model):
    name = models.CharField(max_length =60)
    id = models.IntegerField(primary_key=True)
    neighborhood = models.ForeignKey(NeighbourHood,on_delete=models.CASCADE)
    email_address = models.CharField(max_length =200)

    def __str__(self):
        return self.name
    
#     def save_project(self):
#         self.save()

#     @classmethod
#     def get_projects(cls):
#         projects = cls.objects.all()
#         return projects    

#     def delete_project(self):
#         self.delete()

#     @classmethod
#     def search_by_project(cls,search_term):
#         projects=cls.objects.filter(name__icontains=search_term)
    
#         return projects

# class ProjectLetterForm(models.Model):
#     name = models.CharField(max_length = 30)
#     email = models.EmailField()

class Business(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=True)
    business_name =  models.CharField(max_length =60)
    neighborhood = models.ForeignKey(NeighbourHood,on_delete=models.CASCADE,default=True)
    business_email_address =   models.CharField(max_length =60)
    posted_on = models.DateTimeField(default=datetime.datetime(2015, 12, 26, 17, 1, 28, 128127))

    def __str__(self):
        return self.business_name

#     @classmethod
#     def count_posts(cls,id):
#         Votes.objects.all().count()