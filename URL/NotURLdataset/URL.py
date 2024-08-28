import csv

# 入力ファイルと出力ファイルのパス
input_file = 'dataset.csv'
output_file = 'processed_data.csv'

# URL部分を削除してデータを抽出する関数
def process_data(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f_in, open(output_file, 'w', encoding='utf-8', newline='') as f_out:
        reader = csv.reader(f_in)
        writer = csv.writer(f_out)
        
        # ヘッダーを読み込んで書き出す
        header = next(reader)
        writer.writerow(header[1:])  # URL部分を除いて書き出す
        
        # 各行を処理して書き出す
        for row in reader:
            writer.writerow(row[1:])  # URL部分を除いて書き出す

# 実行
process_data(input_file, output_file)
