from django.shortcuts import render
from .models import DetectorRange

def home(request):
    context = {
        'results': None,
        'query_time': None
    }
    
    if request.method == 'POST':
        gps_time = request.POST.get('gps_time')
        if gps_time:
            try:
                gps_time = int(gps_time)
                context['query_time'] = gps_time
                
                # Query for segments that contain the GPS time
                active_detectors = DetectorRange.objects.filter(
                    start__lte=gps_time,
                    stop__gt=gps_time
                )
                
                results = []
                for detector in active_detectors:
                    results.append({
                        'ifo': detector.ifo,
                        'range': detector.range,
                        'active': detector.range > 0
                    })
                
                # Add detectors with no data as unknown
                found_ifos = [r['ifo'] for r in results]
                all_ifos = set(DetectorRange.objects.values_list('ifo', flat=True))
                for ifo in all_ifos:
                    if ifo not in found_ifos:
                        results.append({
                            'ifo': ifo,
                            'range': None,
                            'active': None
                        })
                
                context['results'] = sorted(results, key=lambda x: x['ifo'])
                
            except ValueError:
                context['error'] = 'Please enter a valid GPS time'
    
    return render(request, 'detector_ranges/home.html', context)
