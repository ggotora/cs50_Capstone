from django.shortcuts import render
from django.views import generic 
from loads.models import Load 
from .models import Profile
from django.urls import reverse, reverse_lazy
from .forms import ProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from allauth.account.views import SignupView



class HomeView(generic.ListView):
    template_name = 'main/home.html' 

    def get_queryset(self):
        return Load.objects.all()
    
class ProfileDetailView(LoginRequiredMixin, generic.DetailView):
    model = Profile
    template_name = "main/profile.html"

class ProfileUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Profile
    template_name = "main/profile_update.html"
    form_class = ProfileForm

    def get_success_url(self):
        pk = self.kwargs["pk"]

        return reverse_lazy('main:profile', kwargs={'pk':pk})
    
def incomplete_profile(request):
    if request.method == "POST":
        print('posting')
    form = ProfileForm()
    return render(request, 'main/incomplete_profile.html', {'form': form})

    # def get_success_url(self):
    #     pk = self.kwargs["pk"]
    #     return reverse("main:profile", kwargs={"pk": pk})