
function fetch_files(user_id){
  fetch('/get_files', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({ user_id: user_id })
  })
  .then(response => response.json())
  .then(data => {
      console.log('Received files:', data.files);
      // Process received .tex files, e.g., display them on the client side
      displayFiles(data.files);
  })
  .catch(error => console.error('Error fetching .tex files:', error));
}


function displayFiles(files) {
  var content = document.getElementById('content');
  files.forEach((data, index) => {
    let article = document.createElement('p');
    article.addEventListener('click', function() {
      // 点击时触发的操作
      alert('Paragraph clicked!');
    })
    article.classList.add('article-index');
    article.textContent = data.name;
    article.myGuid = data.guid;
    content.appendChild(article);
  });
  //just for test
  let article = document.createElement('p');
  article.classList.add('article-index');
  article.textContent = "\(E=mc^2\)";
  content.appendChild(article);
}
