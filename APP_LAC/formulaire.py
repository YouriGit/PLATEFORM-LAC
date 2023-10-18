import datetime

from django import forms
from APP_LAC import models
from django.forms import widgets
import pycountry

class Connexion(forms.ModelForm):
    class Meta:
        model = models.Utilisateur
        fields = ['nom_utilisateur', 'mot_de_passe']

        labels = {
            'nom_utilisateur': "Nom d'utilisateur",
            'mot_de_passe': 'Mot de passe',
        }

        widgets = {
            'nom_utilisateur': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Nom d'utilisateur"}),
            'mot_de_passe': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Mot de passe"}),
        }

#formulaire pour créer un nouvel agent par l'administrateur
class Ajout_agent(forms.ModelForm):
    class Meta:
        model = models.Utilisateur
        fields = ['nom', 'postnom', 'prenom', 'nom_utilisateur', 'mot_de_passe', 'antenne',
                  'departement', 'fonction', 'email', 'tel1', 'tel2', 'photo', 'cv', 'lettre',
                  'contrat', 'carteid', 'diplome1', 'diplome2', 'diplome3']
        labels = {
            'nom': '',
            'postnom': '',
            'prenom': '',
            'nom_utilisateur': '',
            'mot_de_passe': '',
            'email': '',
            'tel1': '',
            'tel2': '',
            'photo': 'Ajouter une photo',
        }
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Nom de l'agent"}),
            'postnom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Postnom de l'agent"}),
            'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Prénom de l'agent"}),
            'nom_utilisateur': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Nom d'utilisateur"}),
            #'mot_de_passe': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Mot de passe"}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "exemple@gmail.com"}),
            'tel1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Numéro de téléphone"}),
            'tel2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Un autre numéro"}),
        }

#formulaire de modification du profile de l'agent dans un compte administrateur
class Profile_agent(forms.ModelForm):
    class Meta:
        model = models.Utilisateur
        fields = ['nom', 'postnom', 'prenom', 'nom_utilisateur', 'mot_de_passe', 'antenne',
                  'departement', 'fonction', 'email', 'tel1', 'tel2', 'photo', 'cv', 'lettre',
                  'contrat', 'carteid', 'diplome1', 'diplome2', 'diplome3']
        labels = {
            'nom': "Nom de l'agent",
            'postnom': "Postnom de l'agent",
            'prenom': "Prénom de l'agent",
            'nom_utilisateur': "Nom d'utilisateur",
            'mot_de_passe': "Mot de passe",
            'email': "Email",
            'tel1': "Téléphone 1",
            'tel2': 'Téléphone 2',
            'photo': 'Ajouter une photo',
            'cv': 'Ajouter un CV',
            'lettre': 'Ajouter une lettre',
            'contrat': 'Ajouter un contrat',
            'Carteid': "Ajouter une carte d'identité",
            'diplome1': 'Ajouter un diplôme',
            'diplome2': 'Ajouter un autre diplôme',
            'diplome3': 'Ajouter un autre diplôme',
        }
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Nom de l'agent"}),
            'postnom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Postnom de l'agent"}),
            'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Prénom de l'agent"}),
            'nom_utilisateur': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Nom d'utilisateur"}),
            #'mot_de_passe': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Mot de passe"}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "exemple@gmail.com"}),
            'tel1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Numéro de téléphone"}),
            'tel2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Un autre numéro"}),
        }

#formulaire de modification des informations de l'utilisateur courant
class Mon_profil_agent(forms.ModelForm):
    class Meta:
        model = models.Utilisateur
        fields = ['nom', 'postnom', 'prenom', 'nom_utilisateur', 'mot_de_passe',
                  'email', 'tel1', 'tel2', 'photo', 'cv', 'lettre',
                  'contrat', 'carteid', 'diplome1', 'diplome2', 'diplome3']
        labels = {
            'nom': "Nom de l'agent",
            'postnom': "Postnom de l'agent",
            'prenom': "Prénom de l'agent",
            'nom_utilisateur': "Nom d'utilisateur",
            'mot_de_passe': "Mot de passe",
            'email': "Email",
            'tel1': "Téléphone 1",
            'tel2': 'Téléphone 2',
            'photo': 'Ajouter une photo',
            'cv': 'Ajouter un CV',
            'lettre': 'Ajouter une lettre',
            'contrat': 'Ajouter un contrat',
            'Carteid': "Ajouter une carte d'identité",
            'diplome1': 'Ajouter un diplôme',
            'diplome2': 'Ajouter un autre diplôme',
            'diplome3': 'Ajouter un autre diplôme',
        }
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Nom de l'agent"}),
            'postnom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Postnom de l'agent"}),
            'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Prénom de l'agent"}),
            'nom_utilisateur': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Nom d'utilisateur"}),
            #'mot_de_passe': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "exemple@gmail.com"}),
            'tel1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Numéro de téléphone"}),
            'tel2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Un autre numéro"}),
        }

#un formulaire de test


# class Test(forms.ModelForm):
#     class Meta:
#         model = models.tester
#         fields = ['nom']


class Doc_Projet(forms.ModelForm):
   class Meta:
       model = models.Doc_Projet
       fields = '__all__'

       labels = {
           "titre": "",
           "code_project": "",
           "finance_par": "",
           "date_debut": "",
           "date_fin": "",
           "duree": "",
           "plan_action": "",
           "programme_solicite": "",
           "contextActualiseProgramme": "",
           "descImpactAttenduProg": "",
       }
       widgets = {
           "titre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Titre du programme"}),
            "code_project": forms.TextInput(attrs={"class": "form-control", "placeholder": "Code du programme"}),
            "finance_par": forms.TextInput(attrs={"class": "form-control", "placeholder": "Fincancé par"}),
            "date_debut": forms.DateInput(attrs={'type': 'date', 'format': '%d/%m/%Y'}),
            "date_fin": forms.DateInput(attrs={'type': 'date', 'format': '%d/%m/%Y'}),
            "plan_action": forms.TextInput(attrs={"class": "form-control", "placeholder": "Plan d'action opérationnel"}),
            "programme_solicite": forms.TextInput(attrs={"class": "form-control", "placeholder": "Programme sollicité"}),
            "contextActualiseProgramme": forms.TextInput(attrs={"class": "form-control", "placeholder": "Contexte actualisé du programme"}),
            "descImpactAttenduProg": forms.TextInput(attrs={"class": "form-control", "placeholder": "Déscription de l'impact attendu du programme"}),
       }


class NoteService(forms.ModelForm):
    class Meta:
        model = models.NoteService
        fields = '__all__'
        labels = {
            'titre': 'Objet de la note',
            'message': 'Description de la note',
        }


class EchoBureau(forms.ModelForm):
    class Meta:
        model = models.EchoBureau
        fields = '__all__'


class Agenda(forms.ModelForm):
    class Meta:
        model = models.Agenda
        fields = ['date', 'activitePrevue', 'lieu', 'heure']
        widgets = {
            'date': widgets.SelectDateWidget(),
            'heure': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "00:00:00"})
        }


class SuiviDeContrat(forms.ModelForm):
    class Meta:
        model = models.SuiviContrat
        fields = ['dureeContrat', 'cahierDeCharge', 'salaire', 'formationbourses']



# class BulletinInfo(forms.ModelForm):
#     class Meta:
#         model = models.BulletinInfo
#         fields = ['projet', 'periode', 'activitePrevues', 'resultatAtteints', 'lieuxExecution',
#                   'photoRealisation', 'statut', 'justification', 'mesuresCorrectives']
#

class DomaineProjetEdit(forms.ModelForm):
    class Meta:
        model = models.DomaineProjet
        fields = ['objectif_lac_de_dvpt_dans_ce_domaine']
        labels = {'objectif_lac_de_dvpt_dans_ce_domaine': 'Objectif LAC de développement dans ce volet'}
        widgets = {
            "objectif_lac_de_dvpt_dans_ce_domaine": forms.TextInput(attrs={"class": "form-control"}),
        }


class DomaineProjet(forms.ModelForm):
    class Meta:
        model = models.DomaineProjet
        fields = ['domaine']
        labels = {'domaine': '',}
        widgets = {
            "domaine": forms.Select(attrs={"class": "form-control"})
        }


class PartenaireProjet(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        key = kwargs.pop('key', None)
        super(PartenaireProjet, self).__init__(*args, **kwargs)
        if key:
            pjt = []
            projet = models.Doc_Projet.objects.get(id=key)
            pjt.append((projet.id, projet))
            self.fields['projet'].choices = pjt
    class Meta:
        model =models.PartenaireProjet
        fields = '__all__'
        labels = {
            "projet": "",
            "partenaire": "",
        }
        widgets = {
            'partenaire': forms.TextInput(attrs={'class': 'form-control',
                                                   'placeholder': "Partenaire d'exécution"}),
        }



class Pays_Projet(forms.ModelForm):
    class Meta:
        model = models.Pays_Projet
        fields = ['pays']
        labels = {
            'pays': ""
        }
        widgets = {
            'pays': forms.Select(attrs={"class": "form-select"}, choices=[(country.alpha_2, country.name) for country in pycountry.countries]),
        }

class Province_Projet(forms.ModelForm):
    def initialisation(self,context):
        projet = models.Doc_Projet.objects.get(id=context)
        pays = models.Pays_Projet.objects.filter(projet=projet)
        liste_pays = []
        for data in pays:
            liste_pays.append((data.id,data))
        liste_pays.reverse()
        self.fields['pays'].choices = liste_pays
    class Meta:
        model = models.Province_Projet
        fields = "__all__"
        labels = {
            'province': "",
        }
        widgets = {
            'province': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Entrez la province"}),
            'pays': forms.Select(attrs={'class': 'form-select'})
        }

class VilleTerritoir_Projet(forms.ModelForm):
    def initialisation(self,context):
        projet = models.Doc_Projet.objects.get(id=context)
        provinces = models.Province_Projet.objects.all()
        list_province = []
        for data in provinces:
            if data.pays.projet == projet:
                list_province.append((data.id, data))
        list_province.reverse()
        self.fields['province'].choices = list_province
    class Meta:
        model = models.Ville_Territoire_Projet
        fields = "__all__"
        widgets = {
            "province": forms.Select(attrs={"class": "form-select"}),
            'ville_territoire': forms.TextInput(attrs={"class": "form-control", 'placeholder': "Entrer le nom de la ville ou le territoire"}),
        }

class Axe_Projet(forms.ModelForm):
    def initialisation(self,context):
        projet = models.Doc_Projet.objects.get(id=context)
        ville_territoir = models.Ville_Territoire_Projet.objects.all()
        liste_territoire = []
        for data in ville_territoir:
            if data.province.pays.projet == projet:
                liste_territoire.append((data.id,data))
        liste_territoire.reverse()
        self.fields['ville_territoire'].choices = liste_territoire
    class Meta:
        model = models.Axe_Projet
        fields = "__all__"
        widgets = {
            "ville_territoire": forms.Select(attrs={'class': 'form-select'}),
            "axe": forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Entrer le nom de l'axe"}),
        }


class Coordination_National(forms.ModelForm):

    class Meta:
        model = models.Coordination_Nationale_Projet
        fields = ['coordination_national']
        labels = {
            "coordination_national": "",
        }
        widgets = {
            "coordination_national": forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Coordination Nationale"}),
        }

class Coordination_Provinciale(forms.ModelForm):
    def initialisation(self,context):
        projet = models.Doc_Projet.objects.get(id=context)
        cn = models.Coordination_Nationale_Projet.objects.filter(projet=projet)
        liste_cn= []
        for data in cn:
            liste_cn.append((data.id,data))
        liste_cn.reverse()
        self.fields['cordination_nationale'].choices = liste_cn
    class Meta:
        model = models.Coordination_Provinciale_Projet
        fields = "__all__"
        widgets = {
            "cordination_nationale": forms.Select(attrs={'class': 'form-select'}),
            "coordination_provinciale": forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Coordination provinciale"}),
        }


class Antenne_projet(forms.ModelForm):
    def initialisation(self,context):
        projet = models.Doc_Projet.objects.get(id=context)
        coop = models.Coordination_Provinciale_Projet.objects.all()
        liste_coop = []
        for data in coop:
            if data.cordination_nationale.projet == projet:
                liste_coop.append((data.id,data))
        liste_coop.reverse()
        self.fields['coordination_provinciale'].choices = liste_coop
    class Meta:
        model = models.Antenne_Projet
        fields = "__all__"
        widgets = {
            "coordination_provinciale": forms.Select(attrs={'class': 'form-select'}),
            "antenne_projet": forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Antenne"}),
        }



class VoletProjet(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        key = kwargs.pop('key', None)
        super(VoletProjet, self).__init__(*args, **kwargs)
        if key:
            listdomaine = []
            domaine = models.DomaineProjet.objects.get(id=key)
            if domaine:
                listdomaine.append((domaine.id, domaine))
            listvolet = models.Volet.objects.filter(domaine=domaine.domaine)
            self.fields['volet'].queryset = listvolet
            self.fields['domaine'].choices = listdomaine
    class Meta:
        model = models.VoletProjet
        fields = "__all__"
        labels = {
            "objectif_LAC": "OBJECTIF LAC ASBL DE DEVELOPPEMENT",
            "objectif_SMART": "OBJECTIF SPECIFIQUE SMART",
            "vue_d_ensemble": "VUE D'ENSEMBLE OU SOMMAIRE DE LA STRATEGIE",
            "description_des_effets": "DESCRIPTION DES EFFETS ESPERES",
            "nbre_succes": "NOMBRE D'HISTOIRE A SUCCES A DOCUMENTER",
            "enumererpersonnel": "ENUMERATION DU PERSONNEL",
        }
        widgets = {
            "domaine": forms.Select(attrs={'class': 'form-control'}),
            "volet": forms.Select(attrs={'class': 'form-control'}),
            "objectif_LAC": forms.Textarea(attrs={"class": "form-control",
                                                   "placeholder": "Objectif LACasbl  de développement "
                                                                  "auquel le programme contribue dans ce volet"}),
            "objectif_SMART": forms.Textarea(attrs={"class": "form-control",
                                                     "placeholder": "Objectif spécifique SMART "
                                                                    "poursuivi par ce programme  dans ce volet"}),
            "vue_d_ensemble": forms.Textarea(attrs={"class": "form-control",
                                                     "placeholder": "Vue d’ensemble ou sommaire de la "
                                                                    "stratégie et tactiques pour atteindre "
                                                                    "l’objectif du programme dans ce volet"}),
            "description_des_effets": forms.Textarea(attrs={"class": "form-control",
                                                             "placeholder": "Description des effets espérés "
                                                                            "(veuillez préciser "
                                                                            "l'année de déscription)"}),
            "enumererpersonnel": forms.Textarea(attrs={"class": "form-control",
                                                        "placeholder": "Enumérez le personnel "
                                                                       "clé et le nombre de jours de travail"}),
            "nbre_succes": forms.TextInput(attrs={'class': 'form-control form-control-sm',
                                                  "placeholder": "Nombre d'histoire à succès à documenter "
                                                                 "(veuillez préciser l'année de documentation)"}),
        }


class ActivitePrincipale(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        key = kwargs.pop('key', None)
        super(ActivitePrincipale, self).__init__(*args, **kwargs)
        if key:
            listvolet = []
            volet = models.VoletProjet.objects.get(id=key)
            if volet:
                listvolet.append((volet.id, volet))
            self.fields['volet'].choices = listvolet
    class Meta:
        model = models.ActivitePrincipal
        fields = '__all__'
        labels = {
            "activitePrincipale": "",
            "responsable_execution": "",
            "volet": "",
        }
        widgets = {
            "volet": forms.Select(attrs={"class": "form-control"}),
            "activitePrincipale": forms.Textarea(attrs={"class": "form-control", "placeholder": "Activité principale"}),
            "responsable_execution": forms.TextInput(attrs={"class": "form-control", "placeholder": "Responsable d'exécution"}),
        }


class Suivi_des_indicateurs(forms.ModelForm):
    periode_execution = forms.MultipleChoiceField(
        choices=[
            ('janvier', 'janvier'),
            ('février', 'février'),
            ('mars', 'mars'),
            ('avril', 'avril'),
            ('mai', 'mai'),
            ('juin', 'juin'),
            ('juillet', 'juillet'),
            ('aout', 'aout'),
            ('septembre', 'septembre'),
            ('octobre', 'octobre'),
            ('novembre', 'novembre'),
            ('décembre', 'décembre'),
        ], widget=forms.CheckboxSelectMultiple
    )

    def __init__(self, *args, **kwargs):
        key = kwargs.pop('key', None)
        super(Suivi_des_indicateurs, self).__init__(*args, **kwargs)
        if key:
            listact = []
            actp = models.ActivitePrincipal.objects.get(id=key)
            if actp:
                listact.append((actp.id, actp))
            self.fields['activite_principale'].choices = listact

    class Meta:
        model = models.Suivi_de_indicateurs_projet
        fields = ['activite_principale', 'indicateur_lac', 'base_line_gab',
                  'cible_NA', 'source_outils', 'frequence_de_collecte', 'periode_execution']
        labels = {
            'activite_principale': "",
            'indicateur_lac': "Indicateur LAC",
            'base_line_gab': "Base_line/GAP",
            'cible_NA': "Cible_NA",
            'source_outils': "Sources des données",
            'frequence_de_collecte': "Fréquence de la collecte",
        }
        widgets = {
            'indicateur_lac': forms.TextInput(attrs={"class": "form-control", "placeholder": "Indicateurs standard de LAC asbl"}),
            'base_line_gab': forms.TextInput(attrs={"class": "form-control", "placeholder": "Base line/GAP"}),
            'cible_NA': forms.TextInput(attrs={"class": "form-control", "placeholder": "Cible (ou N/A) veuillez préciser l'année"}),
            'source_outils': forms.TextInput(attrs={"class": "form-control", "placeholder": "Source des données y compris l’outil utilisé"}),
            'frequence_de_collecte': forms.TextInput(attrs={"class": "form-control", "placeholder": "Fréquence de la collecte"}),
            'periode_execution': forms.SelectMultiple(attrs={"class": "form-control"}),
        }


class Gestion_des_risques(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        key = kwargs.pop('key', None)
        super(Gestion_des_risques, self).__init__(*args, **kwargs)
        if key:
            listvolet = []
            volet = models.VoletProjet.objects.get(id=key)
            if volet:
                listvolet.append((volet.id, volet))
            self.fields['volet'].choices = listvolet
    class Meta:
        model = models.Gestion_des_risques_SI
        fields = '__all__'
        labels = {
            "volet": "",
            "description": "",
            "mesure": "",
            "responsable": "",
        }
        widgets = {
            "description": forms.Textarea(attrs={"class": "form-control", "placeholder": "Déscription du risque"}),
            "mesure": forms.Textarea(attrs={"class": "form-control", "placeholder": "Mesure de mitigation"}),
            "responsable": forms.TextInput(attrs={"class": "form-control", "placeholder": "Responsable de prévention"}),
        }


class BudgetPlan(forms.ModelForm):
    def initialisations(self,context):
        projet = models.Doc_Projet.objects.get(id=context)
        activiteprincipale = models.ActivitePrincipal.objects.all()
        liste_ap = []
        for ap in activiteprincipale:
            if ap.volet.domaine.projet == projet:
                liste_ap.append((ap.id, ap))
        self.fields['activite_principale'].choices = liste_ap

    class Meta:
        model = models.BudgetEtPlanDecaissement
        fields = '__all__'
        labels = {
            'activite': "Sélectionner l'activité à budgetiser",
            'numLigne': 'Numéro de ligne budgetaire',
            'designation': 'Désignation',
            'unite': 'Unité',
            'quantite': 'Quantité',
            'frequence': 'Fréquence',
            'prixUnit': 'Prix Unitaire',
            'partenaire': '',
        }
        widgets = {
            'prixTot':forms.HiddenInput()
        }


class BudgetPlanMod(forms.ModelForm):
    def initialisations(self,context):
        projet = models.Doc_Projet.objects.get(id=context)
        sous_activites = models.Sous_activite_Ap.objects.all()
        liste_sa = []
        for sa in sous_activites:
            if sa.actPrincipal.objSpec.objglob.volet.domaine.projet == projet:
                liste_sa.append((sa.id, sa))

        self.fields['projet'].choices = [(context, projet)]
        self.fields['activite'].choices = liste_sa

    class Meta:
        model = models.BudgetEtPlanDecaissement
        fields = '__all__'
        labels = {
            'projet': 'Projet ID',
            'activite': "Sélectionner l'activité à budgetiser",
            'numLigne': 'Numéro de ligne budgetaire',
            'designation': 'Désignation',
            'unite': 'Unité',
            'quantite': 'Quantité',
            'frequence': 'Fréquence',
            'prixUnit': 'Prix Unitaire',
        }
        widgets = {
            'dateDecaissement': widgets.SelectDateWidget,
            'prixTot':forms.HiddenInput()
        }


class Modif_sa_detail(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        key = kwargs.pop('key', None)
        super(Modif_sa_detail, self).__init__(*args, **kwargs)
        list_indicateur = []
        list_ligne_budgetaire = []
        if key:
            indicateur = models.Suivi_de_indicateurs_projet.objects.get(id=key)
            ap = indicateur.activite_principale

            list_indicateur.append((indicateur.id, indicateur))
            self.fields['indicateur'].choices = list_indicateur

    class Meta:
        model = models.Sous_activite_Ap
        fields = '__all__'
        labels = {
            'sousactivite': "",
            'descapproche': "",
            'outildesupervision': "",
            'partenairetechnique': "",
            'partenairetatique': "",
            'lieu_execution': "",
            'date_debut': "Date de début",
            'date_fin': "Date de fin",
            'date_rapportage': "Date de rapportage",
        }
        widgets = {
            'sousactivite': forms.TextInput(attrs={'class': 'form-control',
                                                   'placeholder': "Sous activités /Opérations Prénant "
                                                                  "en compte les mesures de mittigations"}),
            'descapproche': forms.TextInput(attrs={'class': 'form-control',
                                                   'placeholder': "Description de l'approche d'exécution de "
                                                                  "cette sous-activité"}),
            'outildesupervision': forms.TextInput(attrs={'class': 'form-control',
                                                   'placeholder': "outils de supervision de l'activité sur terrain"}),
            'partenairetechnique': forms.TextInput(attrs={'class': 'form-control',
                                                   'placeholder': "Partenaire Technique d'Exécution sur terrain"}),
            'partenairetatique': forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': "Partenaire Etatique d'Exécution sur terrain"}),
            'lieu_execution': forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': "Lieu d'exécution"}),
            'date_debut': forms.SelectDateWidget(),
            'date_fin': forms.SelectDateWidget(),
            'date_rapportage': forms.SelectDateWidget(),
        }

class Personnel_Execution(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        key = kwargs.pop('key', None)
        super(Personnel_Execution, self).__init__(*args, **kwargs)
        list_volet = []
        if key:
            projet = models.Doc_Projet.objects.get(id=key)
            volet = models.VoletProjet.objects.all()
            for vlt in volet:
                if vlt.domaine.projet == projet:
                    list_volet.append((vlt.id, vlt))
            self.fields['volet'].choices = list_volet
    class Meta:
        model = models.Personnel_de_mise_en_oeuvre
        fields = '__all__'
        labels = {
            'volet': "",
            'personnel': "",
            'effectif': "",
            'nombre_jour': "Nombre des jours de travail",
            'sexe_souhaite': "Sexe souhaité",
            'role_responsabilite': "",
            'profil_poste': "",
        }
        widgets = {
            'personnel': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Personnel"}),
            'effectif': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Effectif"}),
            'sexe_souhaite': forms.Select(choices=[("1","Masculin"), ("2","Féminin")]),
            'role_responsabilite': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Rôle/Responsabilité dans le programme"}),
            'profil_poste': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Profil de ce poste"}),
        }

# class EtatdeBesoin_LigneBudgetaire(forms.ModelForm):
#     def initialisation(self, context):
#         projet = models.Doc_Projet.objects.get(id = context)
#         # self.fields['projet'].choices = [('1',projet)]
#         sous_activites = models.SousActivite.objects.all()
#         liste_sa = []
#         for sa in sous_activites:
#             if sa.actPrincipal.objSpec.objglob.volet.domaine.projet == projet:
#                 liste_sa.append((sa.id, sa))
#         self.fields['sous_activite'].choices = liste_sa
#     class Meta:
#         model = models.EtatdeBesoin_LigneBudgetaire
#         fields = ['etat_de_besoin','sous_activite']

# class Bulletin_Info(forms.ModelForm):
#     def initialisation(self,context):
#         projet = models.Doc_Projet.objects.get(id=context)
#         sous_activite = models.SousActivite.objects.all()
#         liste_sa = []
#         for sa in sous_activite:
#             if sa.actPrincipal.objSpec.objglob.volet.domaine.projet == projet:
#                 liste_sa.append((sa.id,sa))
#         self.fields['sous_activite'].choices = liste_sa
#     class Meta:
#         model = models.BulletinInfo
#         fields = ['sous_activite','resultatAtteints','leconAprise','justification','lieuxExecution',
#                   'date_debut','date_fin','statut','mesuresCorrectives']
#         widgets = {
#             'date_debut': forms.DateInput(attrs={'type': 'date', 'format': '%d/%m/%Y'}),
#             'date_fin': forms.DateInput(attrs={'type': 'date', 'format': '%d/%m/%Y'}),
#         }
class Photo_Realisation_Sitrep(forms.ModelForm):
    class Meta:
        model = models.PhotoRealisation_Sitrep
        fields = "__all__"


class PlanDetaille_Sa(forms.ModelForm):
    class Meta:
        model = models.Sous_activite_Ap
        fields = [
            'sousactivite',
            'descapproche',
            'strategie_genre',
            'inclusion_pers_besoin',
            'contribution',
            'besoinenappui',
            'outildesupervision',
            'partenairetechnique',
            'partenairetatique',
            'lieu_execution',
            'date_debut',
            'date_fin',
            'date_rapportage',
        ]
        labels = {
            "sousactivite": "",
            "descapproche": "",
            "strategie_genre": "",
            "inclusion_pers_besoin": "",
            "contribution": "",
            "besoinenappui": "L'activité a-t-il besoin d'appui du service communication ?(média,Repportage,publication,Designe,…); OUI/NON",
            "outildesupervision": "",
            "partenairetechnique": "",
            "partenairetatique": "",
            "lieu_execution": "",
            "date_debut": "date de début",
            "date_fin": "date de fin",
            "date_rapportage": "date de rapportage",
            "ligne_budgetaire_correspondante": "ligne budgétaire corréspondate",
        }

        widgets = {
            'sousactivite': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': "Sous activités /Opérations Prénant "
                                                                  "en compte les mesures de mittigations"}),
            'descapproche': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': "Description de l'approche d'exécution de sous activité"}),
            'strategie_genre': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': "Stratégie de prise en compte genre"}),
            'inclusion_pers_besoin': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': "Inclusion de  personnes à besoin spéciques(PVH,..)  ,la prise en compte de leurs besoin et intégration de thèmes sensibles au coflits"}),
            'contribution': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': "Contribution  de l'action au developpement durable et conservation nature"}),
            'outildesupervision': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': "outils de supervision de l'activité sur terrain"}),
            'partenairetechnique': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': "Partenaire Technique d'Exécution sur terrain"}),
            'partenairetatique': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': "Partenaire Etatique d'Exécution sur terrain"}),
            'lieu_execution': forms.TextInput(attrs={'class': 'form-control form-control-sm', 'placeholder': "Lieu d'exécution"}),

            'date_debut': forms.DateInput(
                attrs={'type': 'date', 'format': '%d/%m/%Y', 'class': 'form-control form-control-sm'}),
            'date_fin': forms.DateInput(
                attrs={'type': 'date', 'format': '%d/%m/%Y', 'class': 'form-control form-control-sm'}),
            'date_rapportage': forms.DateInput(
                attrs={'type': 'date', 'format': '%d/%m/%Y', 'class': 'form-control form-control-sm'}),
            'besoinenappui': forms.Select(attrs={'class': 'form-control'}, choices=[("1","OUI"), ("2","NON")]),
        }

class Mapping(forms.ModelForm):
    def initialisation(self,pk:int):
        self.fields['projet'].choices = [(models.Doc_Projet.objects.get(id=pk).id, models.Doc_Projet.objects.get(id=pk))]
    class Meta:
        model = models.Mapping_Projet
        fields = '__all__'
        labels = {
            'projet': "",
            'grade_agent':"Grade de l'agent",
            'effectif_recherche':"Effectif recherché",
            'nombre_de_jours':"Nombre de jours de travail",
            'reponsables_h':"Responsables herarchique",
            'personnel_supervise':"Personnel supervises directement et / ou indirectement",
            'responsable_cle':"Responsabilites clés du personnel",
            'description_taches':"Description de taches dans le prgramme",
            'profil_de_ce_poste':"Profil de ce poste/conditions a remplir",
            'type_de_recrutement':"Type de recrutement (interne/externe/mixt)",
            'debut_recrutement':"Début",
            'type_contrat':"Type de contrats à donner au staff",
            'nature_contrat':"Nature de contrat",
            'id_agent':"ID agent",
            'date_debut_contrat':"Date de début du contrat",
            'date_de_fin_contrat':"Date de fin du contrat",
            'date_de_fin_essai':"Date de fin d'essai ",
            'date_premiere_evaluation':"Date de la 1ère évaluation de performence",
            'total_salaire':"Total salaire  brute prevu",
            'ligne_budgetaire':"Ligne budgetaire à imputer",
            'impot_DGI':"Retenues  impôt DGI",
            'retune_CNSS':"Retenues  cotisation CNSS",
            'retune_NPP':"Retenues  NPP",
            'retune_CaisseSociale':"Retenues  caisse sociale agents LACasbl",
            'net_a_payer':"Net à payer",
            'equipement':"Equipement necessaires à disponibiliser au personnel",
        }
        widgets = {
                    'projet':forms.Select(attrs={'class':'form-control form-select-sm'}),
                    'personnel': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
                    'grade_agent': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
                    'affectation': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
                    'personnel_supervise': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
                    'responsable_cle': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
                    'description_taches': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
                    'type_contrat': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
                    'type_de_recrutement': forms.Select(choices=[('i','INTERNE'),('e','EXTERNE'),('m','MIXT')],
                                                        attrs={'class':'form-control form-control-sm'}),
                    'nature_contrat': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
                    'id_agent': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
                    'ligne_budgetaire': forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'ligen budgetaire'}),

                    'profil_de_ce_poste': forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 2}),
                    'equipement': forms.Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 2}),

                    'debut_recrutement': widgets.SelectDateWidget(attrs={'type':'date','class':'form-control form-control-sm'}),
                    'fin_recrutement': widgets.SelectDateWidget(attrs={'type':'date','class':'form-control form-control-sm'}),
                    'date_debut_contrat': widgets.SelectDateWidget(attrs={'type':'date','class':'form-control form-control-sm'}),
                    'date_de_fin_contrat': widgets.SelectDateWidget(attrs={'type':'date','class':'form-control form-control-sm'}),
                    'date_premiere_evaluation': widgets.SelectDateWidget(attrs={'type':'date','class':'form-control form-control-sm'}),
                    'date_de_fin_essai': widgets.SelectDateWidget(attrs={'type':'date','class':'form-control form-control-sm'}),

                    'reponsables_h': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
                    'effectif_recherche': forms.NumberInput(attrs={'class':'form-control form-control-sm','min':0}),
                    'nombre_de_jours': forms.NumberInput(attrs={'class':'form-control form-control-sm','min':0}),
                    'total_salaire': forms.NumberInput(attrs={'class':'form-control form-control-sm','min':0}),
                    'net_a_payer': forms.NumberInput(attrs={'class':'form-control form-control-sm','min':0}),
                    'retune_CaisseSociale': forms.NumberInput(attrs={'class':'form-control form-control-sm','min':0}),
                    'retune_NPP': forms.NumberInput(attrs={'class':'form-control form-control-sm','min':0}),
                    'retune_CNSS': forms.NumberInput(attrs={'class':'form-control form-control-sm','min':0}),
                    'impot_DGI': forms.NumberInput(attrs={'class':'form-control form-control-sm','min':0}),
                }


