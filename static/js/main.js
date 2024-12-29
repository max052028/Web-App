// 搜索功能
async function searchCountry() {
    const country = document.getElementById('countrySearch').value;
    try {
        const response = await fetch(`/api/country/${country}`);
        const data = await response.json();
        
        // 顯示結果
        const resultsDiv = document.getElementById('results');
        resultsDiv.innerHTML = `
            <div class="stat-box">
                <h3>${data.country}</h3>
                <p>確診病例：${data.confirmed}</p>
                <p>死亡人數：${data.deaths}</p>
                <p>康復人數：${data.recovered}</p>
                <p>現存病例：${data.active}</p>
                <p>更新時間：${new Date(data.last_update).toLocaleString()}</p>
            </div>
        `;
    } catch (error) {
        console.error('Error:', error);
        // 顯示錯誤訊息給用戶
        document.getElementById('results').innerHTML = '<p>無法找到該國家的數據。請檢查國家名稱是否正確。</p>';
    }
}

// 載入圖表（在首頁）
async function loadGlobalChart() {
    if (!document.getElementById('globalChart')) return;
    
    try {
        const response = await fetch('/api/global-timeline');
        const data = await response.json();
        
        const ctx = document.getElementById('globalChart').getContext('2d');
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: data.dates,
                datasets: [{
                    label: '確診病例',
                    data: data.confirmed,
                    borderColor: '#007bff',
                    fill: false
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
    } catch (error) {
        console.error('Error:', error);
    }
}

// 頁面載入時執行
document.addEventListener('DOMContentLoaded', () => {
    loadGlobalChart();
});
