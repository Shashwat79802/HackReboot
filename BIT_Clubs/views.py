from django.shortcuts import render
from .models import Club, TeamMember


def clubs_list(request):
    club_list = Club.objects.all()
    return render(request, 'BIT_Clubs/index.html', {'club_list': club_list})


def club_description(request, club_name):
    club = Club.objects.get(name=club_name)
    return render(request, 'BIT_Clubs/club_desc.html', {'club': club})