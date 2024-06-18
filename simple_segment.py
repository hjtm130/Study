import requests
from bs4 import BeautifulSoup

# クローリングしたいURL
target_url = 'https://www.bmddbs.com/h53/'

# 1. URLからHTMLコンテンツを取得
response = requests.get(target_url)

# エラーチェック
if response.status_code == 200:
    # 2. BeautifulSoupを使ってHTMLを解析
    soup = BeautifulSoup(response.text, 'html.parser')

    # 例：タイトルを取得する場合
    title = soup.title.text
    print(f"ページのタイトル: {title}")

    # 他に必要な情報を取得したり、ページ内のリンクなどをスクレイピングすることも可能です

else:
    print(f"ページの取得に失敗しました。ステータスコード: {response.status_code}")
