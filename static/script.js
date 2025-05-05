// Dashboard Admin - Grafik Pemasukan Bulanan
document.addEventListener('DOMContentLoaded', function () {
    if (document.getElementById('grafikPemasukan')) {
        var ctx = document.getElementById('grafikPemasukan').getContext('2d');
        var labels = JSON.parse(document.getElementById('grafikPemasukan').getAttribute('data-labels'));
        var data = JSON.parse(document.getElementById('grafikPemasukan').getAttribute('data-data'));

        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Total Pemasukan Bulanan',
                    backgroundColor: '#2e7d32',
                    borderColor: '#2e7d32',
                    data: data
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    }
});

// Dashboard Rekap Tahunan - Grafik
if (document.getElementById('grafikTahunan')) {
    var ctx2 = document.getElementById('grafikTahunan').getContext('2d');
    var labels2 = JSON.parse(document.getElementById('grafikTahunan').getAttribute('data-labels'));
    var data2 = JSON.parse(document.getElementById('grafikTahunan').getAttribute('data-data'));

    new Chart(ctx2, {
        type: 'bar',
        data: {
            labels: labels2,
            datasets: [{
                label: 'Total Pemasukan Bulanan',
                backgroundColor: '#4caf50',
                borderColor: '#2e7d32',
                data: data2
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

function renderGrafikBulanan(labels, data) {
    const canvas = document.getElementById('grafikBulanan');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Pemasukan',
                data: data,
                backgroundColor: '#4caf50'
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

document.addEventListener('DOMContentLoaded', function () {
    const canvas = document.getElementById('grafikBulanan');
    if (!canvas) return;

    const labels = JSON.parse(canvas.dataset.labels || '[]');
    const values = JSON.parse(canvas.dataset.values || '[]');

    const ctx = canvas.getContext('2d');
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Pemasukan',
                data: values,
                backgroundColor: '#4caf50'
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
});


document.getElementById('santri_search').addEventListener('input', async function () {
    const query = this.value;
    const res = await fetch(`/cari_santri?q=${encodeURIComponent(query)}`);
    const data = await res.json();

    const resultsContainer = document.getElementById('santri_results');
    resultsContainer.innerHTML = '';
    data.forEach(item => {
        const div = document.createElement('div');
        div.className = 'search-item';
        div.textContent = item.label;
        div.addEventListener('click', () => {
            document.getElementById('santri_search').value = item.label;
            document.getElementById('id_santri').value = item.id;
            resultsContainer.innerHTML = '';
        });
        resultsContainer.appendChild(div);
    });
});
