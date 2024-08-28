import re

def clean_tokens(tokens):
    # トークンのクリーニング
    cleaned_tokens = []
    for token in tokens:
        # 特定のクリーニングルールを適用する
        cleaned_token = token  # ここでは特にクリーニングの例を示しませんが、必要に応じて追加できます。
        cleaned_tokens.append(cleaned_token)
    
    return cleaned_tokens

def url_to_word_corpus(url):
    # URLをトークン化してクリーニングする関数
    token_pattern = re.compile(r'[/.=&?\-@:*%^(),~]+')
    tokens = token_pattern.split(url)
    tokens = [token.lower() for token in tokens if token]
    cleaned_tokens = clean_tokens(tokens)
    return cleaned_tokens

def read_urls_from_file(file_path):
    # ファイルからURLを1行ずつ読み取り、単語レベルのコーパスを構築する
    word_corpus = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            url = line.strip()
            word_corpus.append(url_to_word_corpus(url))
    return word_corpus

def write_corpus_to_file(corpus, output_file):
    # 単語レベルのコーパスをファイルに書き込む
    with open(output_file, 'w', encoding='utf-8') as file:
        for index, url_words in enumerate(corpus):
            file.write(f"URL {index+1}: {' '.join(url_words)}\n")

# URLが記述されたファイルのパス
file_path = 'URLdataset/URLdataset.csv'

# URL.txtファイルから単語レベルのコーパスを構築する
word_corpus = read_urls_from_file(file_path)

# 単語レベルのコーパスをcorpus.txtに書き出す
output_file = 'URLdataset/corpus.txt'
write_corpus_to_file(word_corpus, output_file)

# 結果の表示例
for index, url_words in enumerate(word_corpus):
    print(f"URL {index+1}: {url_words}")
