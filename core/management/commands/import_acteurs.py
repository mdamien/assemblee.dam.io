import json, glob

from django.core.management.base import BaseCommand
from core.models import Acteur


def nil2none(obj):
    if type(obj) is dict and obj['@xsi:nil'] == 'true':
        return None


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('files', type=str)

    def handle(self, *args, **options):
        Acteur.objects.all().delete()
        acteurs = []
        for file in glob.glob(options["files"]):
            json_dos = json.load(open(file))['acteur']

            acteur = Acteur(
                uid=json_dos['uid'],
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
        print("creating", len(acteurs), "acteurs")
        Acteur.objects.bulk_create(acteurs)