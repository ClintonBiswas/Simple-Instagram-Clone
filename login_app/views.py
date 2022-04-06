from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from login_app.forms import CreateUserForm, profileForm
from django.contrib.auth import authenticate, login, logout
from login_app.models import userProfile, Follow
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from app_post.forms import PostForm

# Create your views here.
def sign_up(request):
    registered = False
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            registered = True
            user_profile = userProfile(user=user)
            user_profile.save()
            return HttpResponseRedirect(reverse('login_app:login_page'))
    diction = {'title': 'Sign Up . Instagram', 'form': form}
    return render(request, 'login_app/sign_up.html', context=diction)

def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('app_post:home'))
    return render(request, 'login_app/login_page.html', context={'title': 'Login', 'form':form})
@login_required
def edit_profile(request):
    current_user = userProfile.objects.get(user=request.user)
    form = profileForm(instance=current_user)
    if request.method == 'POST':
        form = profileForm(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save(commit=True)
            form = profileForm(instance=current_user)
            return HttpResponseRedirect(reverse('login_app:user'))
    return render(request, 'login_app/profile.html', context={'title': 'Profile', 'form':form})

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login_app:login_page'))

@login_required
def profile(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'login_app/user.html', context={'title':'User', 'form': form})

@login_required
def user_other_profile(request, username):
    user_other = User.objects.get(username=username)
    already_followed = Follow.objects.filter(follower=request.user, following=user_other)
    if user_other == request.user:
        return HttpResponseRedirect(reverse('login_app:user'))
    return render(request, 'login_app/user_other.html', context={'user_other':user_other, 'already_followed': already_followed})

@login_required
def follow(request, username):
    following_user = User.objects.get(username=username)
    follwer_user = request.user
    already_followed = Follow.objects.filter(follower=follwer_user, following=following_user)
    if not already_followed:
        follwed_user = Follow(follower=follwer_user, following=following_user)
        follwed_user.save()
    return HttpResponseRedirect(reverse('login_app:user_other', kwargs={'username':username}))

@login_required
def unfollow(request, username):
    following_user = User.objects.get(username=username)
    follwer_user = request.user
    already_followed = Follow.objects.filter(follower=follwer_user, following=following_user)
    already_followed.delete()
    return HttpResponseRedirect(reverse('login_app:user_other', kwargs={'username':username}))
