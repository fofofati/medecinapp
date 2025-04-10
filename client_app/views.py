from django.shortcuts import render
from django.db.models import Avg, Case, When, FloatField
from core.models import Medecin, Aspect, Aborder

def get_specialties_and_aspects():
    all_specialties = Medecin.objects.values_list('specialite', flat=True).distinct()
    all_aspects = Aspect.objects.values_list('nom_aspect', flat=True).distinct()
    all_villes = Medecin.objects.values_list('quartier__ville', flat=True).distinct()  # Ajouter les villes
    return all_specialties, all_aspects, all_villes

def search_doctors(request):
    all_specialties, all_aspects, all_villes = get_specialties_and_aspects()

    specialite_query = request.GET.get('specialite_query', '')
    aspect_query = request.GET.get('aspect_query', '')
    ville_query = request.GET.get('ville_query', '')  # Recherche par ville

    doctors = Medecin.objects.all()

    if specialite_query:
        doctors = doctors.filter(specialite__icontains=specialite_query)

    if aspect_query:
        # On filtre d'abord les médecins liés à l'aspect
        doctors = doctors.filter(
            commentaires__aborder__aspect__nom_aspect__icontains=aspect_query
        ).distinct()

        # Puis on annote le score en ne prenant en compte QUE les commentaires liés à cet aspect
        doctors = doctors.annotate(
            score=Avg(
                Case(
                    When(
                        commentaires__aborder__aspect__nom_aspect__icontains=aspect_query,
                        commentaires__aborder__polarite='Positif', then=1.0
                    ),
                    When(
                        commentaires__aborder__aspect__nom_aspect__icontains=aspect_query,
                        commentaires__aborder__polarite='Negatif', then=-1.0
                    ),
                    default=0.0,
                    output_field=FloatField(),
                )
            )
        ).filter(score__gte=0.80)

    if ville_query:
        # Filtrer les médecins par ville (via le quartier)
        doctors = doctors.filter(quartier__ville__icontains=ville_query)

    context = {
        'doctors': doctors,
        'specialite_query': specialite_query,
        'aspect_query': aspect_query,
        'ville_query': ville_query,  # Ajouter la variable ville_query
        'all_specialties': all_specialties,
        'all_aspects': all_aspects,
        'all_villes': all_villes,  # Ajouter la liste des villes
    }
    return render(request, 'client_app/search_doctors.html', context)

def public_doctors(request):
    """
    Affiche la liste de tous les médecins sans aucun filtrage.
    """
    doctors = Medecin.objects.all()
    return render(request, 'client_app/public_doctors.html', {'doctors': doctors})

def about(request):
    """
    Affiche une page "À propos".
    """
    return render(request, 'client_app/about.html')
