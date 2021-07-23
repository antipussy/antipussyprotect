import base64

from django.urls import path
from django.http import FileResponse

import requests


def download_crypt_file(request, task_id):
    with requests.session() as session:
        download_url = 'https://cryptor.biz/api/crypt/download'
        data = {'apikey': '2dba068b223896703c02a938f8f10fdf45d6f4ba',
                'task_id': task_id}
        r = session.post(download_url, data=data)
    response_data = r.json()
    with open('levi.exe', 'wb') as f:
        f.write(base64.decodebytes(response_data['data'].encode()))
    return FileResponse(open('levi.exe', 'rb'))


urlpatterns = [
    path('download/<str:task_id>/', download_crypt_file)
]
