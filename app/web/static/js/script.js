// Função para esconder automaticamente mensagens flash após 4 segundos
setTimeout(() => {
    const flash = document.querySelector(".flash");
    if (flash) {
        flash.style.opacity = "0";
        setTimeout(() => flash.remove(), 600); // remove do DOM
    }
}, 4000);

// Alternância manual entre modo claro e escuro
const toggleBtn = document.querySelector("#toggle-dark");
if (toggleBtn) {
    toggleBtn.addEventListener("click", () => {
        document.body.classList.toggle("dark-mode");

        // Armazena a preferência no localStorage
        const isDark = document.body.classList.contains("dark-mode");
        localStorage.setItem("darkMode", isDark ? "on" : "off");
    });

    // Ao carregar a página, aplica o tema salvo
    window.addEventListener("DOMContentLoaded", () => {
        const savedMode = localStorage.getItem("darkMode");
        if (savedMode === "on") {
            document.body.classList.add("dark-mode");
        }
    });
}
