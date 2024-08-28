import torch
import transformers
import tqdm

# BERTの準備
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# 読み込むテキストファイルのパス
corpus_file = 'corpus.txt'

# テキストをBERT埋め込みする関数
def embed_text_with_bert(text):
    inputs = tokenizer(text, return_tensors="pt", max_length=512, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).squeeze().numpy()

# corpus.txtから1行ずつテキストを読み込んでBERT埋め込みを行う
with open(corpus_file, 'r', encoding='utf-8') as file:
    for line in tqdm(file.readlines()):
        text = line.strip()
        if text:
            embeddings = embed_text_with_bert(text)
            # ここでembeddingsを使って何か処理を行う場合
            print(f"Embeddings for '{text}': {embeddings}")

