from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic 
from loads.models import Load 
from .models import Profile
from django.urls import reverse, reverse_lazy
from .forms import ProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST



class HomeView(generic.ListView):
    template_name = 'main/home.html' 

    def get_queryset(self):
        return Load.objects.all()[:6]
    
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

@login_required
def incomplete_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            object = form.save()
            return redirect(object.get_absolute_url())
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'main/incomplete_profile.html',{ 'form': form, 'profile': request.user.profile })
    

