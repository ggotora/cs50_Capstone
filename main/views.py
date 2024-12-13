from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic 
from loads.models import Load 
from .models import Profile
from django.urls import reverse, reverse_lazy
from .forms import ProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
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

# require_POST('POST')
def incomplete_profile(request):
    # pk=pk
    user = get_object_or_404(Profile, id=request.user.profile.id)
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            object = form.save()
            return redirect(object.get_absolute_url())
    return render(request, 'main/incomplete_profile.html',{ 'form': form, 'profile': user })
    # user = get_object_or_404(Profile, id=pk)
    # form = ProfileForm(instance=user)
    # if request.method == "POST":
    #    form = ProfileForm(request.POST, instance=user)
    #    if form.is_valid():
    #        print(user)
    #        form.save()
    #        return redirect(Profile)
    # form = ProfileForm()
    # return render(request, 'main/incomplete_profile.html', {'form': form})
       
           
    
    if request.method == "POST":
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            user = get_object_or_404(Profile, pk=request.user.id)
            form.instance.user  = request.user.profile.user
            form.save()
            return redirect('main:home')
    form = ProfileForm()
    return render(request, 'main/incomplete_profile.html', {'form': form})
    # if request.method == "POST":
        # form = ProfileForm(request.POST or None)
        # if form.is_valid():
            # form.instance.user = request.user.id 
            # form.save()
            # return redirect('home')
        
    # form = ProfileForm()

    # return render(request, "main/incomplete_profile.html", {"form": form})
   