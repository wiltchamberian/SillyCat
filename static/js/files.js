
function fetch_files(user_id) {
  send_message('/get_files', JSON.stringify({ user_id: user_id }),displayFiles);
}

function displayFiles(data) {
  files = data.files
  var content = document.getElementById('content');
  files.forEach((data, index) => {
    let article = document.createElement('p');
    article.addEventListener('click', function () {
      js = JSON.stringify({
        "guid": data.guid
      });
      send_message('open_file', js, function (data) {
        
      })
    })
    article.classList.add('article-index');
    article.textContent = data.name;
    //alert(data.name);
    article.myGuid = data.guid;
    content.appendChild(article);
  });
}
