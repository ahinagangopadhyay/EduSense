document.addEventListener("DOMContentLoaded", function () {
  const toggle = document.getElementById("themeToggle");
  const label = document.getElementById("modeLabel");
  const body = document.body;

  toggle.addEventListener("change", function () {
    body.classList.toggle("dark-mode");
    label.textContent = toggle.checked ? "🌙 Dark" : "🌞 Light";
  });
});
