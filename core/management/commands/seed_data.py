import random, itertools
from django.core.management.base import BaseCommand
from django.utils import timezone
from core.models import Medecin, Commentaire, Aspect, Aborder

class Command(BaseCommand):
   
    def handle(self, *args, **options):
        
        logical_polarities = {
            "gentillesse": "Positif",
            "ponctualité": "Positif",
            "professionnalisme": "Positif",
            "matérialité": "Negatif",
            "écoute": "Positif",
            "compétence": "Positif",
            "empathie": "Positif",
        }

        # Créer ces aspects dans la base
        aspect_map = {}
        for aspect_name, polarite_defaut in logical_polarities.items():
            aspect_obj, _ = Aspect.objects.get_or_create(nom_aspect=aspect_name)
            aspect_map[aspect_name] = polarite_defaut
            self.stdout.write(self.style.SUCCESS(f"Aspect créé : {aspect_obj.nom_aspect} (polarité par défaut : {polarite_defaut})"))

        # 2) Préparer des noms uniques pour 200 médecins
        first_names = [
            "Fatima", "Amina", "Khadija", "Yasmine", "Samira", "Leila", 
            "Meriem", "Nadia", "Imane", "Sofia", "Mohamed", "Hassan", 
            "Youssef", "Karim", "Amine", "Rachid", "Reda", "Omar", "Abdel", "Salah"
        ]
        last_names = [
            "Ezzahara", "El Fassi", "Bouazza", "Benali", "Rifai", "Ziani", 
            "Mansouri", "Kabbaj", "Hamdani", "Tazi", "Benyoussef", "El Amrani", 
            "Safi", "Ouladsalah", "Ait", "Bennani", "Amrani", "Chakir", "Larbi", "Nour"
        ]
        # Produit cartésien => 20 x 20 = 400 combinaisons possibles
        unique_names = list(itertools.product(first_names, last_names))
        if len(unique_names) < 200:
            self.stdout.write("Pas assez de combinaisons uniques pour 200 médecins.")
            return
        # On mélange et on prend 200
        random.shuffle(unique_names)
        selected_names = unique_names[:200]

        # 3) Liste de spécialités
        specialties = [
            "Médecin général", "Dentiste", "Cardiologue", "Gynécologue", "Pédiatre", "Neurologue",
            "Ophtalmologiste", "Dermatologue", "Chirurgien", "Oncologue", "Orthopédiste", "Psychiatre",
            "Rhumatologue", "Endocrinologue", "Urologue", "Gastro-entérologue", "Pneumologue", 
            "Hématologue", "Néphrologue", "Infectiologue"
        ]

        # 4) Créer 200 médecins
        for i, (first_name, last_name) in enumerate(selected_names, start=1):
            specialty = random.choice(specialties)
            email = f"{first_name.lower()}.{last_name.lower()}@example.com"
            telephone = f"06{random.randint(10000000, 99999999)}"
            doctor, created = Medecin.objects.get_or_create(
                nom=last_name,
                prenom=first_name,
                defaults={
                    "specialite": specialty,
                    "email": email,
                    "telephone": telephone
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(
                    f"Médecin créé : Dr {doctor.prenom} {doctor.nom} ({doctor.specialite})"
                ))
            else:
                self.stdout.write(f"Médecin déjà existant : Dr {doctor.prenom} {doctor.nom}")

            # 5) Créer entre 1 et 3 commentaires
            num_comments = random.randint(1, 3)
            for j in range(num_comments):
                # Pour générer un commentaire plus réaliste, on prend un aspect "clé"
                chosen_aspect = random.choice(list(logical_polarities.keys()))
                comment_content = (
                    f"Commentaire {j+1} pour Dr {doctor.prenom} {doctor.nom}. "
                    f"Ce docteur est très {chosen_aspect}."
                )
                note_global = random.randint(1, 5)
                comment, _ = Commentaire.objects.get_or_create(
                    medecin=doctor,
                    contenu=comment_content,
                    defaults={"date": timezone.now(), "note_global": note_global}
                )
                self.stdout.write(self.style.SUCCESS(
                    f"Commentaire créé pour Dr {doctor.prenom} {doctor.nom}"
                ))

                # 6) Associer 1 à 2 aspects par commentaire
                #    On pioche au hasard dans la liste de 7 aspects
                num_aspects = random.randint(1, 2)
                chosen_aspects = random.sample(list(logical_polarities.keys()), num_aspects)
                for aspect_name in chosen_aspects:
                    # Polarité logique pour gentillesse => "Positif", etc.
                    # (sinon, on peut faire un random choice sur ["Positif","Negatif","Neutre"])
                    default_pol = aspect_map[aspect_name]  
                    # On va quand même rester cohérent
                    Aborder.objects.get_or_create(
                        commentaire=comment,
                        aspect=Aspect.objects.get(nom_aspect=aspect_name),
                        defaults={"polarite": default_pol}
                    )
                    self.stdout.write(self.style.SUCCESS(
                        f"Aborder créé pour Dr {doctor.prenom} {doctor.nom} : {aspect_name} ({default_pol})"
                    ))

        self.stdout.write(self.style.SUCCESS("Base peuplée avec 200 médecins et 7 aspects logiques !"))
