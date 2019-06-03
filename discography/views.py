import math
from django.shortcuts import render, get_object_or_404
from discography.models import Album, Song, GalleryImage
def main(request):
    return render(request, 'main.html', {})

def albums(request):
    all_albums = Album.objects.all()
    rows =  math.ceil(len(all_albums)/3)
    albums_list = []
    for i in range(0, rows+1):
        album_sublist = []
        for j in range(0, 3):
            if (i*3+j) < len(all_albums):
                album_sublist.append(all_albums[i*3+j])
        albums_list.append(album_sublist)       
    return render(request, 'albums.html', {'albums': albums_list})

def about_album(request, album_name):
    songs = Song.objects.filter(album__name=album_name)
    album = get_object_or_404(Album, name=album_name)
    return render(request, 'about_album.html', {'album': album, 'songs': songs})

def about(request):
    return render(request, 'about.html', {})

def gallery(request):
    all_images = GalleryImage.objects.all()
    count = len(all_images)
    return render(request, 'gallery.html', {'images': all_images, 'count': count})
    
