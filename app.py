from flask import Flask, render_template, jsonify, request
from database import Database

app = Flask(__name__)

# MySQL配置
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Max#052028'
app.config['MYSQL_DB'] = 'covid19_data'

# 初始化數據庫
db = Database(app)

@app.route('/')
def home():
    # 獲取全球數據
    global_data = db.get_global_stats()
    return render_template('index.html', data=global_data)

@app.route('/search')
def search():
    # 獲取所有國家列表供搜索使用
    countries = db.get_all_countries()
    return render_template('search.html', countries=countries)

@app.route('/api/country/<country>')
def get_country_data(country):
    data = db.get_country_data(country)
    if data:
        return jsonify({
            'confirmed': data[1],
            'deaths': data[2],
            'recovered': data[3],
            'active': data[4]
        })
    return jsonify({'error': 'Country not found'}), 404

@app.route('/api/timeline')
def get_timeline():
    data = db.get_timeline_data()
    dates = [row[0].strftime('%Y-%m-%d') for row in data]
    confirmed = [row[1] for row in data]
    deaths = [row[2] for row in data]
    recovered = [row[3] for row in data]
    
    return jsonify({
        'dates': dates,
        'confirmed': confirmed,
        'deaths': deaths,
        'recovered': recovered
    })

@app.route('/compare')
def compare():
    # 獲取所有國家列表供選擇
    countries = db.get_all_countries()
    return render_template('compare.html', countries=countries)

if __name__ == '__main__':
    app.run(debug=True)