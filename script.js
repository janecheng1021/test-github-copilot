document.addEventListener('DOMContentLoaded', () => {
    console.log('GitHub Copilot Results Tracker Loaded');

    // Load project data dynamically from a JSON file
    fetch('projects.json')
        .then(response => response.json())
        .then(data => {
            const tableBody = document.querySelector('#dashboard tbody');
            tableBody.innerHTML = '';
            data.projects.forEach(project => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${project.name}</td>
                    <td>${project.status}</td>
                    <td>${project.progress}%</td>
                `;
                tableBody.appendChild(row);
            });
        })
        .catch(error => {
            console.error('Error loading project data:', error);
            const tableBody = document.querySelector('#dashboard tbody');
            tableBody.innerHTML = '<tr><td colspan="3">Failed to load data</td></tr>';
        });
});