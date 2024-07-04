from django.shortcuts import render
from pulse.forms import PulseForm
from django.contrib.auth.decorators import login_required
from .models import Pulse
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Pulse
from django.views.decorators.http import require_POST

def feed_view(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            pulse_id = request.POST.get('pulse_id')  # Assuming you have a hidden input in the form with pulse_id
            pulse = get_object_or_404(Pulse, id=pulse_id)
            if 'like_button' in request.POST:
                if pulse.add_like(request.user):
                    print(JsonResponse({'status': 'success', 'message': 'Pulse liked successfully'}))
                else:
                    print(JsonResponse({'status': 'error', 'message': 'You have already liked this Pulse'}))
            elif 'unlike_button' in request.POST:
                if pulse.remove_like(request.user):
                    print(JsonResponse({'status': 'success', 'message': 'Like removed successfully'}))
                else:
                    print(JsonResponse({'status': 'error', 'message': 'You haven\'t liked this Pulse'}))
        else:
            print(JsonResponse({'status': 'error', 'message': 'User not authenticated'}))

    # If it's a GET request or after handling the POST request
    pulses = Pulse.objects.all()

    context = {
        'pulses': pulses,
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



