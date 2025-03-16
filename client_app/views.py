# client_app/views.py
from django.shortcuts import render
from django.db.models import Q
from core.models import Medecin, Aspect

def search_doctors(request):
    # 1) Récupérer la liste des spécialités depuis la base
    #    On prend les distinct() pour éviter les doublons
    all_specialties = Medecin.objects.values_list('specialite', flat=True).distinct()

    # 2) Récupérer tous les aspects depuis la table Aspect
    all_aspects = Aspect.objects.values_list('nom_aspect', flat=True).distinct()

    # 3) Récupérer les champs de recherche
    specialite_query = request.GET.get('specialite_query', '')
    aspect_query = request.GET.get('aspect_query', '')

    # 4) Filtrer
    doctors = Medecin.objects.all()

    if specialite_query:
        doctors = doctors.filter(specialite__icontains=specialite_query)

    if aspect_query:
        # On cherche un médecin qui a un commentaire
        # lié à un aspect = aspect_query
        doctors = doctors.filter(
            commentaires__aborder__aspect__nom_aspect__icontains=aspect_query
        ).distinct()

    context = {
        'doctors': doctors,
        'specialite_query': specialite_query,
        'aspect_query': aspect_query,
        'all_specialties': all_specialties,
        'all_aspects': all_aspects,
    }
    return render(request, 'client_app/search_doctors.html', context)
