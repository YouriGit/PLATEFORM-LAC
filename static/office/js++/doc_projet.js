var addButton = document.getElementById("add_button_domaine");
var divconteneur = document.getElementById("project_container");
var domainename = document.getElementById("id_domaine");

function createDomaine() {
    var divdomaine = document.createElement("div");
    var divvoletcontainerbase = document.createElement("div");
    var domainelbl = document.createElement("label")
    var buttonvolet = document.createElement("button")
    var select = document.createElement("select");
    var objlacdomaine = document.createElement("textarea")
    var label = document.createElement("label")
    var divvoletcount = 1
    var labelselect = document.createElement("label");

    divdomaine.setAttribute("id", "div_domaine");
    divdomaine.setAttribute("class", "container-fluid");
    divdomaine.style.padding = "5px";
    divdomaine.style.display = "flex";
    divdomaine.style.flexDirection = "column";
    divvoletcontainerbase.setAttribute("id", "div_domaine_volet_container");
    domainelbl.setAttribute("class", "label_domaine");
    domainelbl.setAttribute("id", "label_domaine");
    domainelbl.name = "domaineprojet"
    domainelbl.textContent = domainename[domainename.value].textContent;
    labelselect.textContent = "-- Sélectionner un volet --";
    labelselect.style.color = "gray";
    labelselect.style.fontSize = "14px";
    labelselect.style.marginTop = "12px";
    labelselect.style.marginBottom = "2px";
    buttonvolet.setAttribute("id", "button_volet_domaine");
    buttonvolet.setAttribute("type", "button");
    buttonvolet.textContent = "Ajouter ce volet";
    buttonvolet.setAttribute("class", "btn w-25 btn-sm btn-primary");
    buttonvolet.style.marginTop = "9px";
    select.setAttribute("id", "select_volet_domaine");
    select.setAttribute("class", "form-control");
    select.style.padding = "3px";
    objlacdomaine.setAttribute("placeholder", "Objectif LACasbl de développement dans ce domaine")
    objlacdomaine.setAttribute("id", "objlacdedomaine");
    objlacdomaine.setAttribute("required", true);
    objlacdomaine.className = "form-control";
    objlacdomaine.name = "objectiflacdomaine";

    var mondomaine = document.getElementById("id_domaine");
    mondomaine = mondomaine[mondomaine.value].textContent;

    $.ajax({
            url:'../les_volets',
            dataType:'json',
            data:{
                'domaine':mondomaine,
            },
            success: function (data) {
                var options = '';
                for (var i=0; i<data.length; i++){
                    options += '<option value"' + data[i].id + '">' + data[i].volet + '</option>';
                }
                addButton.style.display = "none";
                $("#id_domaine").css("display", "none");

                divdomaine.appendChild(domainelbl);
                divdomaine.appendChild(objlacdomaine);
                divdomaine.appendChild(divvoletcontainerbase);
                divdomaine.appendChild(labelselect);
                divdomaine.appendChild(select);
                divdomaine.appendChild(buttonvolet);
                divconteneur.appendChild(divdomaine);

                $("#select_volet_domaine").append(options);
                function createVolet() {
                    var selectedValue  = document.getElementById("select_volet_domaine");
                    var voletlist = document.querySelectorAll(".label_volet");
                    var scan = 0
                    voletlist.forEach(labelElement => {
                        if (labelElement.value == selectedValue.value) {
                            scan = 1
                        }else{
                            scan = 0
                        }
                    });
                    if (scan == 0) {
                        var divvolet = document.createElement("div");
                        var btnremovevolet = document.createElement("button");
                        var divcontainervolet = document.createElement("div");
                        var divvoletcontains = document.createElement("div");
                        var divaccordionbody = document.createElement("div");
                        var titrevolet = document.createElement("h4");
                        var btntitrevolet = document.createElement("button");
                        var divgestion = document.createElement("div");
                        var divrisque = document.createElement("div");
                        var divactivite = document.createElement("div");
                        var labeldivgestion = document.createElement("label");
                        var bouttonrisque = document.createElement("button");

                        var voletlbl = document.createElement("input");
                        var voletname = document.getElementById("select_volet_domaine");
                        var objlacvolet = document.createElement("textarea");
                        var objspecsmartvolet = document.createElement("textarea");
                        var strategietactique = document.createElement("textarea");
                        var desceffetspr = document.createElement("textarea");
                        var nbrTotalHist = document.createElement("input");
                        var enumPersonnelCle = document.createElement("textarea");
                        var boutonactivite = document.createElement("button");

                        var divactivitecount = 1;
                        var risquecount = 1;


                        divvolet.setAttribute("id", "volet_" + divvoletcount);
                        divvolet.setAttribute("class", "accordion mt-1 mb-3");
                        divvolet.style.padding = "0px";
                        divcontainervolet.setAttribute("class", "accordion-item");
                        divcontainervolet.style.padding = "0px";
                        divvoletcontains.setAttribute("class", "accordion-collapse collapse");
                        divvoletcontains.setAttribute("id", "collapse" + divvoletcount);
                        divvoletcontains.style.padding = "0px";
                        divaccordionbody.setAttribute("class", "accordion-body")
                        divaccordionbody.style.display = "flex";
                        divaccordionbody.style.padding = "0px";
                        divaccordionbody.style.flexDirection = "column";
                        titrevolet.setAttribute("class", "accordion-header");
                        titrevolet.setAttribute("id", "headingTwo_beta");
                        btntitrevolet.setAttribute("class", "accordion-button btn-sm collapsed");
                        btntitrevolet.setAttribute("data-bs-toggle", "collapse");
                        btntitrevolet.setAttribute("data-bs-target", "#collapse"+divvoletcount);
                        btntitrevolet.setAttribute("type", "button");
                        btntitrevolet.textContent = "VOLET " + divvoletcount;
                        btntitrevolet.setAttribute("aria-expanded", "false");
                        voletlbl.setAttribute("class", "label_volet");
                        voletlbl.setAttribute("id", "volet_" + divvoletcount);
                        voletlbl.value = voletname.value;
                        voletlbl.name = "volet_" + divvoletcount;
                        voletlbl.style.marginTop = "8px";
                        voletlbl.readOnly = true;
                        objlacvolet.setAttribute("placeholder", "Objectif LACasbl  de développement auquel le programme contribue dans ce volet");
                        objlacvolet.setAttribute("id", "objlacvolet_" + divvoletcount);
                        objlacvolet.setAttribute("required", true);
                        objlacvolet.setAttribute("class", "form-control");
                        objlacvolet.style.marginBottom = "4px";
                        objlacvolet.style.marginTop = "4px";
                        objlacvolet.name = "objectiflac_" + voletlbl.name;
                        btnremovevolet.setAttribute("id", "btn_remove_" + voletlbl.name);
                        btnremovevolet.style.backgroundColor = "red";
                        btnremovevolet.style.color = "white";
                        btnremovevolet.style.border = "none";
                        btnremovevolet.style.fontSize = "13px";
                        btnremovevolet.style.borderRadius = "8px";
                        btnremovevolet.textContent = "Rétirer";
                        btnremovevolet.setAttribute("type", "button");
                        objspecsmartvolet.setAttribute("placeholder", "Objectif spécifique SMART poursuivi par ce programme  dans ce volet");
                        objspecsmartvolet.setAttribute("id", "objspecsmartvolet_" + divvoletcount);
                        objspecsmartvolet.setAttribute("required", true);
                        objspecsmartvolet.setAttribute("class", "form-control");
                        objspecsmartvolet.style.marginTop = "4px";
                        objspecsmartvolet.name = "objectifspecsmart_" + voletlbl.name;
                        strategietactique.setAttribute("placeholder", "Vue d’ensemble ou sommaire de la stratégie et tactiques pour atteindre l’objectif du programme dans ce volet");
                        strategietactique.setAttribute("id", "strategietactique_" + divvoletcount)
                        strategietactique.setAttribute("required", true);
                        strategietactique.setAttribute("class", "form-control");
                        strategietactique.style.marginTop = "4px";
                        strategietactique.name = "vuestrategietactique_" + voletlbl.name;
                        desceffetspr.setAttribute("placeholder", "Description des effets espérés (veuillez préciser l'année de déscription)");
                        desceffetspr.setAttribute("id", "desceffetspr_");
                        desceffetspr.setAttribute("required", true);
                        desceffetspr.setAttribute("class", "form-control");
                        desceffetspr.style.marginTop = "4px";
                        desceffetspr.name = "descripeffetspr_" + voletlbl.name;
                        nbrTotalHist.setAttribute("placeholder", "Nombre total  d’histoire de succès à documenter (veuillez préciser l'année de documentation)");
                        nbrTotalHist.setAttribute("id", "nbrTotalHist_" + divvoletcount);
                        nbrTotalHist.setAttribute("required", true);
                        nbrTotalHist.setAttribute("class", "form-control");
                        nbrTotalHist.setAttribute("type", "number");
                        nbrTotalHist.style.marginTop = "4px";
                        nbrTotalHist.name = "nombreTotalHist_" + voletlbl.name;
                        enumPersonnelCle.setAttribute("placeholder", "Enumérez le personnel clé et le nombre de jours de travail")
                        enumPersonnelCle.setAttribute("id", "enumPersonnelCle_" + divvoletcount);
                        enumPersonnelCle.setAttribute("required", true);
                        enumPersonnelCle.setAttribute("class", "form-control");
                        enumPersonnelCle.style.marginTop = "4px";
                        enumPersonnelCle.name = "enumererPersonnelCle_" + voletlbl.name;
                        boutonactivite.setAttribute("type", "button");
                        boutonactivite.setAttribute("id", "bouton_ajout_activite_" + divvoletcount);
                        boutonactivite.textContent = "Ajouter une activité";
                        boutonactivite.setAttribute("class", "bouton_activite_ajouter");
                        boutonactivite.setAttribute("class", "btn btn-primary w-25");
                        boutonactivite.style.marginTop = "3px";

                        divgestion.setAttribute("class", "divgestion");
                        divgestion.setAttribute("id", "divgestion_" + voletlbl.name);
                        divrisque.setAttribute("class", "divrisque");
                        divrisque.setAttribute("id", "divrisque_" + voletlbl.name)
                        labeldivgestion.setAttribute("class", "labeldivgestion");
                        labeldivgestion.textContent = "GESTION DES RISQUES";
                        bouttonrisque.setAttribute("id", "bouttonrisque_" + voletlbl.name);
                        bouttonrisque.textContent = "Ajouter une ligne";
                        bouttonrisque.setAttribute("class", "bouttonrisque");
                        bouttonrisque.setAttribute("class", "btn btn-primary w-25")
                        bouttonrisque.setAttribute("type", "button");
                        divactivite.setAttribute("id", "div_activite_" + voletlbl.name);

                        titrevolet.style.display = "flex";
                        titrevolet.style.flexDirection = "row";
                        titrevolet.appendChild(btntitrevolet);
                        titrevolet.appendChild(btnremovevolet);
                        divgestion.appendChild(labeldivgestion);
                        divgestion.appendChild(divrisque);
                        divgestion.appendChild(bouttonrisque);
                        divaccordionbody.appendChild(label);
                        divaccordionbody.appendChild(voletlbl);
                        divaccordionbody.appendChild(objlacvolet);
                        divaccordionbody.appendChild(objspecsmartvolet);
                        divaccordionbody.appendChild(strategietactique);
                        divaccordionbody.appendChild(desceffetspr);
                        divaccordionbody.appendChild(nbrTotalHist);
                        divaccordionbody.appendChild(enumPersonnelCle);
                        divaccordionbody.appendChild(divactivite);
                        divaccordionbody.appendChild(boutonactivite);
                        divaccordionbody.appendChild(divgestion);
                        divvoletcontains.appendChild(divaccordionbody);
                        divcontainervolet.appendChild(titrevolet);
                        divcontainervolet.appendChild(divvoletcontains);
                        divvolet.appendChild(divcontainervolet);
                        divvoletcontainerbase.appendChild(divvolet);

                        function createAp(){
                            var divactivite = document.createElement("div");
                            var divindiccontainer = document.createElement("div");
                            var label = document.createElement("label");
                            var buttonindic = document.createElement("button")
                            var designationactivite = document.createElement("input")
                            var responsableExec = document.createElement("input")
                            var indiccount = 1;
                            var btnremoveap = document.createElement("button");
                            divactivite.setAttribute("id", "div_activite_" + divactivitecount + "_" + voletlbl.name);
                            divactivite.setAttribute("class", "divactivite");
                            divindiccontainer.setAttribute("id", "div_indic_container_activite_" + divactivitecount + "_" + voletlbl.name);
                            label.textContent = "Activité " + divactivitecount;
                            label.style.color = "blue";
                            label.style.fontSize = "13pt";
                            designationactivite.setAttribute("id", "activite_" + divactivitecount);
                            designationactivite.setAttribute("class", "detail_activite");
                            designationactivite.setAttribute("required", true);
                            designationactivite.setAttribute("class", "form-control");
                            designationactivite.name = "activite_" + divactivitecount + "_" + voletlbl.name;
                            designationactivite.setAttribute("placeholder", "activité");
                            designationactivite.style.marginTop = "4px";
                            designationactivite.style.marginBottom = "4px";
                            responsableExec.setAttribute("id", "responsable_" + divactivitecount);
                            responsableExec.setAttribute("placeholder", "responsable d'exécution");
                            responsableExec.setAttribute("class", "detail_activite");
                            responsableExec.setAttribute("required", true);
                            responsableExec.setAttribute("class", "form-control");
                            responsableExec.style.marginBottom = "4px";
                            responsableExec.name = "responsable_" + designationactivite.name;
                            buttonindic.setAttribute("id", "indicbutton_" + designationactivite.name);
                            buttonindic.setAttribute("type", "button");
                            buttonindic.setAttribute("class", "detail_activite");
                            buttonindic.setAttribute("class", "btn btn-primary w-25");
                            buttonindic.style.marginBottom = "4px";
                            buttonindic.textContent = "Ajouter un/des indicateur/s pour cette activité";

                            btnremoveap.setAttribute("id", "btn_remove_ap_" + designationactivite.name);
                            btnremoveap.style.backgroundColor = "red";
                            btnremoveap.style.color = "white";
                            btnremoveap.style.border = "none";
                            btnremoveap.style.fontSize = "13px";
                            btnremoveap.style.borderRadius = "8px";
                            btnremoveap.textContent = "Rétirer";
                            btnremoveap.style.marginLeft = "5px";
                            btnremoveap.setAttribute("type", "button");

                            divactivite.style.backgroundColor = "#efefef";
                            divactivite.style.padding = "5px";
                            divactivite.style.marginTop = "9px";
                            divactivite.style.borderRadius = "5px";

                            var divactivit = document.getElementById("div_activite_" + voletlbl.name);
                            label.appendChild(btnremoveap);
                            divactivite.appendChild(label);
                            divactivite.appendChild(designationactivite);
                            divactivite.appendChild(responsableExec);
                            divactivite.appendChild(divindiccontainer);
                            divactivite.appendChild(buttonindic);
                            divactivit.appendChild(divactivite);

                            function deleteap(){
                                divactivite.remove();
                            }
                            var element = "btn_remove_ap_" + designationactivite.name;
                            var btnsupap = document.getElementById(element);
                            btnsupap.addEventListener("click", deleteap);
                            function createIndic(){
                                var btnremoveindic = document.createElement("button");
                                var divindic = document.createElement("div");
                                var indicateur = document.createElement("input");
                                var baseline = document.createElement("input");
                                var cible = document.createElement("input");
                                var sourcedesdonnees = document.createElement("input");
                                var frequence = document.createElement("input");
                                var divperiode = document.createElement("div");
                                var mois1 = document.createElement("input");
                                var mois2 = document.createElement("input");
                                var mois3 = document.createElement("input");
                                var mois4 = document.createElement("input");
                                var mois5 = document.createElement("input");
                                var mois6 = document.createElement("input");
                                var mois7 = document.createElement("input");
                                var mois8 = document.createElement("input");
                                var mois9 = document.createElement("input");
                                var mois10 = document.createElement("input");
                                var mois11 = document.createElement("input");
                                var mois12 = document.createElement("input");
                                var labelmois1 = document.createElement("label");
                                var labelmois2 = document.createElement("label");
                                var labelmois3 = document.createElement("label");
                                var labelmois4 = document.createElement("label");
                                var labelmois5 = document.createElement("label");
                                var labelmois6 = document.createElement("label");
                                var labelmois7 = document.createElement("label");
                                var labelmois8 = document.createElement("label");
                                var labelmois9 = document.createElement("label");
                                var labelmois10 = document.createElement("label");
                                var labelmois11 = document.createElement("label");
                                var labelmois12 = document.createElement("label");
                                var lbl = document.createElement("label")
                                var lblcountindic = document.createElement("label")

                                indicateur.setAttribute("id", "indicateur_" + indiccount);
                                indicateur.name = "indicateur_" + indiccount + "_" + designationactivite.name;
                                indicateur.setAttribute("class", "detail_activite_indic");
                                indicateur.setAttribute("placeholder", "Indicateurs standard de LAC asbl");
                                indicateur.setAttribute("class", "form-control");
                                indicateur.setAttribute("required", true);
                                indicateur.style.marginBottom = "6px";
                                baseline.setAttribute("id", "baseline_" + indiccount);
                                baseline.name = "baseline_" + indicateur.name;
                                baseline.setAttribute("placeholder", "Base line/GAP");
                                baseline.setAttribute("class", "detail_activite_indic");
                                baseline.setAttribute("class", "form-control");
                                baseline.setAttribute("required", true);
                                baseline.style.marginBottom = "6px";
                                divindic.style.backgroundColor = "#e0dfdf";
                                divindic.style.padding = "5px";
                                divindic.style.marginTop = "9px";
                                divindic.style.borderRadius = "5px";
                                cible.setAttribute("id", "cible_" + indiccount);
                                cible.name = "cible_" + indicateur.name;
                                cible.setAttribute("placeholder", "Cible (ou N/A)");
                                cible.setAttribute("class", "detail_activite_indic");
                                cible.setAttribute("class", "form-control");
                                cible.setAttribute("required", true);
                                cible.style.marginBottom = "6px";
                                sourcedesdonnees.setAttribute("id", "sourcedonnees_" + indiccount);
                                sourcedesdonnees.name = "sourcedesdonnees_" + indicateur.name;
                                sourcedesdonnees.setAttribute("placeholder", "Source des données y compris l’outil utilisé");
                                sourcedesdonnees.setAttribute("class", "detail_activite_indic");
                                sourcedesdonnees.setAttribute("class", "form-control");
                                sourcedesdonnees.setAttribute("required", true);
                                sourcedesdonnees.style.marginBottom = "6px";
                                frequence.setAttribute("id", "frequence_" + indiccount);
                                frequence.name = "frequence_" + indicateur.name;
                                frequence.setAttribute("placeholder", "Fréquence de la collecte");
                                frequence.setAttribute("class", "detail_activite_indic");
                                frequence.setAttribute("class", "form-control");
                                frequence.setAttribute("required", true);
                                frequence.style.marginBottom = "6px";

                                mois1.setAttribute("type", "checkbox");
                                mois1.setAttribute("id", "id_mois_" + indiccount);
                                mois1.style.marginRight = "6px";
                                mois1.name = "periode_" + indicateur.name;
                                mois1.value = "janvier";
                                mois2.setAttribute("type", "checkbox");
                                mois2.style.marginRight = "6px";
                                mois2.name = "periode_" + indicateur.name;
                                mois2.value = "février";
                                mois3.setAttribute("type", "checkbox");
                                mois3.style.marginRight = "6px";
                                mois3.name = "periode_" + indicateur.name;
                                mois3.value = "mars";
                                mois4.setAttribute("type", "checkbox");
                                mois4.style.marginRight = "6px";
                                mois4.name = "periode_" + indicateur.name;
                                mois4.value = "avril";
                                mois5.setAttribute("type", "checkbox");
                                mois5.style.marginRight = "6px";
                                mois5.name = "periode_" + indicateur.name;
                                mois5.name = "mai";
                                mois6.setAttribute("type", "checkbox");
                                mois6.style.marginRight = "6px";
                                mois6.name = "periode_" + indicateur.name;
                                mois6.value = "juin";
                                mois7.setAttribute("type", "checkbox");
                                mois7.style.marginRight = "6px";
                                mois7.name = "periode_" + indicateur.name;
                                mois7.value = "juillet";
                                mois8.setAttribute("type", "checkbox");
                                mois8.style.marginRight = "6px";
                                mois8.name = "periode_" + indicateur.name;
                                mois8.value = "août";
                                mois9.setAttribute("type", "checkbox");
                                mois9.style.marginRight = "6px";
                                mois9.name = "periode_" + indicateur.name;
                                mois9.value = "septembre";
                                mois10.setAttribute("type", "checkbox");
                                mois10.style.marginRight = "6px";
                                mois10.name = "periode_" + indicateur.name;
                                mois10.value = "octobre";
                                mois11.setAttribute("type", "checkbox");
                                mois11.style.marginRight = "6px";
                                mois11.name = "periode_" + indicateur.name;
                                mois11.value = "novembre";
                                mois12.setAttribute("type", "checkbox");
                                mois12.style.marginRight = "6px";
                                mois12.name = "periode_" + indicateur.name;
                                mois12.value = "décembre";

                                labelmois1.setAttribute("for", "id_mois_1");
                                labelmois1.setAttribute("class", "form-check");
                                labelmois1.textContent = "Janvier ";
                                labelmois2.setAttribute("for", "id_mois_2");
                                labelmois2.setAttribute("class", "form-check");
                                labelmois2.textContent = "Février ";
                                labelmois3.setAttribute("for", "id_mois_3");
                                labelmois3.setAttribute("class", "form-check");
                                labelmois3.textContent = "Mars ";
                                labelmois4.setAttribute("for", "id_mois_4");
                                labelmois4.setAttribute("class", "form-check");
                                labelmois4.textContent = "Avril ";
                                labelmois5.setAttribute("for", "id_mois_5");
                                labelmois5.setAttribute("class", "form-check");
                                labelmois5.textContent = "Mai ";
                                labelmois6.setAttribute("for", "id_mois_6");
                                labelmois6.setAttribute("class", "form-check");
                                labelmois6.textContent = "Juin ";
                                labelmois7.setAttribute("for", "id_mois_7");
                                labelmois7.setAttribute("class", "form-check");
                                labelmois7.textContent = "Juillet ";
                                labelmois8.setAttribute("for", "id_mois_8");
                                labelmois8.setAttribute("class", "form-check");
                                labelmois8.textContent = "Aout ";
                                labelmois9.setAttribute("for", "id_mois_9");
                                labelmois9.setAttribute("class", "form-check");
                                labelmois9.textContent = "Septembre ";
                                labelmois10.setAttribute("for", "id_mois_10");
                                labelmois10.setAttribute("class", "form-check");
                                labelmois10.textContent = "Octobre ";
                                labelmois11.setAttribute("for", "id_mois_11");
                                labelmois11.setAttribute("class", "form-check");
                                labelmois11.textContent = "Novembre ";
                                labelmois12.setAttribute("for", "id_mois_12");
                                labelmois12.setAttribute("class", "form-check");
                                labelmois12.textContent = "Décembre ";

                                divperiode.setAttribute("class", "div_periode");
                                lbl.textContent = "Période";
                                lblcountindic.textContent = "Indicateur " + indiccount;
                                lblcountindic.style.color = "teal";
                                lblcountindic.style.fontSize = "13pt";
                                lbl.setAttribute("class", "lblperiode");
                                lbl.style.color = "white";
                                lbl.style.backgroundColor = "black";
                                lbl.style.borderRadius = "8px";
                                lbl.style.padding = "3px";
                                divindic.setAttribute("id", "div_indic_" + indicateur.name);
                                btnremoveindic.style.backgroundColor = "red";
                                btnremoveindic.style.color = "white";
                                btnremoveindic.style.border = "none";
                                btnremoveindic.style.fontSize = "13px";
                                btnremoveindic.style.borderRadius = "8px";
                                btnremoveindic.textContent = "Rétirer";
                                btnremoveindic.setAttribute("id", "btn_remove_indic_" + indicateur.name);
                                btnremoveindic.setAttribute("type", "button");
                                btnremoveindic.style.marginLeft = "8px";

                                element = "div_indic_container_" + designationactivite.name;
                                var divindiccontainer = document.getElementById(element);
                                lblcountindic.appendChild(btnremoveindic);
                                divindic.appendChild(lblcountindic);
                                divindic.appendChild(indicateur);
                                divindic.appendChild(baseline);
                                divindic.appendChild(cible);
                                divindic.appendChild(sourcedesdonnees);
                                divindic.appendChild(frequence);
                                divindic.appendChild(lbl);
                                labelmois1.appendChild(mois1);
                                labelmois2.appendChild(mois2);
                                labelmois3.appendChild(mois3);
                                labelmois4.appendChild(mois4);
                                labelmois5.appendChild(mois5);
                                labelmois6.appendChild(mois6);
                                labelmois7.appendChild(mois7);
                                labelmois8.appendChild(mois8);
                                labelmois9.appendChild(mois9);
                                labelmois10.appendChild(mois10);
                                labelmois11.appendChild(mois11);
                                labelmois12.appendChild(mois12);

                                divperiode.appendChild(labelmois1);
                                divperiode.appendChild(labelmois2);
                                divperiode.appendChild(labelmois3);
                                divperiode.appendChild(labelmois4);
                                divperiode.appendChild(labelmois5);
                                divperiode.appendChild(labelmois6);
                                divperiode.appendChild(labelmois7);
                                divperiode.appendChild(labelmois8);
                                divperiode.appendChild(labelmois9);
                                divperiode.appendChild(labelmois10);
                                divperiode.appendChild(labelmois11);
                                divperiode.appendChild(labelmois12);
                                divindic.appendChild(divperiode);
                                divindiccontainer.appendChild(divindic);

                                function deleteindic(){
                                    divindic.remove();
                                }
                                var element = "btn_remove_indic_" + indicateur.name;
                                var btnsupindic = document.getElementById(element);
                                btnsupindic.addEventListener("click", deleteindic);

                                indiccount++;
                            }
                            var element = "indicbutton_" + designationactivite.name;
                            var addindic = document.getElementById(element);
                            addindic.addEventListener("click", createIndic);
                            divactivitecount++;
                        }

                        function createRisque(){
                            var divrisque = document.createElement("div");
                            var desc = document.createElement("input");
                            var mesure = document.createElement("input");
                            var respons = document.createElement("input");
                            var saut = document.createElement("br")
                            var label = document.createElement("label")
                            var btnremoverisque = document.createElement("button");

                            desc.setAttribute("class", "form-control");
                            desc.setAttribute("placeholder", "Description de risque");
                            desc.style.marginBottom = "6px",
                            desc.name = "description_" + risquecount + "_" + voletlbl.name;
                            desc.setAttribute("required", true);
                            mesure.setAttribute("class", "form-control");
                            mesure.setAttribute("placeholder", "Mesure de mitigation correspondantes");
                            mesure.style.marginBottom = "6px"
                            mesure.name = "mesuremitigation_" + desc.name;
                            mesure.setAttribute("required", true);
                            divrisque.setAttribute("id", "divrisque_" + desc.name);
                            divrisque.style.marginBottom = "10px";
                            divrisque.style.marginTop = "10px";
                            respons.setAttribute("class", "form-control");
                            respons.setAttribute("placeholder", "Responsable  de prévention");
                            respons.style.marginBottom = "6px"
                            respons.name = "responsableprevention_" + desc.name;
                            respons.setAttribute("required", true);

                            btnremoverisque.setAttribute("id", "btn_remove_risque_" + desc.name);
                            btnremoverisque.style.backgroundColor = "red";
                            btnremoverisque.style.color = "white";
                            btnremoverisque.style.border = "none";
                            btnremoverisque.style.fontSize = "13px";
                            btnremoverisque.style.borderRadius = "8px";
                            btnremoverisque.textContent = "Rétirer";
                            btnremoverisque.style.marginLeft = "5px";
                            btnremoverisque.setAttribute("type", "button");


                            var divrisk = document.getElementById("divrisque_" + voletlbl.name);
                            label.textContent = risquecount + ". ";
                            label.appendChild(btnremoverisque);
                            divrisque.appendChild(label);
                            divrisque.appendChild(desc);
                            divrisque.appendChild(mesure);
                            divrisque.appendChild(respons)
                            divrisk.appendChild(divrisque);

                            function deleterisk(){
                                divrisque.remove();
                            }
                            var element = "btn_remove_risque_" + desc.name;
                            var btnsuprisque = document.getElementById(element);
                            btnsuprisque.addEventListener("click", deleterisk);

                            risquecount++;
                        }
                        function deletevolet(){
                            divvolet.remove();
                        }
                        var element = "btn_remove_" + voletlbl.name;
                        var btnsupvolet = document.getElementById(element);
                        btnsupvolet.addEventListener("click", deletevolet);

                        var elem = "bouttonrisque_" + voletlbl.name;
                        var addRisque = document.getElementById(elem);
                        addRisque.addEventListener("click", createRisque);

                        var element = "bouton_ajout_activite_" + divvoletcount;
                        var addactivite = document.getElementById(element);
                        addactivite.addEventListener("click", createAp);



                        divvoletcount++;

                    }else {
                        alert("Ce volet a déjà été ajouté");
                    }
                }
                var btnajoutervolet = document.getElementById("button_volet_domaine");
                btnajoutervolet.addEventListener("click", createVolet);
            }, error: function (xhr, status, error){
                console.log("Erreur: " + error);
                alert("une erreur est survenue lors du traitement de le requête: "+ error);
            }
    });
}
addButton.addEventListener("click", createDomaine);

