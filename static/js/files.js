
function fetch_files(user) {
  send_message('/get_file_list', JSON.stringify({ user: user }),displayFiles);
}

function displayFiles(data) {
  files = data
  content = document.querySelector(".content");
  files.forEach((file, index) => {
    let article = document.createElement('p');
    const link = document.createElement('a');
    const span = document.createElement('span');
    const protocol = window.location.protocol;
    const host = window.location.host;
    let rootURL = `${protocol}//${host}`;
    rootURL = rootURL + `/open_file?user=wiltchamberian&resource_id=${file.guid}`;
    link.href = rootURL; 
    link.textContent = file.title;
    article.appendChild(link);
    article.classList.add('article-index');
    article.myGuid = file.guid;
    content.appendChild(article);
  });
}
