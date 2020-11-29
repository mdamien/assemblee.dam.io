import json, glob

from django.core.management.base import BaseCommand
from core.models import Dossier, ActeLegislatif


def yield_actes(data, dossier, parent=None):
    if type(data) is list:
        for acte in data:
            yield from yield_actes(acte, dossier, parent)
    if type(data) is dict:
        if 'acteLegislatif' in data:
            yield from yield_actes(data['acteLegislatif'], dossier, parent)
        else:
            yield ActeLegislatif(
                dossier=dossier,
                acteLegislatif=parent,
                uid=data['uid'],
                codeActe=data['codeActe'],
                libelleActe_nomCanonique=data['libelleActe']['nomCanonique'],
                libelleActe_libelleCourt=data['libelleActe'].get('libelleCourt'),
                organeRef=data.get('organeRef'),
                dateActe=data['dateActe'],
                texteAssocie=data.get('texteAssocie'),
                provenance=data.get('provenance'),
                reunion=data.get('reunion'),
                texteLoiRef=data.get('texteLoiRef'),
                infoJO_typeJO=data.get('infoJO', {}).get('typeJO'),
                infoJO_dateJO=data.get('infoJO', {}).get('dateJO'),
                infoJO_pageJO=data.get('infoJO', {}).get('pageJO'),
                infoJO_numJO=data.get('infoJO', {}).get('numJO'),
                infoJO_urlLegifrance=data.get('infoJO', {}).get('urlLegifrance'),
                infoJO_referenceNOR=data.get('infoJO', {}).get('referenceNOR'),
                urlEcheancierLoi=data.get('urlEcheancierLoi'),
                codeLoi=data.get('codeLoi'),
                titreLoi=data.get('titreLoi'),
            )
            if 'actesLegislatifs' in data:
                yield from yield_actes(data['actesLegislatifs'], dossier, parent)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('file', type=str)

    def handle(self, *args, **options):
        Dossier.objects.all().delete()
        ActeLegislatif.objects.all().delete()
        dossiers = []
        actes = []
        for json_dos in json.load(open(options['file']))['export']['dossiersLegislatifs']['dossier']:
            json_dos = json_dos['dossierParlementaire']
            dos = Dossier(
                uid=json_dos['uid'],
                legislature=json_dos['legislature'],
                titreDossier_titre=json_dos['titreDossier']['titre'],
                titreDossier_titreChemin=json_dos['titreDossier']['titreChemin'],
                titreDossier_senatChemin=json_dos['titreDossier']['senatChemin'],
                procedureParlementaire_code=json_dos['procedureParlementaire']['code'],
                procedureParlementaire_libelle=json_dos['procedureParlementaire']['libelle'],
                fusionDossier=json_dos['fusionDossier']
            )
            for acte in yield_actes(json_dos['actesLegislatifs'], dos):
                actes.append(acte)
            dossiers.append(dos)
        print("creating", len(dossiers), "dossiers")
        Dossier.objects.bulk_create(dossiers)
        print("creating", len(actes), "actes")
        ActeLegislatif.objects.bulk_create(actes)