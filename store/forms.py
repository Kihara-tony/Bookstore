from django import forms
from .models import Profile , Books,Teacher,Comment
from pyuploadcare.dj.forms import ImageField

class BooksForm(forms.ModelForm):
    class Meta:
        model =Books
        fields = ("book_name","author","pic_cover","content")
        
class CreateteacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ("name","teach_pic","gender","school","available","number","subject")
        
class EditProfileForm(forms.ModelForm):
    """
    form for editing profile
    """
    class Meta:
        model = Profile
        fields = ['user', 'pic', 'bio']
        
class CommentForm(forms.ModelForm):
    """
    form t create comment
    """
    class Meta:
        model = Comment
        exclude = ['user', 'post']
        fields = ['comment']