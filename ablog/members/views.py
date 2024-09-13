from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm,Edit_Profile_Form,Update_Password_Form


def Password_changed_successfully(request):
    return render(request,'registration/Password_changed_successfully.html',{})

class PasswordChange(PasswordChangeView):
    form_class = Update_Password_Form
    success_url = reverse_lazy('Password_changed_successfully')

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = Edit_Profile_Form
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
      # Ensure that the current user is the one being edited
      return self.request.user