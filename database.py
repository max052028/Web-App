from flask_mysqldb import MySQL
from datetime import datetime

class Database:
    def __init__(self, app):
        self.mysql = MySQL(app)

    def get_global_stats(self):
        """獲取全球統計數據"""
        cur = self.mysql.connection.cursor()
        cur.execute("""
            SELECT 
                SUM(confirmed) as total_cases,
                SUM(deaths) as total_deaths,
                SUM(recovered) as total_recovered,
                SUM(active) as active_cases
            FROM country_wise_latest
        """)
        data = cur.fetchone()
        cur.close()
        return data

    def get_country_data(self, country):
        """獲取特定國家的數據"""
        cur = self.mysql.connection.cursor()
        cur.execute("""
            SELECT * FROM country_wise_latest 
            WHERE country = %s
        """, (country,))
        data = cur.fetchone()
        cur.close()
        return data

    def get_timeline_data(self):
        """獲取時間序列數據"""
        cur = self.mysql.connection.cursor()
        cur.execute("""
            SELECT date, confirmed, deaths, recovered 
            FROM day_wise 
            ORDER BY date
        """)
        data = cur.fetchall()
        cur.close()
        return data

    def get_all_countries(self):
        """獲取所有國家列表"""
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT DISTINCT country FROM country_wise_latest")
        countries = [row[0] for row in cur.fetchall()]
        cur.close()
        return countries