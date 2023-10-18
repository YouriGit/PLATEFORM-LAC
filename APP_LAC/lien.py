from django.urls import path

from APP_LAC import views

urlpatterns = [
    path('', views.index_office, name="index_office"),
    path('module_connexion', views.module_connexion, name="module_connexion"),
    path('admindashboard/', views.admindashboard, name="admindashboard"),
    path('agentdashboard/', views.agentdashboard, name="agentdashboard"),
    path('ajout_agent/', views.ajout_agent, name="ajout_agent"),
    path('create_user', views.create_user, name="create_user"),
    path('profil_agent/<int:pk>', views.profil_agent, name="profil_agent"),
    path('mon_profil_agent/<int:pk>', views.mon_profil_agent, name="mon_profil_agent"),
    path('mod_modif_profil/<int:pk>', views.mod_modif_profil, name="mod_modif_profil"),
    path('module_deconnexion', views.module_deconnexion, name="module_deconnexion"),
    path('note_service', views.note_service, name="note_service"),
    path('modif_note_service/<int:pk>', views.modif_note_service, name="modif_note_service"),
    path('mod_sup_note/<int:pk>', views.mod_sup_note, name="mod_sup_note"),
    path('test', views.test, name='test'),
    path('ajouter', views.ajouter, name="ajouter"),
    path('scaner', views.scaner_les_utilisateur, name='test'),

    path('apercu_du_projet/<int:pk>',views.apercu_du_projet,name='apercu_du_projet'),
    path('mod_ajouter_doc_projet',views.mod_ajouter_doc_projet,name='mod_ajouter_doc_projet'),
    path('demande_de_confirmation/<int:pk>', views.demande_de_confirmation,name='demande_de_confirmation'),
    path('effacer_un_agent/<int:pk>', views.effacer_un_agent,name='effacer_un_agent'),
    path('effacer_une_note/<int:pk>', views.effacer_une_note,name='effacer_une_note'),
    path('confirmation_note_de_service/<int:pk>', views.confirmation_note_de_service,name='confirmation_note_de_service'),
    path('ajouter_echo_de_bureau', views.ajouter_echo_de_bureau, name="ajouter_echo_de_bureau"),
    path('doc_projet', views.doc_projet, name="doc_projet"),
    path('mes_document_admin/<int:pk>/<str:doc>', views.mes_document_admin, name="mes_document_admin"),
    path('ajouter-agenda', views.ajouter_agenda, name="ajouter_agenda"),
    path('mod_modifier_agenda/<int:pk>', views.mod_modifier_agenda, name="mod_modifier_agenda"),
    path('mod_sup_agenda/<int:pk>', views.mod_sup_agenda, name="mod_sup_agenda"),
    path('suivi_de_contrat/<int:pk>', views.suivi_de_contrat, name='suivi_de_contrat'),

    path('configuration_doc_projet/<int:pk>', views.configuration_doc_projet, name='configuration_doc_projet'),
    path('office/mod_ajouter_domainProjet/<int:idprojet>', views.mod_ajouter_domainProjet, name='mod_ajouter_domainProjet'),
    path('mod_ajouter_une_activite_principale/<int:pk>', views.mod_ajouter_une_activite_principale, name='mod_ajouter_une_activite_principale'),
    path('liste_projet', views.liste_projet, name='liste_projet'),
    path('exporter_doc_projet/<int:pk>', views.exporter_doc_projet, name='exporter_doc_projet'),

    #LOCALISATION DU PROJET
    path('loc_pays/<int:pk>',views.loc_pays,name='loc_pays'),
    path('loc_province/<int:pk>',views.loc_province,name='loc_province'),
    path('loc_ville_territoire/<int:pk>',views.loc_ville_territoire,name='loc_ville_territoire'),
    path('loc_axe/<int:pk>',views.loc_axe,name='loc_axe'),

    #BUREAU D'EXECUTION DU PROJET
    path('ajouter_cn/<int:pk>', views.ajouter_cn, name='ajouter_cn'),
    path('ajouter_cp/<int:pk>',views.ajouter_cp, name='ajouter_cp'),
    path('ajouter_aldpe/<int:pk>', views.ajouter_aldpe, name='ajouter_aldpe'),

    #DOMAINE DE RESULTAT
    path('configuration_domaine_doc_projet/<int:pk>', views.configuration_domaine_doc_projet, name='configuration_domaine_doc_projet'),
    path('mod_supprimer_domaine_resultat/<int:pk>', views.mod_supprimer_domaine_resultat, name='mod_supprimer_domaine_resultat'),
    path('ajouter_volet_domaine/<int:pk>', views.ajouter_volet_domaine, name='ajouter_volet_domaine'),
    path('mod_ajouter_volet_domaine/<int:pk>', views.mod_ajouter_volet_domaine, name='mod_ajouter_volet_domaine'),
    path('modifier_domaine/<int:pk>', views.modifier_domaine, name='modifier_domaine'),
    path('mod_modifier_domaine/<int:pk>', views.mod_modifier_domaine, name='mod_modifier_domaine'),

    #VOLET
    path('edit_volet_projet/<int:pk>', views.edit_volet_projet, name='edit_volet_projet'),
    path('mod_modifier_volet_projet/<int:pk>', views.mod_modifier_volet_projet, name='mod_modifier_volet_projet'),
    path('mod_effacer_volet/<int:pk>', views.mod_effacer_volet, name='mod_effacer_volet'),

    #ACTIVITES PRINCIPALES
    path('ajouter_ap_volet/<int:pk>', views.ajouter_ap_volet, name='ajouter_ap_volet'),
    path('mod_ajouter_ap_volet/<int:pk>', views.mod_ajouter_ap_volet, name='mod_ajouter_ap_volet'),
    path('mod_effacer_ap/<int:pk>', views.mod_effacer_ap, name='mod_effacer_ap'),
    path('edit_activite_principale_projet/<int:pk>', views.edit_activite_principale_projet, name='edit_activite_principale_projet'),
    path('mod_modifier_activite_principale_projet/<int:pk>', views.mod_modifier_activite_principale_projet, name='mod_modifier_activite_principale_projet'),


    #modifications du vrai projet
    path('edit_doc_projet/<int:pk>',views.edit_doc_projet,name='edit_doc_projet'),
    path('mod_modifier_doc_projet/<int:pk>',views.mod_modifier_doc_projet,name='mod_modifier_doc_projet'),

    #PARTENAIRE PROJET
    path('add_partenaire_execution/<int:pk>', views.add_partenaire_execution, name='add_partenaire_execution'),
    path('edit_partenaire_execution/<int:pk>', views.edit_partenaire_execution, name='edit_partenaire_execution'),
    path('mod_edit_partenaire_execution/<int:pk>', views.mod_edit_partenaire_execution, name='mod_edit_partenaire_execution'),
    path('delete_partenaire_execution/<int:pk>', views.delete_partenaire_execution, name='delete_partenaire_execution'),

    #PAYS PROJET
    path('edit_pays_projet/<int:pk>',views.edit_pays_projet,name='edit_pays_projet'),
    path('mod_delete_pays_projet/<int:pk>',views.mod_delete_pays_projet,name='mod_delete_pays_projet'),
    path('mod_modifier_pays_projet/<int:pk>',views.mod_modifier_pays_projet,name="mod_modifier_pays_projet"),

    #PROVINCE PROJET
    path('edit_province_projet/<int:pk>/<int:projet>',views.edit_province_projet,name='edit_province_projet'),
    path('mod_delete_province_projet/<int:pk>',views.mod_delete_province_projet,name='mod_delete_province_projet'),
    path('mod_modifier_province_projet/<int:pk>/<int:projet>',views.mod_modifier_province_projet,name="mod_modifier_province_projet"),

    #VILLE TERRITOIR PROJET
    path('edit_territoir_ville_projet/<int:pk>/<int:projet>', views.edit_territoir_ville_projet, name='edit_territoir_ville_projet'),
    path('mod_delete_villeterritoire_projet/<int:pk>',views.mod_delete_villeterritoire_projet,name='mod_delete_villeterritoire_projet'),
    path('mod_modifier_territoir_ville_projet/<int:pk>/<int:projet>', views.mod_modifier_territoir_ville_projet,
         name="mod_modifier_territoir_ville_projet"),

    #AXE PROJET
    path('edit_axe_projet/<int:pk>/<int:projet>', views.edit_axe_projet, name='edit_axe_projet'),
    path('mod_delete_axe_projet/<int:pk>',views.mod_delete_axe_projet,name='mod_delete_axe_projet'),
    path('mod_modifier_axe_projet/<int:pk>/<int:projet>', views.mod_modifier_axe_projet,
         name="mod_modifier_axe_projet"),

    #COORDINATION NATIONALE
    path('edit_cn_projet/<int:pk>', views.edit_cn_projet, name='edit_cn_projet'),
    path('mod_delete_coonal_projet/<int:pk>', views.mod_delete_coonal_projet, name='mod_delete_coonal_projet'),
    path('mod_modifier_cn_projet/<int:pk>', views.mod_modifier_cn_projet,
         name="mod_modifier_cn_projet"),

    #COORDINATION PROVINCIALE
    path('edit_cp_projet/<int:pk>/<int:projet>', views.edit_cp_projet, name='edit_cp_projet'),
    path('mod_delete_coopr_projet/<int:pk>',views.mod_delete_coopr_projet,name='mod_delete_coopr_projet'),
    path('mod_modifier_cp_projet/<int:pk>/<int:projet>', views.mod_modifier_cp_projet,
         name="mod_modifier_cp_projet"),

    #ANTENNE PROJET
    path('edit_antenne_projet/<int:pk>/<int:projet>', views.edit_antenne_projet, name='edit_antenne_projet'),
    path('mod_delete_antenne_projet/<int:pk>',views.mod_delete_antenne_projet,name='mod_delete_antenne_projet'),
    path('mod_modifier_antenne_projet/<int:pk>/<int:projet>', views.mod_modifier_antenne_projet,
         name="mod_modifier_antenne_projet"),


    #INDICATEURS
    path('suivi_des_indicateurs/<int:pk>', views.suivi_des_indicateurs, name="suivi_des_indicateurs"),
    path('mod_ajouter_suivi_indicateur/<int:pk>', views.mod_ajouter_suivi_indicateur, name="mod_ajouter_suivi_indicateur"),
    path('mod_delete_indicateur/<int:pk>', views.mod_delete_indicateur, name='mod_delete_indicateur'),
    path('edit_indicateur/<int:pk>', views.edit_indicateur, name='edit_indicateur'),
    path('mod_modifier_indicateur/<int:pk>', views.mod_modifier_indicateur, name='mod_modifier_indicateur'),


    #GESTION DES RISQUES
    path('edit_risque/<int:pk>', views.edit_risque, name='edit_risque'),
    path('mod_modifier_risque/<int:pk>', views.mod_modifier_risque, name='mod_modifier_risque'),
    path('mod_delete_risque/<int:pk>', views.mod_delete_risque, name='mod_delete_risque'),
    path('ajouter_gestion_risque/<int:pk>', views.ajouter_gestion_risque, name='ajouter_gestion_risque'),
    path('mod_ajouter_risque/<int:pk>', views.mod_ajouter_risque, name="mod_ajouter_risque"),

    #BUDGET ET PLAN DE DECAISSEMENT
    path('budget/<int:pk>', views.budget, name='budget'),
    path('edit_budget/<int:pk>',views.edit_budget, name='edit_budget'),
    path('mod_modifier_budget/<int:pk>',views.mod_modifier_budget, name='mod_modifier_budget'),
    path('mod_ajouter_budgetPlan/<int:pk>',views.mod_ajouter_budgetPlan, name='mod_ajouter_budgetPlan'),
    path('delete_budget/<int:pk>',views.delete_budget, name='delete_budget'),

    #EXPORTER BUDGET_DETAILLE
    path('exporter_doc_budget/<int:pk>', views.exporter_doc_budget, name='exporter_doc_budget'),

    # PLANIFICATION DETAILLEE DES ACTIVITES
    path('planification_detaillee/<int:pk>', views.planification_des_activites, name="planification_detaillee"),
    path('module_ajouter_une_planification', views.module_ajouter_une_planification,
         name="module_ajouter_une_planification"),

    #AJOUTER UNE LIGNE DE SOUS ACTIVITE DANS UN INDICATEUR, EDITER ET SUPPRIMER UN LIGNE DE DETAIL INDICATEUR
    path('edit_plan_detail/<int:pk>', views.edit_plan_detail, name="edit_plan_detail"),
    path('mod_modifier_plan/<int:pk>', views.mod_modifier_plan, name="mod_modifier_plan"),
    path('delete_plan_detail/<int:pk>/<int:idprojet>', views.delete_plan_detail, name="delete_plan_detail"),

    #MODIFIER ET SUPPRIMER UNE LIGNE DE SOUS-ACTIVITE
    path('modifier_sa_detail/<int:pk>', views.modifier_sa_detail, name="modifier_sa_detail"),
    path('mod_modifier_sa_detail/<int:pk>', views.mod_modifier_sa_detail, name="mod_modifier_sa_detail"),
    path('delete_sous_activite_detail/<int:pk>/<int:idprojet>', views.delete_sous_activite_detail, name="delete_sous_activite_detail"),

    #EXPORTER PLAN DETAILLE
    path('exporter_doc_plan_detaille/<int:pk>', views.exporter_doc_plan_detaille, name='exporter_doc_plan_detaille'),

    #BULLETIN D'INFORMATION / SITREP
    path('bulletinInfo/<int:pk>', views.bulletinInfo, name='bulletinInfo'),
    path('mod_ajouter_bulletin_info/<int:pk>', views.mod_ajouter_bulletin_info,name='mod_ajouter_bulletin_info'),
    path('mod_ajouter_photo_realisation/<int:pk>',views.mod_ajouter_photo_realisation,name='mod_ajouter_photo_realisation'),

    path('les_volets', views.les_volets, name='les_volets'),
    path('mod_ajouter_domaine_configuration/<int:pk>', views.mod_ajouter_domaine_configuration, name='mod_ajouter_domaine_configuration'),
    path('les_indicateurs', views.les_indicateurs, name='les_indicateurs'),
    path('les_lignes_budgetaires', views.les_lignes_budgetaires, name='les_lignes_budgetaires'),
    path('ajouter_personnel', views.ajouter_personnel, name='ajouter_personnel'),

    # Mapping
    path('mapping', views.mapping_index, name="mapping_index"),
    path('nouveau_mapping/<int:pk>', views.nouveau_mapping, name="nouveau_mapping"),
    path('ajouter_mapping/<int:pk>', views.mod_ajouter_mapping, name="mod_ajouter_mapping"),
    path('mod_modifier_mapping/<int:pk>', views.mod_modifier_mapping, name="mod_modifier_mapping"),
    path('affichage_mapping/<int:pk>', views.mapping_afficher, name="afficher le mapping du projet"),
    path('modifier_lign_mapping/<int:pk>', views.modifier_lign_mapping, name="modifier_lign_mapping"),
    path('mod_effacer_mapping/<int:pk>', views.mod_effacer_mapping, name="mod_effacer_mapping"),
]
