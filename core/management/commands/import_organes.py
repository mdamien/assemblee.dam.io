import json, glob

from django.core.management.base import BaseCommand
from core.models import Organe


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('files', type=str)

    def handle(self, *args, **options):
        Organe.objects.all().delete()
        organes = []
        for file in glob.glob(options["files"]):
            data = json.load(open(file))['organe']

            organe = Organe(
                uid=data['uid'],
                xsi_type=data['@xsi:type'],
                codeType=data['codeType'],
                libelle=data['libelle'],
                libelleEdition=data['libelleEdition'],
                libelleAbrege=data['libelleAbrege'],
                libelleAbrev=data['libelleAbrev'],
                viMoDe_dateDebut=data['viMoDe']['dateDebut'],
                viMoDe_dateAgrement=data['viMoDe']['dateAgrement'],
                viMoDe_dateFin=data['viMoDe']['dateFin'],
                organeParent=data['organeParent'],
                chambre=data.get('chambre'),
                regime=data.get('regime'),
                secretariat_secretaire01=data['secretariat']['secretaire01'] if 'secretariat' in data else None,
                secretariat_secretaire02=data['secretariat']['secretaire02'] if 'secretariat' in data else None,
            )
            organes.append(organe)

        print("creating", len(organes), "organes")
        Organe.objects.bulk_create(organes)