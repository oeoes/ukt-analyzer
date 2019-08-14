import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from django.conf import settings
from . import jurusan as j


def data_frame():
    df = pd.read_csv(settings.STATIC_DATA+'/'+'ukt_with_proper_namefield.csv')
    del df['Unnamed: 0']

    return df

def train_algorithm():
    df = data_frame()
    selected_feature = ['status_kep_rumah', 'penghasilan_utm_ayah', 'penghasilan_tmbh_ayah',
                        'penghasilan_utm_ibu', 'penghasilan_tmbh_ibu', 'pajak_r2', 'pajak_r4',
                        'daya_listrik', 'pbb']

    X = df[selected_feature]
    y = df.skor_ukt
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

    regressor = RandomForestRegressor(n_estimators=100, random_state=0)
    regressor.fit(X_train, y_train)

    return regressor

def predict_data(data):
    model = train_algorithm()
    result = model.predict([data])

    return result

def decide_golongan(jurusan, skor_ukt):
    gol = j.jurusan(jurusan, skor_ukt)
    return gol