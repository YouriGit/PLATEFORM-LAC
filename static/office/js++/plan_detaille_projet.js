$(document).ready(function (){
    $("#select_domaine").change( function (e) {
        var optionSelectionnee = $(this).find("option:selected");
        $("#div_actp").css("display", "none");
        $("#div_sa").css("display", "none");
        $("#div_volet").css("display", "unset");
        e.preventDefault();
        var selectvolet = document.getElementById('select_volet');
        var selectactp = document.getElementById('select_actp');
        var selectindic = document.getElementById('select_indic');
        selectvolet.selectedIndex = 0;
        selectactp.selectedIndex = 0;
        selectindic.selectedIndex = 0;
        for(i=1; i < selectvolet.options.length; i++){
            var option = selectvolet.options[i]
            if(option.className == optionSelectionnee.attr('name')){
                option.style = 'display:unset';
            }
            else {
               option.style = 'display:none';
            }

        }
    })

    $("#select_volet").change( function (e) {
        var optionSelectionnee = $(this).find("option:selected");
        $("#div_actp").css("display", "unset");
        $("#div_sa").css("display", "none");
        e.preventDefault();
        var selectactp = document.getElementById('select_actp');
        var selectindic = document.getElementById('select_indic');
        selectactp.selectedIndex = 0;
        selectindic.selectedIndex = 0;
        for(i=1; i < selectactp.options.length; i++){
            var option = selectactp.options[i]
            if(option.className == optionSelectionnee.attr('name')){
                option.style = 'display:unset';
            }
            else {
               option.style = 'display:none';
            }

        }
    })

    $("#select_actp").change( function (e) {
        var optionSelectionnee = $(this).find("option:selected");
        var selectindic = document.getElementById('select_indic');
        selectindic.selectedIndex = 0;
        $("#div_sa").css("display", "unset");
        e.preventDefault();
        for(i=1; i < selectindic.options.length; i++){
            var option = selectindic.options[i]
            if(option.className == optionSelectionnee.attr('name')){
                option.style = 'display:unset';
            }
            else {
               option.style = 'display:none';
            }
        }
    })


    $("#select_indic").change( function (e) {
        var optionSelectionnee = $(this).find("option:selected");
        var inputindic = document.getElementById("indic_selected")
        inputindic.value = optionSelectionnee.val();
    })


    $('#form_plan_detail').submit(function(event) {
        event.preventDefault();
        $.ajax({
            url: "../module_ajouter_une_planification",
            type: 'POST',
            data: $('#form_plan_detail').serialize(),
            success: function(response) {
                alert(response.message);
            },
            error: function(xhr, status, error) {
                alert(error);
            }
        });
    });
})
// $(document).ready(function () {
//     $("input[name='choixdomaine']").change(function () {
//         var domaine = $(this).val();
//         $("#detail_indic").css("display", "none");
//         $(".div_sa_class").remove();
//         $("#id_outil_collecte").val("");
//         $("#id_methode_collecte").val("");
//         $("#id_frequence_collecte").val("");
//         $('.choixap').css("display", "none");
//         $('.class_ap_projet').prop('checked', false);
//         $('#indicateur').empty()
//         $('.choixvolet').each(function() {
//             var volet_domaine = $(this).attr('name');
//             if (domaine == volet_domaine) {
//                 $(this).css("display", "unset")
//                 $('.radiovoletprojet').prop('checked', false);
//             }else {
//                 $(this).css("display", "none")
//             }
//         })
//     })
//
//     $("input[name='choixvoletprojet']").change(function (){
//         var volet = $(this).val();
//         $("#detail_indic").css("display", "none");
//         $(".div_sa_class").remove();
//         $("#id_outil_collecte").val("");
//         $("#id_methode_collecte").val("");
//         $("#id_frequence_collecte").val("");
//         $('.class_ap_projet').prop('checked', false);
//         $('.choixap').each(function() {
//             var ap_projet = $(this).attr('name');
//             if (volet == ap_projet) {
//                 $(this).css("display", "unset")
//             }else {
//                 $(this).css("display", "none")
//             }
//         })
//         var list_volet = document.getElementById("id_volet");
//         for (i = 0; i < list_volet.length; i++) {
//             if(list_volet.options[i].value == volet) {
//                 list_volet.options[i].style = 'display:unset';
//                 list_volet.selectedIndex = i;
//             }else{
//                 list_volet.options[i].style = 'display:none';
//             }
//         }
//     })
//
//     $("#indicateur").change(function (){
//         $("#sous_act_par_indicateur").empty();
//     })
//
//     $('#form_plan_detail').submit(function(event) {
//         event.preventDefault();
//         $.ajax({
//           url: "../module_ajouter_une_planification",
//           type: 'post',
//           data: $('#form_plan_detail').serialize(),
//           dataType: 'json',
//           success: function(data) {
//               $("#sous_act_par_indicateur").remove();
//               alert(data.message);
//           }
//         });
//       })
//
//     $("input[name='actp']").change(function (){
//         var activiteprincipale = $(this).val();
//         $(".div_sa_class").remove();
//         $.ajax({
//             url:'../les_indicateurs',
//             dataType:'json',
//             data:{
//                 'ap':activiteprincipale,
//             },
//             success: function (data) {
//                 var options = '';
//                 $("#indicateur").empty();
//                 if (data.length > 0) {
//                     $('#detail_indic').css("display", "flex");
//                     $('#detail_indic').css("flex-direction", "column");
//                 }else{
//                     $('#detail_indic').css("display", "none")
//                 }
//                 for (var i=0; i<data.length; i++){
//                     options += '<option value=' + data[i].id + '>' + data[i].indicateur_lac + '</option>';
//                 }
//                 $("#indicateur").append(options);
//             },error: function (xhr, status, error){
//                 console.log("Erreur: " + error);
//                 alert("une erreur est survenue lors du traitement de le requête: "+ error)
//                 $('#detail_indic').css("display", "none")
//             }
//         });
//     })
// })
//
//
// var divsacount = 1
// var divconteneur = document.getElementById("sous_act_par_indicateur");
// function createsa() {
//     var indic = $("#indicateur").val()
//     var divsa = document.createElement("div");
//     var divbuttonremove = document.createElement("div");
//     var inputsa = document.createElement( "input");
//     var inputdescapp = document.createElement("input");
//     var strategiepriseencompte = document.createElement(("input"));
//     var inclusionpersonne = document.createElement(("input"));
//     var contribution = document.createElement(("input"));
//     var label2 = document.createElement("label")
//     var inputbesoinenappui = document.createElement("select");
//     var inputoutilsupervision = document.createElement("input");
//     var inputpartech = document.createElement("input");
//     var inputpartetatique = document.createElement("input");
//     var inputlieuexecution = document.createElement("input");
//     var inputdatedebut=document.createElement("input");
//     var inputdatefin=document.createElement("input");
//     var inputdaterapportage=document.createElement("input");
//     var inputlignebudgetaire=document.createElement("select");
//     var button = document.createElement("button");
//     var saut = document.createElement("br");
//     var label = document.createElement("label");
//     var lbldatedebut = document.createElement("label");
//     var lbldatefin = document.createElement("label");
//     var lbldaterapportage = document.createElement("label");
//     inputsa.setAttribute("placeholder", "Sous activités /Opérations Prénant en compte les mesures de mittigations");
//     inputsa.name = "sa_" + divsacount;
//
//     divsa.setAttribute("id", "div_" + inputsa.name);
//     divsa.setAttribute("class", "div_sa_class");
//     divbuttonremove.setAttribute("class", "div_sa_class");
//     divsa.style.display = "flex";
//     divsa.style.flexDirection = "column"
//
//     label2.textContent = "L'activité a-t-il besoin d'appui du service communication ?(média,Repportage,publication,Designe,…); OUI/NON"
//     inputdescapp.setAttribute("placeholder", "Description de l'approche d'exécution de sous activité ");
//     inputdescapp.name = "desc_" + inputsa.name;
//     inputbesoinenappui.innerHTML += '<option value="oui">OUI</option>';
//     inputbesoinenappui.innerHTML += '<option value="non">NON</option>';
//     inputbesoinenappui.name = "besoinenappui_" + inputsa.name;
//     inputoutilsupervision.setAttribute("placeholder", "outils de supervision de l'activité sur terrain");
//     inputoutilsupervision.name = "outilsupervision_" + inputsa.name;
//     inputpartech.setAttribute("placeholder", "Partenaire Technique d'Exécution sur terrain");
//     inputpartech.name = "partech_" + inputsa.name;
//     inputpartetatique.setAttribute("placeholder", "Partenaire Etatique d'Exécution sur terrain");
//     inputpartetatique.name = "partetat_" + inputsa.name;
//     inputlieuexecution.setAttribute("placeholder", "Lieu d'exécution");
//     inputlieuexecution.name = "lieuexecution_" + inputsa.name;
//     strategiepriseencompte.setAttribute("placeholder", "Stratégie de prise en compte genre");
//     strategiepriseencompte.name = "strategie_prise_" + inputsa.name;
//     inclusionpersonne.setAttribute("placeholder", "Inclusion de  personnes à besoin spéciques(PVH,..)  ,la prise en compte de leurs besoin et intégration de thèmes sensibles au coflits");
//     inclusionpersonne.name = "inclusionpersonne_" + inputsa.name;
//     contribution.setAttribute("placeholder", "Contribution  de l'action au developpement durable et conservation nature");
//     contribution.name = "contribution_action_" + inputsa.name;
//     inputdatedebut.setAttribute("placeholder", "Date de début");
//     inputdatedebut.type = 'date';
//     inputdatedebut.name = "datedebut_" + inputsa.name;
//     inputdatefin.setAttribute("placeholder", "Date de fin");
//     inputdatefin.type = 'date';
//     inputdatefin.name = "datefin_" + inputsa.name;
//     inputdaterapportage.setAttribute("placeholder", "Date rapportage sur l'activite");
//     inputdaterapportage.type = 'date';
//     inputdaterapportage.name = "daterapportage_" + inputsa.name;
//     inputlignebudgetaire.setAttribute("id", "id_lignebudgetaire_" + inputsa.name);
//     inputlignebudgetaire.name = "lignebudgetaire_" + inputsa.name;
//     label.textContent = "Ligne budgetaire"
//     lbldatedebut.textContent = "date de début";
//     lbldatefin.textContent = "date de fin";
//     lbldaterapportage.textContent = "date de rapportage";
//     button.setAttribute("id", "btn_" + inputsa.name);
//     button.style.backgroundColor = "red";
//     button.style.border = "1px solid white";
//     button.style.color = "white";
//     button.style.borderRadius = "3px";
//     button.textContent = "-";
//
//     $.ajax({
//         url:'../les_lignes_budgetaires',
//         dataType:'json',
//         data:{
//             'indicateur':indic,
//         },
//         success: function (data) {
//             divsa.appendChild(inputsa);
//             divsa.appendChild(inputdescapp);
//             divsa.appendChild(strategiepriseencompte);
//             divsa.appendChild(inclusionpersonne);
//             divsa.appendChild(contribution);
//             divsa.appendChild(label2);
//             divsa.appendChild(inputbesoinenappui);
//             divsa.appendChild(inputoutilsupervision);
//             divsa.appendChild(inputpartech);
//             divsa.appendChild(inputpartetatique);
//             divsa.appendChild(inputlieuexecution);
//             divsa.appendChild(lbldatedebut);
//             divsa.appendChild(inputdatedebut);
//             divsa.appendChild(lbldatefin);
//             divsa.appendChild(inputdatefin);
//             divsa.appendChild(lbldaterapportage);
//             divsa.appendChild(inputdaterapportage);
//             divsa.appendChild(label);
//             divsa.appendChild(inputlignebudgetaire);
//             divbuttonremove.appendChild(button);
//             divsa.appendChild(saut);
//             divconteneur.appendChild(divbuttonremove)
//             divconteneur.appendChild(divsa);
//
//             var options = '';
//             var ligne = "#id_" + inputlignebudgetaire.name;
//             for (var i=0; i<data.length; i++){
//                 options += '<option value=' + data[i].numLigne + '>' + data[i].numLigne + '</option>';
//             }
//             $(ligne).append(options);
//
//             function deletesa(){
//                 divsa.remove();
//                 divbuttonremove.remove();
//             }
//             var element = "btn_" + inputsa.name;
//             var btnsupsa = document.getElementById(element);
//             btnsupsa.addEventListener("click", deletesa);
//
//         },error: function (xhr, status, error){
//             console.log("Erreur: " + error);
//             alert("une erreur est survenue lors du traitement de le requête: "+ error)
//
//         }
//     });
//
//     divsacount++;
// }
//
//
// // function addPersonnel(){
// //     if ($("#id_personnel").value != ""){
// //         if ($("#id_effectif").value != ""){
// //             if ($("#id_nombre_jour").value != ""){
// //                 if ($("#id_effectif").value != ""){
// //                     if ($("#id_role_responsabilite").value != ""){
// //                         if ($("#id_profil_poste").value != ""){
// //                             $.ajax({
// //                                 url:'../ajout_personnel',
// //                                 dataType:'json',
// //                                 success: function () {
// //                                     alert("Ajouter")
// //                                 },error: function (xhr, status, error){
// //                                     console.log("Erreur: " + error);
// //                                     alert("une erreur est survenue lors du traitement de le requête: "+ error)
// //                                 }
// //                             });
// //                         }else{
// //                         }
// //                     }else{
// //                     }
// //                 }else{
// //                 }
// //             }else{
// //             }
// //         }else{
// //         }
// //     }else{
// //     }
// // }