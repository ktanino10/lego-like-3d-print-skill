const languageLinks = [...document.querySelectorAll("[data-language-link]")];
const sections = new Set([...document.querySelectorAll("a[id]")].map((anchor) => anchor.id));

for (const link of languageLinks) {
  link.dataset.pageUrl = link.href;
}

function keepRelatedSection() {
  const hash = sections.has(window.location.hash.slice(1)) ? window.location.hash : "";
  for (const link of languageLinks) {
    link.href = link.dataset.pageUrl + hash;
  }
}

keepRelatedSection();
window.addEventListener("hashchange", keepRelatedSection);
