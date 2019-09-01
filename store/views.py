from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile, Teacher, Books,Comment
from .forms import  EditProfileForm, TeacherForm, BooksForm, CommentForm
# Create your views here.
def welcome(request):
    
    return render(request,'welcome.html')


def books(request):
    books = Books.objects.all()
    return render(request,'books.html', {'books': books})
def book(request, books_id):
    """
    view function to render book

    """
    comments = Comment.objects.all()
    form = CommentForm()
    book = Books.find_book(book_id)

    return render(request, 'book.html',locals())

# @login_required(login_url='/accounts/login/')
def teachers(request):
    teachers= Teacher.objects.all()
    return render(request,'teachers.html',{'teachers':teachers})
def teacher(request, teacher_id):
    """
    view function to render teacher

    """
    comments = Comment.objects.all()
    form = CommentForm()
    teach = Teacher.find_teacher(teacher_id)
    
    return render(request, 'teacher.html',locals())

@login_required(login_url='/registration/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.get(user =current_user)
    book = Books.objects.filter(user=current_user)
    teacher = Teacher.objects.filter(user= current_user)
    return render(request,'profile.html')

@login_required(login_url='/registration/login/')
def edit_profile(request):
    form = EditProfileForm()
    current_user = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=current_user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    return render(request,'edit_profile.html',{'form':form})
def updateach(request, id):
    """
    create teacher function
    :param request:
    :return:
    """
    tch = Teacher.objects.get(id=id)
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES, instance=tch)
        if form.is_valid():
            b = form.save(commit=False)
            b.user = request.user.profile
            b.teacher = request.user.profile.teacher
            b.save()
        return redirect('teacher', request.user.profile.teacher.id)
    else:
        form = TeacherForm()
    return render(request, 'createteacher.html', locals())

def about(request):
    
    return render(request,'aboutus.html')
def add_book(request,book_id):
    add = get_object_or_404(Books,pk='book_id')
    request.user.profile.books = add
    request.user.profile.save()
    return redirect('profile',book_id)
def exit_teacher(request):
    have = get_object_or_404(Teacher)
    if request.user.profile.teacher == have:
        request.user.profile.teacher = None
        request.user.profile.save()
    return redirect('profile')
def comm(request,id):
    comment = CommentForm(request.POST)
    if comment.is_valid():
        comms = comment.save(commit=False)
        comms.user = request.user
        comms.save()
        return redirect('profile', request.user.profile.books.id)