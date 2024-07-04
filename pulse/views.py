from django.shortcuts import redirect, render
from pulse.forms import PulseForm
from django.contrib.auth.decorators import login_required
from .models import Pulse

def feed_view(request):
    context = {
        'pulses': Pulse.objects.all()
    }
    
    return render(request, 'pages/pulse.html', context)


@login_required
def upload_pulse_view(request):
    if request.method == 'POST':
        form = PulseForm(request.POST, request.FILES)
        if form.is_valid():
            Pulse = form.save(commit=False)
            Pulse.artist = request.user  
            Pulse.save()
            print("succes")
    else:
        form = PulseForm()
    
    return render(request, 'pages/upload_pulse.html', {'form': form})