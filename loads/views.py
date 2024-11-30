from django.shortcuts import render, redirect
from django.views import generic
from .models import Load, Location
from django.contrib.auth.decorators import login_required

class LocationDetailView(generic.DetailView):
    model = Location
    template_name = "loads/location_detail.html"

class LoadDetailView(generic.DetailView):
    model = Load
    template_name = "loads/load_detail.html"



def add_load_location(request):
    address_1 = request.GET.get('address_1')
    address_2 = request.GET.get('address_2')
    city = request.GET.get('city')
    country = request.GET.get('country')
    if country == "":
        field_country = "Zimbabwe"
    else: 
        field_country = country
    location= Location(address_1=address_1, address_2=address_2, city=city, country=field_country)
    location.save()
    return redirect('loads:new_load')

class LoadListView(generic.ListView):
    model = Load
    template_name = "loads/loads.html"

class LoadUpdateView(generic.UpdateView):
    model = Load
    template_name = "loads/load_update.html"

class LoadCreateView(generic.CreateView):
    model = Load
    template_name = "loads/new_load.html"
    fields = ['origin', 'destination', 'type', 'weight', 'rate']

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)


@login_required(login_url="login")
def my_loads(request):
    my_loads = Load.objects.filter(owner=request.user.profile)
    return render(request, 'loads/my_loads.html', {'my_loads': my_loads})

