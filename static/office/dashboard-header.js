i = true;
window.addEventListener("load",$e => {
	menu = document.getElementById("user_menu")
	destination_menu = document.getElementById("arrow_image")
	x = destination_menu.getBoundingClientRect().x
	y = destination_menu.getBoundingClientRect().y
	menu.style.transform = "translate("+(x)+"px,"+(y+30)+"px)"
})
window.addEventListener('click',$e => {
	arrow = document.getElementById("arrow-profil")
	x = destination_menu.getBoundingClientRect().x
	y = destination_menu.getBoundingClientRect().y
	if($e.srcElement.id == 'arrow_image'){
		if(i == false){
			$e.srcElement.style = "transform:rotateZ(0deg);width:30px; height: 30px;"
			menu.style.transform = "translate("+(x)+"px,"+(y+30)+"px)"
			menu.style = "visibility:hidden"
			i = true
		}else{
			i = false
			$e.srcElement.style = "transform:rotateZ(90deg);width:30px; height: 30px;"
			menu.style = "visibility:visible"
			menu.style.transform = "translate("+(x)+"px,"+(y+30)+"px)"
		}
		
	}
	
})