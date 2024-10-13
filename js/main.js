// const prefersDarkScheme = window.matchMedia('(prefers-color-scheme: dark)');
// prefersDarkScheme.addEventListener("change", e => e.matches && enableDark());

function enableDark() {
    document.documentElement.style.setProperty('--BGCOLOR', '#202224');
    document.documentElement.style.setProperty('--HEADER-BGCOLOR', '#90b0d8');
    document.documentElement.style.setProperty('--HEADER-FONT-COLOR', '#202224');
    document.documentElement.style.setProperty('--FONT-COLOR', '#e2dfda');
    document.documentElement.style.setProperty('--FONT-DIM', '#959493');
    document.documentElement.style.setProperty('--LINK-COLOR', '#90b0d8');
    document.documentElement.style.setProperty('--LINK-HOVER', 'rgba(34, 108, 224, 0.6)');
    document.documentElement.style.setProperty('--LINK-ACTIVE', '#1b998b');
    document.getElementById('darkmode').checked = true;
};

function enableLight() {
    document.documentElement.style.setProperty('--BGCOLOR', 'whitesmoke');
    document.documentElement.style.setProperty('--HEADER-BGCOLOR', '#2a3b7a');
    document.documentElement.style.setProperty('--HEADER-FONT-COLOR', 'whitesmoke');
    document.documentElement.style.setProperty('--FONT-COLOR', '#000000');
    document.documentElement.style.setProperty('--FONT-DIM', '#00000098');
    document.documentElement.style.setProperty('--LINK-COLOR', '#2a3b7a');
    document.documentElement.style.setProperty('--LINK-HOVER', 'rgba(34, 108, 224, 0.6)');
    document.documentElement.style.setProperty('--LINK-ACTIVE', '#1b998b');
    document.getElementById('darkmode').checked = false;
};

addEventListener("change", function() {
    if (document.getElementById("darkmode").checked) {
        enableDark();
        console.log("Darkmode enabled");
    }
    else {
        enableLight();
        console.log("Lightmode enabled");
    }
});


if (window.matchMedia) {
    // Check if the dark-mode Media-Query matches
    if(window.matchMedia('(prefers-color-scheme: dark)').matches){
      // Dark
      enableDark();
    } else {
      // Light
      enableLight();
    }
  } else {
    // Default (when Media-Queries are not supported)
    enableLight();
  }