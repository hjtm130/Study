import requests
import json
from urllib.parse import quote_plus

# 注意: f-strings は Python 3.6+ が必要です

# Common Crawl インデックスサーバーのURL
CC_INDEX_SERVER = 'http://index.commoncrawl.org/'

# クエリしたい Common Crawl インデックス名
INDEX_NAME = 'CC-MAIN-2024-22'      # 最新のインデックス名に置き換えてください

# Common Crawl インデックスで調べたい URL
target_url = 'commoncrawl.org/faq'  # 対象のURLに置き換えてください

# Common Crawl インデックスを検索するための関数
def search_cc_index(url):
    encoded_url = quote_plus(url)
    index_url = f'{CC_INDEX_SERVER}{INDEX_NAME}-index?url={encoded_url}&output=json'
    response = requests.get(index_url)
    print("Response from CCI:", response.text)  # サーバーからの応答を出力します
    if response.status_code == 200:
        records = response.text.strip().split('\n')
        return [json.loads(record) for record in records]
    else:
        return None

# Common Crawl からコンテンツを取得するための関数
def fetch_page_from_cc(records):
    for record in records:
        offset, length = int(record['offset']), int(record['length'])
        prefix = record['filename'].split('/')[0]
        s3_url = f'https://data.commoncrawl.org/{record["filename"]}'
        response = requests.get(s3_url, headers={'Range': f'bytes={offset}-{offset+length-1}'})
        if response.status_code == 206:
            # 応答コンテンツを必要に応じて処理します
            # 例えば、WARC レコードを解析するには warcio を使用できます
            return response.content
        else:
            print(f"Failed to fetch data: {response.status_code}")
            return None

# 対象URLに関連するインデックスを検索します
records = search_cc_index(target_url)
if records:
    print(f"Found {len(records)} records for {target_url}")

    # 最初のレコードからページコンテンツを取得します
    content = fetch_page_from_cc(records)
    if content:
        print(f"Successfully fetched content for {target_url}")
        # 'content' 変数を必要に応じて処理できます
else:
    print(f"No records found for {target_url}")