let currentCategory = "all";
let currentSearch = "";

function renderCards() {
  const container = document.getElementById("projectGrid");
  const filtered = projectsData.filter(p => {
    const matchCat = (currentCategory === "all" || p.cat === currentCategory);
    const matchSearch = (p.name.toLowerCase().includes(currentSearch) || p.desc.toLowerCase().includes(currentSearch) || p.badge.toLowerCase().includes(currentSearch));
    return matchCat && matchSearch;
  });

  if (filtered.length === 0) {
    container.innerHTML = `<div style="grid-column:1/-1; text-align:center; color:#94a3b8; padding:3rem;">No repositories match the specified filter.</div>`;
    return;
  }

  container.innerHTML = filtered.map(p => `
    <div class="card">
      <div>
        <div class="card-header">
          <span class="card-tag">Project ${p.id} • ${p.cat}</span>
          <span class="badge">${p.badge}</span>
        </div>
        <h3 class="card-title" onclick="navigateTo('detail', '${p.id}')">${p.name}</h3>
        <p class="card-desc">${p.desc}</p>
        <div class="tech-pills">
          ${p.techStack.map(t => `<span class="tech-tag">${t}</span>`).join('')}
        </div>
      </div>
      <div class="card-actions">
        <a href="${p.web}" target="_blank" class="btn btn-primary">Live Web ↗</a>
        <button onclick="navigateTo('detail', '${p.id}')" class="btn btn-detail">Specs & API</button>
        <a href="${p.repo}" target="_blank" class="btn btn-secondary">GitHub →</a>
      </div>
    </div>
  `).join("");
}

function filterCategory(cat) {
  currentCategory = cat;
  document.querySelectorAll(".pill").forEach(el => el.classList.remove("active"));
  event.target.classList.add("active");
  renderCards();
}

function filterSearch(e) {
  currentSearch = e.target.value.toLowerCase();
  renderCards();
}

function showDetail(id) {
  const p = projectsData.find(item => item.id === id);
  if (!p) return;

  const detailContainer = document.getElementById("detailView");
  detailContainer.innerHTML = `
    <div class="detail-box">
      <div class="detail-header">
        <div>
          <span class="card-tag">Project ${p.id} • ${p.cat}</span>
          <h1 style="font-size:2rem; margin:0.25rem 0;">${p.name}</h1>
          <span class="badge">${p.badge}</span>
        </div>
        <button onclick="navigateTo('grid')" class="btn btn-secondary" style="max-width:140px;">← Back to Grid</button>
      </div>

      <div class="detail-grid">
        <div>
          <div class="section-title">Architectural Solution & Hardening</div>
          <p style="color:#cbd5e1; line-height:1.6; margin-bottom:1.25rem;">${p.desc}</p>
          
          <div class="section-title">Core Production Advancement</div>
          <p style="color:#38bdf8; font-weight:600; margin-bottom:1.5rem;">${p.keyFeature}</p>

          <div class="section-title">Target REST / WS Endpoints</div>
          <div class="code-block">
            ${p.endpoints.map(ep => `${ep}`).join("<br>")}
          </div>

          <div style="display:flex; gap:1rem; margin-top:2rem;">
            <a href="${p.web}" target="_blank" class="btn btn-primary">Launch Live Web Deployment ↗</a>
            <a href="${p.repo}" target="_blank" class="btn btn-secondary">Inspect Source on GitHub →</a>
          </div>
        </div>

        <div>
          <div class="section-title">Technology Ecosystem</div>
          <div class="tech-pills" style="margin-bottom:1.5rem;">
            ${p.techStack.map(t => `<span class="tech-tag" style="font-size:0.85rem; padding:0.4rem 0.75rem;">${t}</span>`).join('')}
          </div>

          <div class="section-title">Reliability & Observability Verified</div>
          <ul class="spec-list">
            <li>ACID / Persistence Layer Integrated</li>
            <li>Zero 404 URL / Method Mismatches</li>
            <li>W3C Compliant CORS Origin Protection</li>
            <li>100% Automated PyTest Assertion Pass</li>
          </ul>
        </div>
      </div>
    </div>
  `;
}

function navigateTo(view, param) {
  document.querySelectorAll(".page-view").forEach(v => v.classList.remove("active"));
  document.querySelectorAll(".nav-link").forEach(l => l.classList.remove("active"));

  if (view === "grid") {
    document.getElementById("gridView").classList.add("active");
    document.getElementById("navHome").classList.add("active");
    window.location.hash = "directory";
  } else if (view === "detail") {
    showDetail(param);
    document.getElementById("detailView").classList.add("active");
    window.location.hash = `project-${param}`;
  } else if (view === "about") {
    document.getElementById("aboutView").classList.add("active");
    document.getElementById("navAbout").classList.add("active");
    window.location.hash = "about";
  }
}

// Router Hash Listener
window.addEventListener("hashchange", () => {
  const hash = window.location.hash.replace("#", "");
  if (hash.startsWith("project-")) {
    const id = hash.replace("project-", "");
    navigateTo("detail", id);
  } else if (hash === "about") {
    navigateTo("about");
  } else {
    navigateTo("grid");
  }
});

window.addEventListener("DOMContentLoaded", () => {
  const hash = window.location.hash.replace("#", "");
  if (hash.startsWith("project-")) {
    navigateTo("detail", hash.replace("project-", ""));
  } else if (hash === "about") {
    navigateTo("about");
  } else {
    navigateTo("grid");
  }
  renderCards();
});
