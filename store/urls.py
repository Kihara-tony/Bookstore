from django.conf.urls import url,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

# adding url
urlpatterns = [
    url('^$', views.welcome, name='welcome'), #home
    url(r'books/', views.books, name='books'), #portfolio
    url(r'teachers/', views.teachers, name='teachers'), #contact
    url(r'profile/',views.profile,name='profile'),
    url(r'edit_profile/',views.edit_profile,name='editprofile'),
    url(r'addbook/',views.new_book,name="addbook"),
    url(r'addteacher/',views.create_teacher,name='addteacher'),
    # url(r'addteacher/<int:id>/',views.addteacher,name='addteacher'),
    url(r'about/',views.about,name='about')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
