from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.


def main_page(request):

    return render(request, 'main_page.html')


def registration_page(request):

    return render(request, 'registration_page.html')


def account_page(request, name_of_user):

    return render(request, 'account_page.html', {'name_of_user' : name_of_user})


def users_list_page(request):

    return render(request, 'users_list_page.html')


def blog_list_page(request):

    return render(request, 'blogs_list_page.html')


def user_blog_page(request, name_of_user, name_of_blog):

    return render(request, 'user_blog_page.html', {'name_of_user': name_of_user, 'name_of_blog': name_of_blog})


def user_blog_post_page(request, name_of_user, name_of_blog, post_id):

    return render(request, 'user_blog_post_page.html', {'name_of_user': name_of_user, 'name_of_blog': name_of_blog, 'post_id': post_id})
