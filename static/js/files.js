
function fetch_files(user_id) {
  send_message('/get_files', JSON.stringify({ user_id: user_id }),displayFiles);
}

function displayFiles(data) {
  files = data.files
  var content = document.getElementById('content');
  files.forEach((file, index) => {
    let article = document.createElement('p');
    const link = document.createElement('a');
    const span = document.createElement('span');
    const protocol = window.location.protocol;
    const host = window.location.host;
    const rootURL = `${protocol}//${host}//open_file`;
    rootURL = rootURL + `//user=wiltchamberian&resource_id=${file.guid}`;
    link.href = rootURL; 
    link.textContent = file.name;
    article.appendChild(link);
    /* article.addEventListener('click', function () {
      js = JSON.stringify({
        user:"wiltchamberian",
        guid:file.guid,
      });
      send_message('open_file', js, function (data) {
        
      })
    })*/
    article.classList.add('article-index');
    

  
    //alert(data.name);
    article.myGuid = file.guid;
    content.appendChild(article);
  });
}
