from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
from datetime import datetime
from test import scrape_trending_topics
import os
from dotenv import load_dotenv



app = Flask(__name__)

# Load the .env file
load_dotenv()
mail = os.getenv("mail")
userid = os.getenv("userid")
password = os.getenv('password')
scraper_api_key = os.getenv('scraper_api_key')
Mongodb_password=os.getenv("Mongodb_password")


MONGODB_URI = f"mongodb+srv://sharmila:{Mongodb_password}@scraping.juq1qns.mongodb.net/myDatabase?retryWrites=true&w=majority&tls=true"


client = MongoClient(MONGODB_URI, tls=True, tlsAllowInvalidCertificates=True)
db = client['myDatabase']
collection = db['collection1']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_script', methods=['POST'])
def run_script():
    current_data = scrape_trending_topics(mail, userid, password, scraper_api_key)

    
    ip_address = current_data[0]
    trends = current_data[1]

    
    db_data = {
        "ip_address": ip_address,
        "name_of_trend_1": trends[0] if len(trends) > 0 else None,
        "name_of_trend_2": trends[1] if len(trends) > 1 else None,
        "name_of_trend_3": trends[2] if len(trends) > 2 else None,
        "name_of_trend_4": trends[3] if len(trends) > 3 else None,
        "name_of_trend_5": trends[4] if len(trends) > 4 else None,
        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    
    result = collection.insert_one(db_data)

    
    db_data['_id'] = str(result.inserted_id)

    return jsonify({
        "timestamp": db_data["timestamp"],
        "ip_address": ip_address,
        "trends": trends,
        "db_data": db_data
    })

if __name__ == '__main__':
    app.run(debug=True)
