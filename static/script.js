show_hint();

function show_hint(){
  setTimeout(function(){
    // 顯示item 開始動畫
    // document.getElementById("hint").style.visibility = "visible";
    const element = document.querySelector(".hint");
    element.style.visibility = "visible";
    element.classList.add('animate__animated', 'animate__fadeInRight');
    element.style.setProperty('--animate-duration', '1.5s');
  }, 2000);
}