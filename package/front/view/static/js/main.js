function autoRefresh(interval) {
	setTimeout("atualizar();",interval);
}
function atualizar() {
  window.location.reload();
}

var i = setInterval(function () {
    clearInterval(i);
    document.getElementById("loading").style.display = "none";
    document.getElementById("conteudo").style.display = "inline";

}, 2300);