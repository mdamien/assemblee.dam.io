import json, glob

from django.core.management.base import BaseCommand
from core.models import Acteur, Adresse, Mandat


def nil2none(obj):
    if type(obj) is dict and obj['@xsi:nil'] == 'true':
        return None
    return obj

def to_list(obj):
    if type(obj) is not list:
        return [obj]
    return obj


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('files', type=str)

    def handle(self, *args, **options):
        Acteur.objects.all().delete()
        acteurs = []
        adresses = []
        mandats = []
        for file in glob.glob(options["files"]):
            json_dos = json.load(open(file))['acteur']

            acteur = Acteur(
                uid=json_dos['uid']['#text'],
                etatCivil_ident_civ=json_dos['etatCivil']['ident']['civ'],
                etatCivil_ident_prenom=json_dos['etatCivil']['ident']['prenom'],
                etatCivil_ident_nom=json_dos['etatCivil']['ident']['nom'],
                etatCivil_ident_alpha=json_dos['etatCivil']['ident']['alpha'],
                etatCivil_ident_trigramme=nil2none(json_dos['etatCivil']['ident']['trigramme']),
                etatCivil_infoNaissance_dateNais=json_dos['etatCivil']['infoNaissance']['dateNais'],
                etatCivil_infoNaissance_villeNais=json_dos['etatCivil']['infoNaissance']['villeNais'],
                etatCivil_infoNaissance_depNais=json_dos['etatCivil']['infoNaissance']['depNais'],
                etatCivil_infoNaissance_paysNais=json_dos['etatCivil']['infoNaissance']['paysNais'],
                etatCivil_dateDeces=nil2none(json_dos['etatCivil']['dateDeces']),
                profession_libelleCourant=json_dos['profession']['libelleCourant'],
                profession_socProcINSEE_catSocPro=json_dos['profession']['socProcINSEE']['catSocPro'],
                profession_socProcINSEE_famSocPro=json_dos['profession']['socProcINSEE']['famSocPro'],
                uri_hatvp=nil2none(json_dos['uri_hatvp'])
            )
            acteurs.append(acteur)

            for adresse in to_list(json_dos['adresses']['adresse']):
                adresses.append(Adresse(
                    acteur=acteur,
                    xsi_type=adresse['@xsi:type'],
                    uid=adresse['uid'],
                    type=adresse['type'],
                    typeLibelle=adresse['typeLibelle'],
                    poids=adresse['poids'],
                    adresseDeRattachement=adresse['adresseDeRattachement'],
                    valElec=adresse.get('valElec'),
                    intitule=adresse.get('intitule'),
                    numeroRue=adresse.get('numeroRue'),
                    nomRue=adresse.get('nomRue'),
                    complementAdresse=adresse.get('complementAdresse'),
                    codePostal=adresse.get('codePostal'),
                    ville=adresse.get('ville')
                    ))

            for mandat in to_list(json_dos['mandats']['mandat']):
                mandats.append(Mandat(
                    acteur=acteur,
                    uid=mandat['uid'],
                    acteurRef=mandat['acteurRef'],
                    legislature=mandat['legislature'],
                    typeOrgane=mandat['typeOrgane'],
                    dateDebut=mandat['dateDebut'],
                    datePublication=mandat['datePublication'],
                    dateFin=mandat['dateFin'],
                    preseance=mandat['preseance'],
                    nominPrincipale=mandat['nominPrincipale'],
                    infosQualite_codeQualite=mandat['infosQualite']['codeQualite'],
                    infosQualite_libQualite=mandat['infosQualite']['libQualite'],
                    infosQualite_libQualiteSex=mandat['infosQualite']['libQualiteSex'],
                ))
        print("creating", len(acteurs), "acteurs")
        Acteur.objects.bulk_create(acteurs)
        print("creating", len(adresses), "adresses")
        Adresse.objects.bulk_create(adresses)
        print("creating", len(mandats), "mandats")
        Mandat.objects.bulk_create(mandats)