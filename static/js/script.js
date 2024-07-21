// function loadPage(page) {
//   document.getElementById('content').innerHTML = data;
//   fetch(page + '.html')
//       .then(response => response.text())
//       .then(data => {
//           document.getElementById('content').innerHTML = data;
//       })
//       .catch(error => console.error('Error loading page: ', error));
// }

function loadPage(page) {
  var xhr = new XMLHttpRequest();
  xhr.open('GET', page + '.html', true);

  xhr.onload = function() {
      if (xhr.status >= 200 && xhr.status < 400) {
          document.getElementById('content').innerHTML = xhr.responseText;
      } else {
          console.error('Error loading page. Status:', xhr.status);
      }
  };

  xhr.onerror = function() {
      console.error('Request failed');
  };

  xhr.send();
}
