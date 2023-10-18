// function ajouter(){
//     $(document).ready(function () {
//         var objglob = $('#text').val();
//         $.ajax({
//             url:'ajouter',
//             data:{
//                 'objglob':objglob
//             },
//             dataType:'json',
//     })
//         alert('Ajouté')
// })
// }

function chargerVolet(){
    $(document).ready(function () {
        var url = window.location.href;
        var idprojet = url.split('/')[url.split('/').length-1];
        var volet = $('#volet').val();
        var domaine = $('#domaine').val();
        $.ajax({
            url:'ajout_domaine_volet',
            data:{
                'domaine':domaine,
                'volet': volet,
                'idprojet': idprojet,
            },
            dataType:'json',
            success: function (data) {
                msg = data['success'];
                if (msg == "ajouté") {
                    $('#div_objectifglobal').css("display", "unset")
                }else {
                    if (msg != "ajouté")
                        alert(msg)
                    $('#div_objectifglobal').css("display", "unset")
                }

            }
    })
})
}

function ajouteglob(){
    $(document).ready(function () {
        var url = window.location.href;
        var idprojet = url.split('/')[url.split('/').length-1];
        var domaine = $('#domaine').val();
        var volet = $('#volet').val();
        var objglob = $('#objglob').val();

        $.ajax({
            url:'ajouter_glob',
            data:{
                'objglob':objglob,
                'volet': volet,
                'idprojet': idprojet,
                'domaine': domaine,
            },
            dataType:'json',
            success: function (data) {
                $("#objglob").val("");
                var obj = $("#objglobaux");
                obj.append($('<option>').text(objglob))
            }
    })
})
}


function afficherObjspec(){
    $(document).ready(function () {
        $("#div_objectifspecifique").css("display", "unset")
    })
}


function ajoutspec(){
    $(document).ready(function (){
        var url = window.location.href;
        var idprojet = url.split('/')[url.split('/').length-1];
        var domaine = $('#domaine').val();
        var volet = $('#volet').val();
        var objglob = $('#objglobaux').val();
        var objspec = $('#objspec').val();
        $.ajax({
            url:'ajouter_spec',
            data:{
                'objglob':objglob,
                'objspec': objspec,
                'idprojet': idprojet,
                'domaine': domaine,
                'volet': volet,
            },
            dataType:'json',
            success: function (data) {
                $("#objspec").val("");
                var obj = $("#objspecifique");
                obj.append($('<option>').text(objspec))
            }
        })
   })
}


function afficherActPrincipale(){
    $(document).ready(function () {
        $("#div_activiteprincipale").css("display", "unset")
    })
}


function ajoutActivitePrincipale(){
    $(document).ready(function (){
        var url = window.location.href;
        var idprojet = url.split('/')[url.split('/').length-1];
        var domaine = $('#domaine').val();
        var volet = $('#volet').val();
        var objspec = $('#objspecifique').val();
        var actprincipale = $('#actprincipale').val();
        $.ajax({
            url:'ajouter_activiteprincipale',
            data:{
                'objspec':objspec,
                'actprincipale': actprincipale,
                'idprojet': idprojet,
                'domaine': domaine,
                'volet': volet,
            },
            dataType:'json',
            success: function (data) {
                $("#actprincipale").val("");
                var obj = $("#activiteprincipale");
                obj.append($('<option>').text(actprincipale))
            }
        })
   })
}


function affichersousactivite(){
    $(document).ready(function () {
        $("#div_sousactivite").css("display", "unset")
    })
}


function ajoutSousAct(){
    $(document).ready(function (){
        var url = window.location.href;
        var idprojet = url.split('/')[url.split('/').length-1];
        var domaine = $('#domaine').val();
        var volet = $('#volet').val();
        var actprincipale = $('#activiteprincipale').val();
        var sousactivite = $('#sousactivite').val();
        var datedebut = $('#periodeDebut').val();
        var datefin = $('#periodeFin').val();

        $.ajax({
            url:'ajouter_sousactivite',
            data:{
                'actprincipale': actprincipale,
                'sousactivite': sousactivite,
                'datedebut': datedebut,
                'datefin': datefin,
                'idprojet': idprojet,
                'domaine': domaine,
                'volet': volet,
            },
            dataType:'json',
            success: function (data) {
                $("#sousactivite").val("");
            }
        })
   })
}


function afficherDetail(){
    $(document).ready(function (){
        var url = window.location.href;
        var idprojet = url.split('/')[url.split('/').length-1];
        var domaine = $('#domaine').val();
        var volet = $('#volet').val();
        var actprincipale = $('#activiteprincipale').val();
        var sousactivite = $('#sousactivite').val();
        var datedebut = $('#periodeDebut').val();
        var datefin = $('#periodeFin').val();

        $.ajax({
            url:'ajouter_sousactivite',
            data:{
                'actprincipale': actprincipale,
                'sousactivite': sousactivite,
                'datedebut': datedebut,
                'datefin': datefin,
                'idprojet': idprojet,
                'domaine': domaine,
                'volet': volet,
            },
            dataType:'json',
            success: function (data) {
                $("#sousactivite").val("");
            }
        })
   })
}