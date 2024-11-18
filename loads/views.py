from django.shortcuts import render
from django.views import generic
from .models import Load 
from django.contrib.auth.decorators import login_required


class LoadListView(generic.ListView):
    model = Load
    template_name = "loads/loads.html"

class LoadUpdateView(generic.UpdateView):
    model = Load
    template_name = "loads/load_update.html"

class LoadCreateView(generic.CreateView):
    model = Load
    template_name = "loads/new_load.html"


@login_required(login_url="login")
def my_loads(request):
    my_loads = Load.objects.filter(owner=request.user.profile)
    print(my_loads)
    return render(request, 'loads/my_loads.html', {'my_loads': my_loads})

