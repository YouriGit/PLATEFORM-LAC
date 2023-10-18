// $('document').ready(function () {
//     // $('#soumettre')[0].style = 'display:none'
//     var volet = $('#volet')
//     for(i=1; i < volet[0].length; i++){
//         volet[0][i].style = 'display:none'
//     }
//     $('#domaine').on('change',function (e) {
//         volet[0].selectedIndex = 0
//         if($(this)[0].selectedIndex == 0 || volet[0].selectedIndex == 0){
//             $('#soumettre')[0].style = 'display:none'
//         }else {
//             $('#soumettre')[0].style = 'display:unset'
//         }
//         e.preventDefault();
//         for(i=1; i < 11; i++){
//             if(volet[0][i].className == $(this)[0].value){
//                 volet[0][i].style = 'display:unset'
//             }
//             else {
//                 volet[0][i].style = 'display:none'
//             }
//
//         }
//     })
//     $('#volet').on('change',function (e) {
//         e.preventDefault();
//         if($(this)[0].selectedIndex == 0){
//             $('#soumettre')[0].style = 'display : none'
//         }else{
//             $('#soumettre')[0].style = 'display : unset'
//         }
//     })
// })
