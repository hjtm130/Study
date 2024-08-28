import csv

# 入力ファイルと出力ファイルのパス
input_file = 'dataset.csv'
output_file = 'URLdataset.csv'

# URL部分を抜き出して新しいCSVファイルに出力する関数
def extract_urls_to_csv(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f_in, open(output_file, 'w', encoding='utf-8', newline='') as f_out:
        reader = csv.reader(f_in)
        writer = csv.writer(f_out)
        
        # ヘッダーを読み込んで書き出す
        header = next(reader)
        writer.writerow(['URL'])  # 新しいCSVファイルのヘッダー
        
        # 各行を処理してURL部分を書き出す
        for row in reader:
            url = row[0]  # 各行の最初の要素がURL
            writer.writerow([url])
            
# 実行
extract_urls_to_csv(input_file, output_file)
