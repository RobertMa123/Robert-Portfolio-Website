document.addEventListener("DOMContentLoaded", () => {
    loadProjects();

    const form = document.getElementById("contactForm");
    form.addEventListener("submit", async (e) => {
        e.preventDefault();
        const formData = new FormData(form);
        const response = await fetch("/contact", {
            method: "POST",
            body: JSON.stringify({
                name: formData.get("name"),
                email: formData.get("email"),
                message: formData.get("message")
            }),
            headers: {
                "Content-Type": "application/json"
            }
        });
        const result = await response.json();
        alert(result.message);
    });
});

async function loadProjects() {
    const response = await fetch("/api/projects");
    const projects = await response.json();
    const projectList = document.querySelector(".project-list");
    projectList.innerHTML = projects.map(project => `
        <div class="project">
            <h3>${project.name}</h3>
            <p>${project.description}</p>
        </div>
    `).join("");
}
