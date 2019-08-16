

def jurusan(kode):
    jur = {
        'mn': 'S1 Manajemen',
        'ak': 'S1 Akuntansi',
        'ep': 'S1 Ekonomi Pembangunan',
        'es': 'S1 Ekonomi Syariah',
        'kd': 'S1 Kedokteran',
        'tm': 'S1 Teknik Mesin',
        'hi': 'S1 Hubungan Internasional',
        'if': 'S1 Informatika',
        'si': 'S1 Sistem Informasi',
        'hk': 'S1 Hukum',
        'kp': 'S1 Keperawatan',
        'km': 'S1 Kesehatan Masyarakat',
        'gz': 'S1 Gizi',
        'ti': 'S1 Teknik Industri',
        'tp': 'S1 Teknik Perkapalan',
        'ik': 'S1 Ilmu Komunikasi',
        'ip': 'S1 Ilmu Politik',
    }

    return jur.get(kode)

def penghasilan(val):
    ar = ['Tidak berpenghasilan', 'Kurang dari sama dengan Rp. 500.000', 'Rp. 500.001 - Rp. 1000.000', 'Rp. 1000.001 - Rp. 1.500.000',
          'Rp. 1.500.001 - Rp. 2000.000', 'Rp. 2000.001 - Rp. 2.500.001', 'Rp. 2.500.001 - Rp. 3000.000', 'Rp. 3000.001 - Rp. 4000.000',
          'Rp. 4000.001 - Rp. 5000.000', 'Rp. 5000.001 - Rp. 7.500.000', 'Rp. 7.500.001 - Rp. 10.000.000', 'Rp. 10.000.001 - Rp. 15.000.000',
          'Lebih dari 15.000.000'
          ]
    return ar[int(val)]

def rumah(val):
    ar = ['Tidak memiliki', 'Memiliki rumah sendiri']
    return ar[int(val)]

def pajakr2(val):
    ar = ['Tidak memiliki', 'Lebih kecil sama dengan Rp. 150.000', 'Rp. 150.001 - Rp. 300.000', 'Rp. 300.001 - Rp. 450.000',
          'Rp. 450.001 - Rp. 650.000', 'Rp. 650.001 - Rp. Rp. 850.000', 'Rp. 850.001 - Rp. 1.050.000', 'Lebih besar sama dengan Rp. 1.050.000'
          ]
    return ar[int(val)]

def pajakr4(val):
    ar = ['Tidak memiliki', 'Lebih kecil sama dengan Rp. 1.500.000', 'Rp. 1.500.001 - Rp. 2.500.000', 'Rp. 3.500.001 - Rp. 3.500.000',
          'Rp. 3.500.001 - Rp. 5.000.000', 'Rp. 5.000.001 - Rp. 6.500.000', 'Rp. 6.500.001 - Rp. 8.500.000', 'Lebih besar sama dengan Rp. 8.500.001'
          ]
    return ar[int(val)]

def listrik(val):
    ar = ['Tidak berlangganan', '450W', '900W', '1300W', '2200W', '3500W', '4400W', '5500W', '6600W', '7700W', '11000W ke atas']
    return ar[int(val)]

def pbb(val):
    ar = ['Tidak membayar pajak PBB', 'Lebih kecil sama dengan Rp. 250.000', 'Rp. 250.001 - Rp. 500.000',
          'Rp. 500.001 - Rp. 750.000', 'Rp. 750.001 - Rp. 1.000.000', 'Rp. 1.000.001 - Rp. 1.250.000',
          'Rp. 1.250.001 - Rp. 1.500.000', 'Lebih besar sama dengan 1.500.001'
          ]
    return ar[int(val)]

def tanggungan(val):
    ar = [
        '1 Anak', '1 Anak + Tanggungan Lainya', '2 Anak', '2 Anak + Tanggungan Lainya', '3 Anak', '3 Anak + Tanggungan Lainya',
        '4 Anak', '4 Anak + Tanggungan Lainya'
    ]
    return ar[int(val)]
