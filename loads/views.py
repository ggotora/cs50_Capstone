from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Load, Location, LoadStatus
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from main.models import Profile

class LocationDetailView(LoginRequiredMixin,  generic.DetailView):
    model = Location
    template_name = "loads/location_detail.html"

class LoadDetailView(LoginRequiredMixin, generic.DetailView):
    model = Load
    template_name = "loads/load_detail.html"


@login_required(login_url='account_login')
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

class LoadUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Load
    template_name = "loads/load_update.html"
    fields = ['origin', 'destination', 'type', 'weight', 'rate']
    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)

class LoadCreateView(LoginRequiredMixin, generic.CreateView):
    model = Load
    template_name = "loads/new_load.html"
    fields = ['origin', 'destination', 'type', 'weight', 'rate']

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)


@login_required(login_url="account_login")
def my_loads(request):
    my_loads = Load.objects.filter(owner=request.user.profile)
    return render(request, 'loads/my_loads.html', {'my_loads': my_loads})

@login_required(login_url="account_login")
def shipper_loads(request, owner_id):
    loads = Load.objects.filter(owner=owner_id)
    owner = get_object_or_404(Profile, pk=owner_id)
    return render(request, 'loads/shipper_loads.html', {'loads': loads, "owner": owner})

@login_required(login_url='account_login')
def book_load(request, pk):
    load = get_object_or_404(Load, pk=pk)
    load.loadstatus.status = "I"
    load.loadstatus.transporter = request.user.profile
    load.loadstatus.save()
    print(request.user.profile)
    print(load.loadstatus.transporter)
    return redirect('loads:load', pk=pk)

@login_required(login_url="account_login")
def cancel_booking(request, pk):
    load = get_object_or_404(Load, pk=pk)
    load_status = get_object_or_404(LoadStatus, load=load)
    load_status.status = "A"
    load_status.transporter = request.user.profile
    load_status.save()
    return redirect('loads:load', pk=pk)

@login_required(login_url="account_login")
def mark_delivered(request, pk):
    load = get_object_or_404(Load, pk=pk)
    load_status = get_object_or_404(LoadStatus, load=load)
    load_status.status = "D"
    load_status.transporter = request.user.profile
    load_status.save()
    return redirect('loads:load', pk=pk)
