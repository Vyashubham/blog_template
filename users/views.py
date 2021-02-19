from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib import messages
# from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
# from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.decorators import login_required
from .models import VyasProfile


def profile(request):
    context = {
        'things': VyasProfile.objects.all()
    }

    return render(request, 'users/profile.html', context)



# class ProfileCreateView(LoginRequiredMixin, CreateView):
#     model = VyasProfile
#     fields = ['Title', 'Description', 'Date_started', 'Date_ended', 'Category', 'profile_image']




# class ProfileUpdateView(LoginRequiredMixin, UpdateView):
#     model = VyasProfile
#     fields = ['Title', 'Description', 'Date_started', 'Date_ended', 'Category', 'profile_image']


# class ProfileDeleteView(LoginRequiredMixin, DeleteView):
#     model = VyasProfile
#     fields = ['Title', 'Description']

#     success_url = '/'





# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'HI,{username}! Login')
#             return redirect('login_view')
#     else:
#         form = UserRegistrationForm()

#     return render(request, 'users/register.html', {'form': form})

# @login_required
# def account(request):
#     if request.method == 'POST':
#         u_form = UserUpdateForm(request.POST, instance=request.user)
#         p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             messages.success(request, f'changes made!')
#             return redirect('profile')

#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)

#     context = {
#         'u_form': u_form,
#         'p_form': p_form
#     }
#     return render(request, 'users/user_profile.html', context)


    