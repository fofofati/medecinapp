from django.shortcuts import render
from core.models import Medecin, Aspect

def get_specialties_and_aspects():
    all_specialties = Medecin.objects.values_list('specialite', flat=True).distinct()
    all_aspects = Aspect.objects.values_list('nom_aspect', flat=True).distinct()
    return all_specialties, all_aspects

def search_doctors(request):
    # Récupérer la liste des spécialités et des aspects
    all_specialties, all_aspects = get_specialties_and_aspects()

    # Récupérer les champs de recherche
    specialite_query = request.GET.get('specialite_query', '')
    aspect_query = request.GET.get('aspect_query', '')

    # Filtrer les médecins
    doctors = Medecin.objects.all()

    if specialite_query:
        doctors = doctors.filter(specialite__icontains=specialite_query)

    if aspect_query:
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

def public_doctors(request):
    doctors = Medecin.objects.all()
    return render(request, 'client_app/public_doctors.html', {'doctors': doctors})

def about(request):
    return render(request, 'client_app/about.html')
