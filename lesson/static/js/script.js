hljs.highlightAll();
document.querySelectorAll("ul li a").forEach((navLink) => {
  if (navLink.getAttribute("href") === window.location.pathname) {
    navLink.classList.add("md:text-blue-700");
  }
});
