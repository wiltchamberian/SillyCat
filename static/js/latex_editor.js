window.onload = function () {
  // Initialize CodeMirror editor
  let textArea = document.getElementById("editor");
  textArea.value = "";
  var editor = CodeMirror.fromTextArea(textArea, {
    lineNumbers: true,
    mode: "xml",
    theme: "material",
  });
  editor.setCursor({ line: 0, ch: 0 });
  editor.setSize(null, 400);

  // 添加滚动事件监听器
  textArea.addEventListener("scroll", function () {
    renderMath(editor);
  });
  editor.on("scroll", function () {
    renderMath(editor);
  });

  var outputDiv = document.getElementById("mathjax-container");
  outputDiv.style.lineHeight = editor.defaultTextHeight() + "px";

  editor.on("change", function (instance, changeObj) {
    renderMath(editor);
    if (changeObj.origin === "+input" && changeObj.text[0] === "") {
      renderMath(editor);
    }
  });

var btn = document.getElementById("export");
btn.addEventListener('mouseup', handleRelease);
function handleRelease(){
var textRange = getRangeText(editor);
var mathjaxContent =convertLatexToMathJax(textRange);
var tempHTML = createTempHTML(mathjaxContent);
console.log(tempHTML);
convertHTMLToPDF(tempHTML, 'mathjax_result.pdf');
}

  // Initial rendering
  renderMath(editor);
}

function getRangeText(editor) {
  let sci = editor.getScrollInfo();
  let startLine = editor.lineAtHeight(sci.top, "local");
  let endLine = editor.lineAtHeight(sci.top + sci.clientHeight, "local");
  console.log("lineNumber:%s",endLine-startLine);
  var textRange = editor.getRange({ line: startLine, ch: 0 }, { line: endLine, ch: 0 });
  return textRange;
}

function renderMath(editor) {
  var textRange = getRangeText(editor);

  var outputDiv = document.getElementById("mathjax-container");
  outputDiv.innerHTML =convertLatexToMathJax(textRange);

  MathJax.typesetPromise([outputDiv]).catch(function (err) {
    console.error("Error during MathJax typesetting: " + err.message);
  });
}

function convertMathJaxToLatex(text) {
  return text.replace(/\\\(/g, '$').replace(/\\\)/g, '$');
}

function convertLatexToMathJax(text) {
  // 使用正则表达式将每一对 $...$ 替换为 \(...\)
  return text.replace(/\$(.*?)\$/g, '\\($1\\)');
}

// 创建一个包含 MathJax 渲染内容的临时 HTML 文件
function createTempHTML(mathjaxContent) {
var tempHTML = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>MathJax to PDF</title><link rel="stylesheet" href="styles.css"></head><body>';
tempHTML += '<div class="mathjax-content">' + mathjaxContent + '</div>';
tempHTML += '</body></html>';
return tempHTML;
}

// 将临时 HTML 文件转换为 PDF
function convertHTMLToPDF(htmlContent, filename) {
// 使用 Blob 对象创建临时 HTML 文件
var blob = new Blob([htmlContent], { type: 'text/html' });

// 创建一个下载链接
var link = document.createElement('a');
link.href = URL.createObjectURL(blob);
link.download = filename || 'mathjax_result.pdf';

// 将下载链接添加到文档中，并触发点击事件
document.body.appendChild(link);
link.click();

// 移除下载链接
document.body.removeChild(link);
}
