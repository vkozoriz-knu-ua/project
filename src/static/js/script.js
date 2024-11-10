const map = L.map('map').setView([50.45, 30.52], 6);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 18,
}).addTo(map);

fetch('/api')
    .then(response => response.json())
    .then(data => {
        data.forEach(person => {
            L.marker([person.latitude, person.longitude]).addTo(map)
                .bindPopup(`
                    <h3>${person.name}</h3>
                    <img src="${person.thumbnail}" alt="${person.name}" style="width:100px;">
                    <p>${person.abstract}</p>
                `);
        });
    });
