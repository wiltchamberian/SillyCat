
function o2j(js_object) {
  return JSON.stringify(js_object);
}

function send_message(name, js_string, func) {
  fetch(name, {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: js_string
})
.then(response => response.json())//here is a javascript object
.then(data => {
  func(data);
})
.catch(error => console.error('Error fetching', error));
}