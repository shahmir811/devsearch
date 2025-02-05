from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Profile
from .forms import CustomUserCreationForm, ProfileForm, SkillForm

# Create your views here.
def loginUser(request):
  page = 'login'
  context = { 'page': page }
  if request.user.is_authenticated:
    return redirect('profiles')


  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')

    try:
      user = User.objects.get(username=username)
    except:
      messages.error(request, 'User does not exist')

    user = authenticate(request, username=username, password=password)

    if user is not None:
      login(request, user)
      return redirect('profiles')
    else:
      messages.error(request, 'Username OR password is incorrect')

    print(username, password)
    # return redirect('profiles')

  return render(request, 'users/login_register.html', context)


def logoutUser(request):
  logout(request)
  messages.info(request, 'User was successfully logged out')
  return redirect('login')

def registerUser(request):
  page = 'register'
  form = CustomUserCreationForm()

  if request.method == 'POST':
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.username = user.username.lower()
      user.save()
      messages.success(request, 'User was successfully registered')
      login(request, user)
      return redirect('edit-account')
    else:
      messages.error(request, 'An error has occurred during registration')

  context = { 'page': page, 'form': form }
  return render(request, 'users/login_register.html', context)

def profiles(request):
    profiles = Profile.objects.all()
    context = {
        'profiles': profiles
    }
    return render(request, 'users/profiles.html', context)

def user_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    # Filter skills with descriptions
    skills_with_description = profile.skill_set.exclude(description__exact='')
    
    # Filter skills without descriptions
    skills_without_description = profile.skill_set.filter(description__exact='')

    context = {
        'profile': profile,
        'skills_with_description': skills_with_description,
        'skills_without_description': skills_without_description,
    }
    return render(request, 'users/user-profile.html', context)


@login_required(login_url='login')
def user_account(request):
    profile = request.user.profile
    skills = profile.skill_set.all()
    projects = profile.project_set.all()

    context = {
        'profile': profile,
        'projects': projects,
        'skills': skills,
    }
    return render(request, 'users/account.html', context)


@login_required(login_url='login')
def edit_account(request):
  profile = request.user.profile
  form = ProfileForm(instance=profile)

  if request.method == 'POST':
    form = ProfileForm(request.POST, request.FILES, instance=profile)
    if form.is_valid():
      form.save()
      return redirect('user-account')

  context = { 'form': form }
  return render(request, 'users/profile_form.html', context)

@login_required(login_url='login')
def create_skill(request):
  profile = request.user.profile
  form = SkillForm()

  if request.method == 'POST':
    form = SkillForm(request.POST)
    if form.is_valid():
      skill = form.save(commit=False)
      skill.owner = profile
      skill.save()
      messages.success(request, 'Skill was added successfully')
      return redirect('user-account')

  context = { 'form': form }
  return render(request, 'users/skill_form.html', context)


@login_required(login_url='login')
def update_skill(request, pk):
  profile = request.user.profile
  skill = profile.skill_set.get(id=pk)
  form = SkillForm(instance=skill)

  if request.method == 'POST':
    form = SkillForm(request.POST, instance=skill)
    if form.is_valid():
      form.save()
      messages.success(request, 'Skill was updated successfully')
      return redirect('user-account')

  context = { 'form': form }
  return render(request, 'users/skill_form.html', context)

def delete_skill(request, pk):
  profile = request.user.profile
  skill = profile.skill_set.get(id=pk)

  if request.method == 'POST':
    skill.delete()
    messages.success(request, 'Skill was deleted successfully')
    return redirect('user-account')

  context = { 'object': skill }
  return render(request, 'delete-template.html', context)