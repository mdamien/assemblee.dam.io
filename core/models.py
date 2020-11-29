from django.db import models


class Organe(models.Model):
    xsi_type = models.TextField()
    uid = models.TextField(primary_key=True)
    codeType = models.TextField()
    libelle = models.TextField()
    libelleEdition = models.TextField(null=True)
    libelleAbrege = models.TextField()
    libelleAbrev = models.TextField()
    viMoDe_dateDebut = models.TextField(null=True)
    viMoDe_dateAgrement = models.TextField(null=True)
    viMoDe_dateFin = models.TextField(null=True)
    organeParent = models.TextField(null=True) # todo: Organe ?
    chambre = models.TextField(null=True)
    regime = models.TextField(null=True)
    legislature = models.TextField(null=True)
    secretariat_secretaire01 = models.TextField(null=True) # todo: acteurs ?
    secretariat_secretaire02 = models.TextField(null=True)


class Acteur(models.Model):
    uid = models.TextField(primary_key=True)
    etatCivil_ident_civ = models.TextField()
    etatCivil_ident_prenom = models.TextField()
    etatCivil_ident_nom = models.TextField()
    etatCivil_ident_alpha = models.TextField()
    etatCivil_ident_trigramme = models.TextField(null=True)
    etatCivil_infoNaissance_dateNais = models.TextField()
    etatCivil_infoNaissance_villeNais = models.TextField()
    etatCivil_infoNaissance_depNais = models.TextField()
    etatCivil_infoNaissance_paysNais = models.TextField()
    etatCivil_dateDeces = models.TextField(null=True)
    profession_libelleCourant = models.TextField()
    profession_socProcINSEE_catSocPro = models.TextField()
    profession_socProcINSEE_famSocPro = models.TextField()
    uri_hatvp = models.TextField(null=True)


class Adresse(models.Model):
    acteur = models.ForeignKey(Acteur, on_delete=models.CASCADE)
    xsi_type = models.TextField()
    uid = models.TextField(primary_key=True)
    type = models.TextField()
    typeLibelle = models.TextField()
    poids = models.TextField(null=True)
    adresseDeRattachement = models.TextField(null=True)
    valElec = models.TextField(null=True)
    intitule = models.TextField(null=True)
    numeroRue = models.TextField(null=True)
    nomRue = models.TextField(null=True)
    complementAdresse = models.TextField(null=True)
    codePostal = models.TextField(null=True)
    ville = models.TextField(null=True)


class Mandat(models.Model):
    acteur = models.ForeignKey(Acteur, on_delete=models.CASCADE)
    uid = models.TextField(primary_key=True)
    acteurRef = models.TextField()
    legislature = models.TextField(null=True)
    typeOrgane = models.TextField()
    dateDebut = models.TextField()
    datePublication = models.TextField(null=True)
    dateFin = models.TextField(null=True)
    preseance = models.TextField(null=True)
    nominPrincipale = models.TextField()
    infosQualite_codeQualite = models.TextField(null=True)
    infosQualite_libQualite = models.TextField()
    infosQualite_libQualiteSex = models.TextField(null=True)
    # todo organes
    # todo suppleants


class Dossier(models.Model):
    uid = models.TextField(primary_key=True)
    legislature = models.TextField()
    titreDossier_titre = models.TextField()
    titreDossier_titreChemin = models.TextField(null=True)
    titreDossier_senatChemin = models.TextField(null=True)
    procedureParlementaire_code = models.TextField()
    procedureParlementaire_libelle = models.TextField()
    # todo: initiateur
    fusionDossier = models.TextField(null=True)
    # todo: check extra fields


class ActeLegislatif(models.Model):
    dossier = models.ForeignKey(Dossier, on_delete=models.CASCADE)
    acteLegislatif = models.ForeignKey('ActeLegislatif', null=True, on_delete=models.CASCADE)
    uid = models.TextField()
    codeActe = models.TextField()
    libelleActe_nomCanonique = models.TextField()
    libelleActe_libelleCourt = models.TextField(null=True)
    organeRef = models.TextField(null=True) # todo: foreign key
    dateActe = models.TextField(null=True)
    texteAssocie = models.TextField(null=True)
    provenance = models.TextField(null=True)
    # todo: rapporteurs
    reunion = models.TextField(null=True)
    texteLoiRef = models.TextField(null=True)
    infoJO_typeJO = models.TextField(null=True)
    infoJO_dateJO = models.TextField(null=True)
    infoJO_pageJO = models.TextField(null=True)
    infoJO_numJO = models.TextField(null=True)
    infoJO_urlLegifrance = models.TextField(null=True)
    infoJO_referenceNOR = models.TextField(null=True)
    urlEcheancierLoi = models.TextField(null=True)
    codeLoi = models.TextField(null=True)
    titreLoi = models.TextField(null=True)
    # todo: check extra fields


class Document(models.Model):
    xsi_type = models.TextField()
    uid = models.TextField(primary_key=True)
    legislature = models.TextField(null=True)
    cycleDeVie_chrono_dateCreation = models.TextField()
    cycleDeVie_chrono_dateDepot = models.TextField(null=True)
    cycleDeVie_chrono_datePublication = models.TextField(null=True)
    cycleDeVie_chrono_datePublicationWeb = models.TextField(null=True)
    denominationStructurelle = models.TextField()
    provenance = models.TextField(null=True)
    titres_titrePrincipal = models.TextField()
    titres_titrePrincipalCourt = models.TextField()
    # todo: divisions
    dossierRef = models.TextField() # todo: foreign key
    # todo: redacteur
    classification_famille_depot_code = models.TextField()
    classification_famille_depot_libelle = models.TextField()
    classification_famille_classe_code = models.TextField()
    classification_famille_classe_libelle = models.TextField()
    classification_famille_espece_code = models.TextField(null=True)
    classification_famille_espece_libelle = models.TextField(null=True)
    classification_type_code = models.TextField()
    classification_type_libelle = models.TextField()
    classification_sousType_code = models.TextField(null=True)
    classification_sousType_libelle = models.TextField(null=True)
    classification_sousType_libelleEdition = models.TextField(null=True)
    classification_statutAdoption = models.TextField(null=True)
    # todo: auteurs
    correction = models.TextField(null=True)
    notice_numNotice = models.TextField(null=True)
    notice_formule = models.TextField(null=True)
    notice_adoptionConforme = models.TextField()
    indexation = models.TextField(null=True)
    imprimerie_ISSN = models.TextField(null=True)
    imprimerie_ISBN = models.TextField(null=True)
    imprimerie_DIAN = models.TextField(null=True)
    imprimerie_nbPage = models.TextField(null=True)
    imprimerie_prix = models.TextField(null=True)
    # todo: check extra fields