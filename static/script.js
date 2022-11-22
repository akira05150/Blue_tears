show_hint();
icons_hint();

function show_hint(){
  setTimeout(function(){
    // 顯示item 開始動畫
    // document.getElementById("hint").style.visibility = "visible";
    const element = document.querySelector(".hint");
    element.style.visibility = "visible";
    element.classList.add('animate__animated', 'animate__fadeInRight');
    element.style.setProperty('--animate-duration', '1.0s');
  }, 2000);
}

function change_temperature(temp){
    const element = document.getElementById("temperature");
    element.innerHTML = temp + "&deg;C";
}

function change_wind(direction){
  const element = document.getElementById("wind_direction");
  element.innerHTML = direction;
}

function icons_hint(){
  setTimeout(function(){
    var icons = ["icon_anemoscope", "icon_compass", "icon_thermometer"];

    for(var i = 0; i < icons.length; i++){
      const element = document.getElementById(icons[i]);
      element.classList.add('animate__animated', 'animate__bounce');
      element.style.setProperty('--animate-duration', '1.0s');
    }
    
  }, 2000);
}
