hljs.highlightAll();

const navBarToggleBtn = document.getElementById("navbar-toggle-btn");
const navBar = document.getElementById("navbar-sticky");

navBarToggleBtn.addEventListener("click", () => {
  navBar.classList.toggle("sm:hidden");
});

document.querySelectorAll("ul li a").forEach((navLink) => {
  if (navLink.getAttribute("href") === window.location.pathname) {
    navLink.classList.add("md:text-blue-700", "text-white", "bg-blue-700");
  }
});
