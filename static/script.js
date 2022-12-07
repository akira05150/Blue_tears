// icons_hint();

var conditions = ['sunset', 'lighthouse', 'wind', 'pray', 'reverse'];
var descriptions = ['每年4-6月時馬祖島嶼海域，海面上會產生冷光面板一樣的藍光，也被稱為「藍眼淚」<br><br>適合觀賞的地點，都是沒有光害，光線昏暗的海岸<br>'
                  , '夜幕降臨，可以做出開關的手勢，讓燈塔發光'
                  , '在馬祖當南面海邊或澳口吹起南風，海面波浪翻滾使夜光蟲產生微弱的藍光，即為藍眼淚'
                  , '現在請將燈塔關上，雙手比愛心代表誠心祈禱，等待藍眼淚的出現'
                  , '等待太陽倒轉'];
var gestures = ['../static/images/sunset.jpg'
              , '../static/images/smallhand.gif'
              , '../static/images/anemoscope.png'
              , '../static/images/heart.jpg'
              , '../static/images/reverse.png'];
var hints = ['請調整(哪邊的)旋鈕，讓太陽下山'
           , ''
           , '請調整(哪邊的)旋鈕，轉動風向至南風'
           , '慢慢靠近畫作，更近距離地欣賞藍眼淚吧！'
           , ''];

var precondition = "sunrise";

// show animations
function show_description(data){
  setTimeout(function(){
    // 修改文案
    const element = document.getElementById("description");
    element.innerHTML = data;

    // 顯示item 開始動畫
    element.style.visibility = "visible";
    element.classList.add('animate__animated', 'animate__fadeInDown');
    element.style.setProperty('--animate-duration', '1.0s');
  }, 500);
}

function show_gesture(pics){
  setTimeout(function(){
    // 修改圖片
    const element = document.getElementById("gesture");
    element.src = pics;

    // 顯示item 開始動畫
    element.style.visibility = "visible";
    element.classList.add('animate__animated', 'animate__fadeIn');
    element.style.setProperty('--animate-duration', '1.0s');
  }, 1500);
}

function show_hint(data){
  setTimeout(function(){
    // 修改文案
    const text = document.getElementById("hint_text");
    text.innerHTML = data;

    // 顯示item 開始動畫
    const element = document.querySelector(".hint");
    element.style.visibility = "visible";
    element.classList.add('animate__animated', 'animate__fadeIn');
    element.style.setProperty('--animate-duration', '1.0s');
  }, 2500);
}

// remove animations
function remove_hint_animation(){
  const element = document.querySelector(".hint");
  element.style.visibility = "hidden";
  element.classList.remove('animate__animated', 'animate__fadeIn');
  element.style.removeProperty('--animate-duration', '1.0s');
  void element.offsetWidth;
}

function remove_description_animation(){
  const element = document.getElementById("description");
  element.style.visibility = "hidden";
  element.classList.remove('animate__animated', 'animate__fadeInDown');
  element.style.removeProperty('--animate-duration', '1.0s');
  void element.offsetWidth;
}

function remove_gesture_animation(){
  const element = document.getElementById("gesture");
  element.style.visibility = "hidden";
  element.classList.remove('animate__animated', 'animate__fadeIn');
  element.style.removeProperty('--animate-duration', '1.0s');
  void element.offsetWidth;
}


// function change_wind(direction){
//   const element = document.getElementById("wind_direction");
//   element.innerHTML = direction;
// }

// function icons_hint(){
//   setTimeout(function(){
//     var icons = ["icon_anemoscope", "icon_compass"];

//     for(var i = 0; i < icons.length; i++){
//       const element = document.getElementById(icons[i]);
//       element.classList.add('animate__animated', 'animate__bounce');
//       element.style.setProperty('--animate-duration', '1.0s');
//     }
    
//   }, 1500);
// }

function update_page(){
  $.get("/update", function(condition){

    if (condition != precondition){
      console.log("changed to: " + condition);
      console.log("pre:" + precondition);
      remove_description_animation();
      remove_gesture_animation();
      remove_hint_animation();

      switch (condition){
        case "sunset":
          show_description(descriptions[0]);
          show_gesture(gestures[0]);
          show_hint(hints[0]);
          break;
        case "lighthouse":
          show_description(descriptions[1]);
          show_gesture(gestures[1]);
          // show_hint(hints[0]);
          break;
        case "wind":
          show_description(descriptions[2]);
          show_gesture(gestures[2]);
          show_hint(hints[2]);
          break;
        case "pray":
          show_description(descriptions[3]);
          show_gesture(gestures[3]);
          show_hint(hints[3]);
          break;
        case "reverse":
          show_description(descriptions[4]);
          // show_gesture(gestures[4]);
          // show_hint(hints[0]);
          break;
        default:
          remove_description_animation();
          remove_gesture_animation();
          remove_hint_animation();
          break;
      }
      precondition = condition;
    } 
  });
}

update_page();
var intervalId = setInterval(function() {
  update_page();
}, 1000);