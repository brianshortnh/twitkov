const dateOptions = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
const today  = new Date();
const dateElement = document.getElementById('date');

dateElement.innerHTML = today.toLocaleDateString("en-US", dateOptions);

function handleFormSubmit(e) {
  // Hide all stuff flagged
  var hideStuff = document.getElementsByClassName('hide-on-load');

  console.log(hideStuff);

  for (var i = 0; i < hideStuff.length; i++) {
    console.log('cow');
    hideStuff[i].style.display = 'none';
    hideStuff[i].hidden = true;
  }

  // Show spinner
  document.getElementById('loading').hidden = false;
}
