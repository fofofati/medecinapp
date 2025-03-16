import unicodedata
from .models import Aspect, Aborder

def normalize_text(text):
    """
    Supprime les accents et convertit le texte en minuscules.
    """
    text = str(text)  # S'assurer que c'est bien une chaîne
    normalized = unicodedata.normalize('NFKD', text)
    return ''.join(c for c in normalized if not unicodedata.combining(c)).lower()


ASPECTS_KEYWORDS = {
    # gentillesse
    'gentil': ('gentillesse', 'Positif'),
    'gentille': ('gentillesse', 'Positif'),
    'aimable': ('gentillesse', 'Positif'),
    'impoli': ('gentillesse', 'Negatif'),
    'grossier': ('gentillesse', 'Negatif'),
    # ponctualité
    'ponctuel': ('ponctualité', 'Positif'),
    'à l heure': ('ponctualité', 'Positif'),
    'retard': ('ponctualité', 'Negatif'),
    'en retard': ('ponctualité', 'Negatif'),
    # compétence
    'compétent': ('compétence', 'Positif'),
    'doué': ('compétence', 'Positif'),
    'incompétent': ('compétence', 'Negatif'),
    'mauvais diagnostic': ('compétence', 'Negatif'),
    # écoute
    'écoute': ('écoute', 'Positif'),
    'à l écoute': ('écoute', 'Positif'),
    'attentif': ('écoute', 'Positif'),
    'pas attentif': ('écoute', 'Negatif'),
    'pas à l écoute': ('écoute', 'Negatif'),
    'désintéressé': ('écoute', 'Negatif'),
    # empathie
    'empathique': ('empathie', 'Positif'),
    'compatissant': ('empathie', 'Positif'),
    'compassion': ('empathie', 'Positif'),
    'froid': ('empathie', 'Negatif'),
    'distant': ('empathie', 'Negatif'),
    'apathique': ('empathie', 'Negatif'),
    # matérialité
    'matérialiste': ('matérialité', 'Negatif'),
    'vénal': ('matérialité', 'Negatif'),
    'avide': ('matérialité', 'Negatif'),
    'un peu matérialiste': ('matérialité', 'Negatif'),
    # accueil
    'accueil chaleureux': ('accueil', 'Positif'),
    'accueil froid': ('accueil', 'Negatif'),
    'bien accueilli': ('accueil', 'Positif'),
    # professionnalisme
    'professionnel': ('professionnalisme', 'Positif'),
    'non professionnel': ('professionnalisme', 'Negatif'),
    'peu professionnel': ('professionnalisme', 'Negatif'),
    # rigueur
    'consciencieux': ('rigueur', 'Positif'),
    'bâclé': ('rigueur', 'Negatif'),
    'rigoureux': ('rigueur', 'Positif'),
    # explications
    'expliqué clairement': ('explications', 'Positif'),
    'pas d explication': ('explications', 'Negatif'),
    'pas clair': ('explications', 'Negatif'),
    # amabilité
    'amabilité': ('amabilité', 'Positif'),
    'souriant': ('amabilité', 'Positif'),
    'renfrogné': ('amabilité', 'Negatif'),
    # confiance
    'rassurant': ('confiance', 'Positif'),
    'confiance': ('confiance', 'Positif'),
    'anxieux': ('confiance', 'Negatif'),
    'doute': ('confiance', 'Negatif'),
    # coût / tarif
    'pas cher': ('coût', 'Positif'),
    'cher': ('coût', 'Negatif'),
    'abordable': ('coût', 'Positif'),
    'excessif': ('coût', 'Negatif'),
    'honoraires élevés': ('coût', 'Negatif'),
    'honoraires corrects': ('coût', 'Positif'),
    # hygiène
    'hygiène impeccable': ('hygiène', 'Positif'),
    'hygiène douteuse': ('hygiène', 'Negatif'),
    'sale': ('hygiène', 'Negatif'),
    'propre': ('hygiène', 'Positif'),
    # douceur
    'doux': ('douceur', 'Positif'),
    'brusque': ('douceur', 'Negatif'),
    'violent': ('douceur', 'Negatif'),
    # approche
    'approche globale': ('approche', 'Positif'),
    'superficiel': ('approche', 'Negatif'),
    'approche personnalisée': ('approche', 'Positif'),
    # tempérament
    'calme': ('tempérament', 'Positif'),
    'agressif': ('tempérament', 'Negatif'),
    'énervé': ('tempérament', 'Negatif'),
    # respect
    'respectueux': ('respect', 'Positif'),
    'irrespectueux': ('respect', 'Negatif'),
    # patience
    'patient': ('patience', 'Positif'),
    'impatient': ('patience', 'Negatif'),
    # bienveillance
    'bienveillant': ('bienveillance', 'Positif'),
    'malveillant': ('bienveillance', 'Negatif'),
    # discrétion
    'discret': ('discrétion', 'Positif'),
    'indiscret': ('discrétion', 'Negatif'),
    # propreté
    'propre': ('propreté', 'Positif'),
    'sale': ('propreté', 'Negatif'),
    # recommandation
    'à recommander': ('recommandation', 'Positif'),
    'pas recommandable': ('recommandation', 'Negatif'),
    # examen
    'examen complet': ('examen', 'Positif'),
    'examen partiel': ('examen', 'Negatif'),
    # courtoisie
    'courtois': ('courtoisie', 'Positif'),
    'rude': ('courtoisie', 'Negatif'),
    # organisation
    'organisé': ('organisation', 'Positif'),
    'désorganisé': ('organisation', 'Negatif'),
    # flexibilité
    'calendrier flexible': ('flexibilité', 'Positif'),
    'calendrier rigide': ('flexibilité', 'Negatif'),
    # attente
    'attente courte': ('attente', 'Positif'),
    'attente longue': ('attente', 'Negatif'),
    # délai rdv
    'disponible rapidement': ('délai rdv', 'Positif'),
    'trop long': ('délai rdv', 'Negatif'),
    # équipement
    'bien équipé': ('équipement', 'Positif'),
    'pas équipé': ('équipement', 'Negatif'),
    # expérience
    'expérimenté': ('expérience', 'Positif'),
    # accessibilité
    'accès facile': ('accessibilité', 'Positif'),
    'accès difficile': ('accessibilité', 'Negatif'),
    # suivi
    'suit correctement': ('suivi', 'Positif'),
    'pas de suivi': ('suivi', 'Negatif'),
    # diagnostic
    'diagnostic sûr': ('diagnostic', 'Positif'),
    'diagnostic douteux': ('diagnostic', 'Negatif'),
    'mauvais diagnostic': ('diagnostic', 'Negatif'),
}

def detect_aspects_and_create_aborder(commentaire):
    """
    Parcourt le texte normalisé du commentaire, détecte des mots-clés,
    et crée un enregistrement Aborder pour chaque aspect détecté, avec sa polarité.
    """
    # Normalisation du contenu
    contenu_lower = normalize_text(commentaire.contenu)
    print("Contenu normalisé :", contenu_lower)
    
    aspects_detectes = set()
    for keyword, (aspect_name, polarite) in ASPECTS_KEYWORDS.items():
        # Normaliser le mot-clé pour assurer la correspondance
        normalized_keyword = normalize_text(keyword)
        if normalized_keyword in contenu_lower:
            print(f"Détection : '{keyword}' (normalisé: '{normalized_keyword}') -> {aspect_name} ({polarite})")
            aspects_detectes.add((aspect_name, polarite))
    
    for aspect_name, polarite in aspects_detectes:
        aspect_obj, _ = Aspect.objects.get_or_create(nom_aspect=aspect_name)
        already_exists = Aborder.objects.filter(
            commentaire=commentaire,
            aspect=aspect_obj,
            polarite=polarite
        ).exists()
        if not already_exists:
            Aborder.objects.create(
                commentaire=commentaire,
                aspect=aspect_obj,
                polarite=polarite
            )
            print(f"Création de Aborder : {aspect_name} avec polarité {polarite}")
