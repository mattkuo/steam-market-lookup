import os
from urllib import request
from bs4 import BeautifulSoup
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/listings/<int:app_id>/<item>', methods=['GET'])
def search_items(app_id, item):
    url = "http://steamcommunity.com/market/listings/{}/{}".format(app_id, encode(item))
    req = request.urlopen(url).read()
    soup = BeautifulSoup(req, 'html.parser')

    result = {'success': True, 'items': []}

    name = soup.select('.market_listing_nav > a')[0].text.strip()
    
    if name:
        result['app_name'] = name

    for row in soup.find_all('div', class_='market_listing_row'):
        price = row.find('span', class_='market_listing_price_with_fee').text.strip()
        item_id = clean_id(row['id'])
        result['items'].append({'id': item_id, 'price': price})

    if not result['items']:
        result['success'] = False
        result['message'] = 'Item not found.'
        del result['items']

    return jsonify(result)

def encode(str):
    return str.replace(' ', '%20')

def clean_id(str):
    return str.replace('listing_', '')

def clean_price(str):
    return float(str.strip().split(' ')[1])

if __name__ == '__main__':
    app.run(debug=True)
