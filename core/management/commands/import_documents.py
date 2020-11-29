import json, glob

from django.core.management.base import BaseCommand
from core.models import Document


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('files', type=str)

    def handle(self, *args, **options):
        Document.objects.all().delete()
        documents = []
        for file in glob.glob(options["files"]):
            json_dos = json.load(open(file))['document']

            doc = Document(
                xsi_type=json_dos['@xsi:type'],
                uid=json_dos['uid'],
                legislature=json_dos.get('legislature'),
                cycleDeVie_chrono_dateCreation=json_dos['cycleDeVie']['chrono']['dateCreation'],
                cycleDeVie_chrono_dateDepot=json_dos['cycleDeVie']['chrono']['dateDepot'],
                cycleDeVie_chrono_datePublication=json_dos['cycleDeVie']['chrono']['datePublication'],
                cycleDeVie_chrono_datePublicationWeb=json_dos['cycleDeVie']['chrono']['datePublicationWeb'],
                denominationStructurelle=json_dos['denominationStructurelle'],
                provenance=json_dos.get('provenance'),
                titres_titrePrincipal=json_dos['titres']['titrePrincipal'],
                titres_titrePrincipalCourt=json_dos['titres']['titrePrincipalCourt'],
                dossierRef=json_dos['dossierRef'],
                classification_famille_depot_code=json_dos['classification']['famille']['depot']['code'],
                classification_famille_depot_libelle=json_dos['classification']['famille']['depot']['libelle'],
                classification_famille_classe_code=json_dos['classification']['famille']['classe']['code'],
                classification_famille_classe_libelle=json_dos['classification']['famille']['classe']['libelle'],
                classification_famille_espece_code=json_dos['classification']['famille'].get('espece', {}).get('code'),
                classification_famille_espece_libelle=json_dos['classification']['famille'].get('espece', {}).get('libelle'),
                classification_type_code=json_dos['classification']['type']['code'],
                classification_type_libelle=json_dos['classification']['type']['libelle'],
                classification_sousType_code=json_dos['classification']['sousType']['code'] if json_dos['classification']['sousType'] else None,
                classification_sousType_libelle=json_dos['classification']['sousType'].get('libelle') if json_dos['classification']['sousType'] else None,
                classification_sousType_libelleEdition=json_dos['classification']['sousType'].get('libelleEdition') if json_dos['classification']['sousType'] else None,
                classification_statutAdoption=json_dos['classification']['statutAdoption'],
                correction=json_dos['correction'],
                notice_numNotice=json_dos['notice'].get('numNotice'),
                notice_formule=json_dos['notice'].get('formule'),
                notice_adoptionConforme=json_dos['notice']['adoptionConforme'],
                indexation=json_dos['indexation'],
                imprimerie_ISSN=json_dos['imprimerie'].get('ISSN') if json_dos['imprimerie']  else None,
                imprimerie_ISBN=json_dos['imprimerie'].get('ISBN') if json_dos['imprimerie']  else None,
                imprimerie_DIAN=json_dos['imprimerie'].get('DIAN') if json_dos['imprimerie']  else None,
                imprimerie_nbPage=json_dos['imprimerie'].get('nbPage') if json_dos['imprimerie'] else None,
                imprimerie_prix=json_dos['imprimerie']['prix'] if json_dos['imprimerie'] else None,
            )
            documents.append(doc)
        print("creating", len(documents), "documents")
        Document.objects.bulk_create(documents)