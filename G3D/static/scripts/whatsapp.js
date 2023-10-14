function verificarNumeroDeTelefone(numeroTelefone) {
    if (numeroTelefone.startsWith("55")) {
        return numeroTelefone;
    } else {
        return "55" + numeroTelefone;
    }
}

document.addEventListener("DOMContentLoaded", function () {
    // Recupere o valor do atributo de dados "telefone" do elemento
    const telefoneElement = document.getElementById("link-whatsapp");
    const telefone = telefoneElement.getAttribute("data-telefone");

    // Verifique o número de telefone e crie o link do WhatsApp
    const numeroVerificado = verificarNumeroDeTelefone(telefone);
    const linkWhatsApp = `https://api.whatsapp.com/send?phone=${numeroVerificado}`;

    // Crie um link e adicione-o ao elemento "link-whatsapp"
    const linkElement = document.createElement("a");
    linkElement.href = linkWhatsApp;
    linkElement.textContent = `${telefone}`;
    telefoneElement.appendChild(linkElement);
});