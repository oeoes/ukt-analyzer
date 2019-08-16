from django.shortcuts import render
from classification_app.tools import mechine, processor
import numpy as np


def predict_ukt(request):
    data = []
    data.extend([
        request.POST.get('status_kep_rumah'),
        request.POST.get('penghasilan_utm_ayah'),
        request.POST.get('penghasilan_tmbh_ayah'),
        request.POST.get('penghasilan_utm_ibu'),
        request.POST.get('penghasilan_tmbh_ibu'),
        request.POST.get('pajak_r2'),
        request.POST.get('pajak_r4'),
        request.POST.get('daya_listrik'),
        request.POST.get('pbb'),
    ])
    hasil = mechine.decide_golongan(request.POST.get('jurusan'), mechine.analyze_tanggungan(mechine.predict_data(data), request.POST.get('tanggungan')))
    context = {
        'golongan': hasil.get('golongan'),
        'nominal': hasil.get('nominal'),
        'skor': np.round(hasil.get('skor'), 2),
        'nama': request.POST.get('name'),
        'nim': request.POST.get('nim'),
        'email': request.POST.get('email'),
        'jurusan': processor.jurusan(request.POST.get('jurusan')),
        'p_ayah': processor.penghasilan(request.POST.get('penghasilan_utm_ayah')),
        'pt_ayah': processor.penghasilan(request.POST.get('penghasilan_tmbh_ayah')),
        'p_ibu': processor.penghasilan(request.POST.get('penghasilan_utm_ibu')),
        'pt_ibu': processor.penghasilan(request.POST.get('penghasilan_tmbh_ibu')),
        'rumah': processor.rumah(request.POST.get('status_kep_rumah')),
        'r2': processor.pajakr2(request.POST.get('pajak_r2')),
        'r4': processor.pajakr4(request.POST.get('pajak_r4')),
        'listrik': processor.listrik(request.POST.get('daya_listrik')),
        'pbb': processor.pbb(request.POST.get('pbb')),
        'tanggungan': processor.tanggungan(request.POST.get('tanggungan')),
    }
    return render(request, 'app/result.html', context)

def ukt_analyzer(request):
    return render(request, 'app/ukt-analyzer.html')