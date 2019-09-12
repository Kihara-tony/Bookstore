from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from io import BytesIO
from django.core.files import File


# Create your models here.
GENDER_CHOICES =(
    ("MALE","Male"),
    ("FEMALE","Female"),
    ("OTHERS","Others"),
)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    pic = models.ImageField(upload_to='media/', null=True)
    bio = models.CharField(default="Hi!", max_length = 30)
    def __str__(self):
        return self.user.username
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class Teacher(models.Model):
    '''
    class for creating teachers details
    '''
    name = models.CharField(max_length=25, null=False)
    teach_pic =models.ImageField(upload_to='media/',null=False)
    gender = models.CharField(max_length=100,choices=GENDER_CHOICES)
    school = models.CharField(max_length=100, null=False)
    available = models.CharField(max_length=5, null=True,default='Yes/No')
    number = models.IntegerField(blank=True)
    subject = models.TextField(max_length=10000, null=False)
    def __str__(self):
        return self.name

    def create_teacher(self):
        self.save()
        
    def update_teacher(self):
        self.update()
        
    def delete_teacher(self):
        self.delete()

    @classmethod
    def find_teacher(cls,teacher_search):
        """
        method to find business by id
        :param teacher_id:
        :return:
        """
        teacher = cls.objects.filter(name=teacher_search)
        return teacher
class Books(models.Model):
    '''
    class to add the books
    '''
    book_name = models.CharField(max_length=25, null=False,default='The abandon')
    author =models.CharField(max_length=25,null=False)
    pic_cover= models.ImageField(upload_to='media/', null=True)
    content= models.FileField(upload_to='pdfs/',null=False)
    # text=models.TextField(upload_to='pdfs/',null=False)
    def __str__(self):
        return self.author

    def create_books(self):
        self.save()
        
    def update_books(self):
        self.update()
        
    def delete_books(self):
        self.delete()
        
    
    @classmethod
    def find_books(cls,book_search):
        """
        method to find business by id
        :param books_id:
        :return:
        """
        books = cls.objects.filter(name=book_search)
        return books
class Comment(models.Model):
    """
    class for creating comments on posts
    """
    comment = models.CharField(max_length=10000, null=True)
    teacher_comment = models.ForeignKey(Teacher,related_name='comment', null=True)
    book =models.ForeignKey(Books,related_name='comment',null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment", null=True)

    def save_comment(self):
        self.save()
