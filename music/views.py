from django.http import HttpResponse
from django.http import JsonResponse
from .models import *
import json
import pickle


def index(request):
    return JsonResponse({'name': 'dev'})


def details(request):
    if request.method == 'GET':

        art = request.GET['artist']
        query = list(Album.objects.filter(artist=art).values('artist', 'album_title', 'genre', 'album_logo'))
        status = 200
        return JsonResponse(data=query, status=200, safe=False)
    elif request.method == 'POST':
        input_data = json.loads(request.body)
        check_artisst = input_data['artist']
        allquery = list(
            Album.objects.filter(artist=check_artisst).values('artist', 'album_title', 'genre', 'album_logo'))

        if allquery:
            return JsonResponse({'msg': 'user already exist'})
        else:
            insert_music = Album.objects.create(artist=input_data['artist'], album_title=input_data['album_title'],
                                                genre=input_data['genre'], album_logo=input_data['album_logo'])
            return JsonResponse({'msg': 'success'})


def song(request):
    if request.method == 'GET':
        song = list(Song.objects.values('file_type', 'song_title'))
        return JsonResponse(data=song, status=200, safe=False)
    elif request.method == 'POST':
        success = 'msg', 'some error occured'
        input_data = json.loads(request.body)
        file_type = input_data['file_type']
        song_title = input_data['song_title']

        album_name = input_data['album_name']
        get_album_id = list(Album.objects.filter(album_title=album_name).values('id'))
        for v in get_album_id:
            query = Song.objects.create(album_id=v.get('id'), file_type=file_type, song_title=song_title)
        if get_album_id:
            return JsonResponse({'msg': 'success'})
        else:
            return JsonResponse({'msg': 'error'})
