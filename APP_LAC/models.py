import os
import django.utils.timezone
from django.db import models
from django.contrib import admin
import datetime

from django.db.models import CASCADE


#fonction pour récupérer le chemin d'enregistrement de la photo profile utilisateur

class Antenne(models.Model):
    designation = models.CharField(max_length=30, unique=True, null=False)

    def __str__(self):
        return self.designation


class Departement(models.Model):
    antenne = models.ForeignKey(Antenne, on_delete=models.CASCADE)
    designation = models.CharField(max_length=30, unique=True, null=False)

    def __str__(self):
        return self.designation


class Fonctions(models.Model):
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE, default=None)
    designation = models.CharField(max_length=30, unique=True, null=False)

    def __str__(self):
        return self.designation


class Utilisateur(models.Model):
    nom = models.CharField(default=None, max_length=50, null=False, blank=False)
    postnom = models.CharField(default=None, max_length=50, null=False, blank=False)
    prenom = models.CharField(default=None, max_length=50, null=True, blank=True)
    nom_utilisateur = models.CharField(max_length=50, null=False)
    mot_de_passe = models.CharField(max_length=50, unique=False, null=False)
    typeCompte = models.IntegerField(unique=False, null=False, blank=False, default=1)
    antenne = models.ForeignKey(Antenne, on_delete=models.CASCADE, default=None)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE, default=None)
    fonction = models.ForeignKey(Fonctions, on_delete=models.RESTRICT, default=None)
    email = models.EmailField(default=None, max_length=50, null=False, blank=False)
    tel1 = models.CharField(max_length=13, unique=False, null=False, blank=False, default=None)
    tel2 = models.CharField(max_length=13, unique=False, null=True, blank=True)
    agentFolderPht = models.CharField(max_length=100, null=True, blank=True)
    agentFolderDoc = models.CharField(max_length=100, null=True, blank=True)
    photo = models.FileField(default=None, null=True, blank=True, upload_to="photos")
    cv = models.FileField(default=None, null=True, blank=True, upload_to="CV")
    lettre = models.FileField(default=None, null=True, blank=True, upload_to="lettre")
    contrat = models.FileField(default=None, null=True, blank=True, upload_to="contrat")
    carteid = models.FileField(default=None, null=True, blank=True, upload_to="carte")
    diplome1 = models.FileField(default=None, null=True, blank=True, upload_to="dip1")
    diplome2 = models.FileField(default=None, null=True, blank=True, upload_to="dip2")
    diplome3 = models.FileField(default=None, null=True, blank=True, upload_to="dip2")

    def __str__(self):
        return "{} {} {}".format(self.nom, self.postnom, self.prenom)


class EchoBureau(models.Model):
    titre = models.CharField(default=None, null=False, blank=False, max_length=250)
    description = models.TextField(default=None, null=False, blank=False)
    photo = models.FileField(default=None, null=True, blank=True)
    video = models.FileField(default=None, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.titre


class NoteService(models.Model):
    titre = models.CharField(default=None, null=False, blank=False, max_length=250)
    message = models.TextField(default=None, null=False, blank=False)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titre


class SuiviContrat(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    dureeContrat = models.CharField(default=None, null=False, blank=False, max_length=100)
    cahierDeCharge = models.TextField(default=None, null=True, blank=True)
    salaire = models.CharField(default=None, null=False, blank=False, max_length=100)
    formationbourses = models.TextField(default=None, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.utilisateur)


class Agenda(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    date = models.DateField(default=None, null=False, blank=False)
    activitePrevue = models.TextField(default=None, null=False, blank=False)
    lieu = models.CharField(default=None, null=False, blank=False, max_length=250)
    heure = models.CharField(default=None, null=False, blank=False, max_length=10)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return "{}".format(self.utilisateur)


class Domaine(models.Model):
    domaine = models.CharField(default=None, null=False, blank=False, max_length=300)

    def __str__(self):
        return self.domaine


class Volet(models.Model):
    domaine = models.ForeignKey(Domaine, on_delete=models.CASCADE)
    volet = models.CharField(default=None, null=False, blank=False, max_length=350)

    def __str__(self):
        return self.volet


class Doc_Projet(models.Model):
    titre = models.CharField(max_length=100, blank=False)
    code_project = models.CharField(default=None, max_length=200, null=True, blank=True)
    finance_par = models.CharField(max_length=50, blank=False)
    date_debut = models.DateField(default=django.utils.timezone.now, blank=False)
    date_fin = models.DateField(default=django.utils.timezone.now, blank=False)
    duree = models.CharField(default=0, max_length=50)
    plan_action = models.CharField(max_length=100)
    programme_solicite = models.CharField(max_length=100)
    contextActualiseProgramme = models.TextField()
    descImpactAttenduProg = models.TextField()
    statut = models.CharField(default='En attente de soumission', blank=False, max_length=100)
    etat = models.CharField(default='En cours', blank=False, max_length=100)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.titre


class PartenaireProjet(models.Model):
    projet = models.ForeignKey(Doc_Projet, on_delete=models.CASCADE)
    partenaire = models.CharField(max_length=100, blank=False, null=False, default=None)


class Pays_Projet(models.Model):
    projet = models.ForeignKey(Doc_Projet,on_delete=CASCADE)
    pays = models.CharField(max_length=50,blank=False)
    def __str__(self):
        return self.pays


class Province_Projet(models.Model):
    pays = models.ForeignKey(Pays_Projet,CASCADE)
    province = models.CharField(max_length=100,blank=False)
    def __str__(self):
        return "{} - {}".format(self.province,self.pays)


class Ville_Territoire_Projet(models.Model):
    province = models.ForeignKey(Province_Projet, CASCADE)
    ville_territoire = models.CharField(max_length=100, blank=False)
    def __str__(self):
        return "{} - {}".format(self.ville_territoire, self.province)


class Axe_Projet(models.Model):
    ville_territoire = models.ForeignKey(Ville_Territoire_Projet, CASCADE)
    axe = models.CharField(max_length=100, blank=False)
    nombre_beneficiares = models.IntegerField(default=1,blank=False)


class Coordination_Nationale_Projet(models.Model):
    projet = models.ForeignKey(Doc_Projet,CASCADE)
    coordination_national = models.CharField(max_length=100,blank=False)
    def __str__(self):
        return self.coordination_national


class Coordination_Provinciale_Projet(models.Model):
    cordination_nationale = models.ForeignKey(Coordination_Nationale_Projet,CASCADE)
    coordination_provinciale = models.CharField(max_length=100,blank=False)
    def __str__(self):
        return "{} - {}".format(self.coordination_provinciale,self.cordination_nationale)


class Antenne_Projet(models.Model):
    coordination_provinciale = models.ForeignKey(Coordination_Provinciale_Projet,CASCADE)
    antenne_projet = models.CharField(max_length=100,blank=False)

    def __str__(self):
        return self.antenne_projet



class DomaineProjet(models.Model):
    projet = models.ForeignKey(Doc_Projet, on_delete=models.CASCADE)
    domaine = models.ForeignKey(Domaine, on_delete=models.RESTRICT)
    objectif_lac_de_dvpt_dans_ce_domaine = models.CharField(max_length=500, default=None)

    def __str__(self):
        return '{}'.format(self.domaine)


class VoletProjet(models.Model):
    domaine = models.ForeignKey(DomaineProjet, on_delete=models.CASCADE)
    volet = models.ForeignKey(Volet, on_delete=models.CASCADE)
    objectif_LAC = models.TextField(default=None, blank=False, null=False)
    objectif_SMART= models.TextField(default=None, blank=False, null=False)
    vue_d_ensemble = models.TextField(default=None, blank=False, null=False)
    description_des_effets = models.TextField(default=None, blank=False, null=False)
    nbre_succes = models.CharField(max_length=100, default=None, blank=False, null=False)
    enumererpersonnel = models.TextField(default=None, blank=False, null=False)

    def __str__(self):
        return '{}'.format(self.volet)


class ActivitePrincipal(models.Model):
    volet = models.ForeignKey(VoletProjet, models.CASCADE)
    activitePrincipale = models.TextField(blank=False, null=False, default=None)
    responsable_execution = models.CharField(max_length=100, blank=False, null=False)


    def __str__(self):
       return self.activitePrincipale


class Suivi_de_indicateurs_projet(models.Model):
    activite_principale = models.ForeignKey(ActivitePrincipal, on_delete=models.CASCADE)
    indicateur_lac = models.CharField(max_length=300, default=None, null=True, blank=False)
    base_line_gab = models.CharField(max_length=300, default=None, null=True, blank=False)
    cible_NA = models.CharField(max_length=300, default=None, null=True, blank=False)
    source_outils = models.CharField(max_length=300, default=None, null=True, blank=False)
    frequence_de_collecte = models.CharField(max_length=300, default=None, null=True, blank=False)
    periode_execution = models.JSONField(default=dict, null=True,blank=False)

    def __str__(self):
        return self.indicateur_lac


class Gestion_des_risques_SI(models.Model):
    volet = models.ForeignKey(VoletProjet, CASCADE)
    description = models.TextField(default=None, null=False, blank=False)
    mesure = models.TextField(default=None, null=False, blank=False)
    responsable = models.CharField(max_length=300, null=False, blank=False)


class BudgetEtPlanDecaissement(models.Model):
    activite_principale = models.ForeignKey(ActivitePrincipal, on_delete=CASCADE)
    numLigne = models.IntegerField(default=1, null=False, blank=False)
    designation = models.CharField(default=None, null=False, blank=False, max_length=100)
    specification = models.CharField(max_length=400, default=None, null=False, blank=False)
    unite = models.CharField(default=None, null=True, blank=False, max_length=100)
    quantite = models.FloatField(default=1, null=False, blank=False, max_length=10)
    frequence = models.IntegerField(default=1, blank=False,null=True)
    prixUnit = models.FloatField(default=1, null=False, blank=False, max_length=100)
    prixTot = models.FloatField(default=1, null=False, blank=False, max_length=100)
    partenaire = models.JSONField(default=dict, null=False, blank=False)
    observation = models.CharField(null=True, max_length=300)

    def __str__(self):
        return self.designation

class Sous_activite_Ap(models.Model):
    choix = (
        ('oui', 'oui'),
        ('non', 'non'),
    )
    indicateur = models.ForeignKey(Suivi_de_indicateurs_projet, on_delete=models.CASCADE ,default=None)
    sousactivite = models.CharField(max_length=500, blank=False, null=False)
    descapproche = models.CharField(max_length=500, blank=False, null=False)
    strategie_genre = models.CharField(max_length=500, default=None, blank=False, null=False)
    inclusion_pers_besoin = models.CharField(max_length=500, default=None, blank=False, null=False)
    contribution = models.CharField(max_length=500, default=None, blank=False, null=False)
    besoinenappui = models.CharField(default=None, max_length=10, choices=choix)
    outildesupervision = models.CharField(max_length=100, blank=False, null=False)
    partenairetechnique = models.CharField(max_length=100, blank=False, null=False)
    partenairetatique = models.CharField(max_length=100, blank=False, null=False)
    lieu_execution = models.CharField(max_length=100, blank=False, null=False)
    date_debut = models.DateField(default=None, blank=False, null=False)
    date_fin = models.DateField(default=None, blank=False, null=False)
    date_rapportage = models.DateField(default=None, blank=False, null=False)


class Personnel_de_mise_en_oeuvre(models.Model):
    genre = (
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    )
    volet = models.ForeignKey(VoletProjet, on_delete=models.CASCADE)
    personnel = models.CharField(max_length=300, default=None, null=False, blank=False)
    effectif = models.IntegerField(null=False, blank=False)
    nombre_jour = models.IntegerField(null=False, blank=False)
    sexe_souhaite = models.CharField(max_length=10, default=None, choices=genre)
    role_responsabilite = models.CharField(max_length=300, default=None, null=False, blank=False)
    profil_poste = models.CharField(max_length=200, default=None, null=False, blank=False)

class EtatdeBesoin_LigneBudgetaire(models.Model):
    projet = models.ForeignKey(Doc_Projet, on_delete=models.CASCADE)
    etat_de_besoin = models.CharField(max_length=100)
    ligne_budgetaire = models.CharField(max_length=100,default=0)


class BulletinInfo(models.Model):
    projet = models.ForeignKey(Doc_Projet, on_delete=models.CASCADE, default=None)
    # sous_activite = models.ForeignKey(SousActivite, on_delete=models.CASCADE)
    date_debut = models.DateField(null=False, blank=False)
    date_fin = models.DateField(null=False, blank=False)

    resultatAtteints = models.CharField(default=None, null=True, blank=True,max_length=500)
    lieuxExecution = models.CharField(default=None, null=False, blank=False, max_length=150)
    statut = models.CharField(default=None, null=False, blank=False, max_length=100)
    justification = models.CharField(default=None, null=True, blank=True,max_length=500)
    mesuresCorrectives = models.CharField(default=None, null=True, blank=True,max_length=300)
    leconAprise = models.CharField(default=None, null=True, blank=True,max_length=300)
    def __str__(self):
        return self.sous_activite.sousactivite

class PhotoRealisation_Sitrep(models.Model):
    bulletin_info = models.ForeignKey(BulletinInfo,on_delete=models.CASCADE)
    photoRealisation = models.ImageField(null=False,blank=False,upload_to='sitrep')


class Mapping_Projet(models.Model):
    projet = models.ForeignKey(Doc_Projet,on_delete=CASCADE)
    personnel = models.CharField(max_length=50,blank=False)
    grade_agent = models.CharField(max_length=50,blank=False)
    effectif_recherche = models.IntegerField(default=1,blank=False)
    affectation = models.CharField(max_length=50, blank=False)
    nombre_de_jours = models.IntegerField(default=0, blank=False)
    reponsables_h = models.CharField(max_length=50, blank=False)
    personnel_supervise = models.CharField(max_length=50, blank=False)
    responsable_cle = models.CharField(max_length=50, blank=False)
    description_taches = models.CharField(max_length=50, blank=False)
    profil_de_ce_poste = models.CharField(max_length=50, blank=False)

    type_de_recrutement = models.CharField(max_length=50, blank=False)
    debut_recrutement = models.DateField(default=None, blank=False)
    fin_recrutement = models.DateField(default=None, blank=False)

    type_contrat = models.CharField(max_length=50, blank=False)
    nature_contrat = models.CharField(max_length=50, blank=False)
    id_agent = models.CharField(max_length=50, blank=False)
    date_debut_contrat = models.DateField(default=None, null=50, blank=False)
    date_de_fin_contrat = models.DateField(default=None, max_length=50, blank=False)
    date_de_fin_essai = models.DateField(default=None, max_length=50, blank=False,null=True)

    date_premiere_evaluation = models.DateField(default=None, blank=False)
    total_salaire = models.FloatField(default=0.0,blank=False)
    ligne_budgetaire = models.CharField(max_length=50, blank=False)
    impot_DGI = models.FloatField(default=0.0,blank=False)
    retune_CNSS = models.FloatField(default=0.0,blank=False)
    retune_NPP = models.FloatField(default=0.0,blank=False)
    retune_CaisseSociale = models.FloatField(default=0.0,blank=False)
    net_a_payer = models.FloatField(default=0.0,blank=False)
    equipement = models.CharField(default="...",blank=False,max_length=500)


admin.site.register(Utilisateur)
admin.site.register(Departement)
admin.site.register(Antenne)
admin.site.register(Fonctions)
admin.site.register(EchoBureau)
admin.site.register(NoteService)
admin.site.register(BulletinInfo)
admin.site.register(SuiviContrat)
admin.site.register(Agenda)
admin.site.register(Domaine)
admin.site.register(Volet)
admin.site.register(Suivi_de_indicateurs_projet)
admin.site.register(Gestion_des_risques_SI)

admin.site.register(Doc_Projet)
admin.site.register(DomaineProjet)
admin.site.register(VoletProjet)
admin.site.register(ActivitePrincipal)
admin.site.register(Sous_activite_Ap)
admin.site.register(BudgetEtPlanDecaissement)
admin.site.register(Personnel_de_mise_en_oeuvre)
admin.site.register(EtatdeBesoin_LigneBudgetaire)
admin.site.register(Pays_Projet)
admin.site.register(Province_Projet)
admin.site.register(Ville_Territoire_Projet)
admin.site.register(Axe_Projet)
admin.site.register(Antenne_Projet)
admin.site.register(Coordination_Provinciale_Projet)
admin.site.register(Coordination_Nationale_Projet)