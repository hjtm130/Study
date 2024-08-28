import numpy as np
import re
import itertools
from collections import Counter

data_nor = "./data2/url/a.txt"
data_ph = "./data2/url/b.txt"
sequence_lengths = 100  # 序列長

def clean_str(string):
    """
    データセットのトークン化および文字列のクリーニング。
    """
    string = string.replace('.', '/')
    string = string.replace('=', '/')
    string = string.replace('&', '/')
    string = string.replace('?', '/')
    string = string.replace('-', '/')
    string = string.replace('@', '/')
    string = string.replace(':', '/')
    string = string.replace('*', '/')
    string = string.replace('%', '/')
    string = string.replace('^', '/')
    string = string.replace('(', '/')
    string = string.replace(')', '/')
    string = string.replace(',', '/')
    string = string.replace('~', '/')
    
    return string.strip().lower()

def load_data_and_labels():
    """
    ファイルから極性データを読み込み、データを単語に分割しラベルを生成します。
    分割された文とラベルを返します。
    """
    # ファイルからデータを読み込む
    positive_examples = list(open(data_nor, "r", encoding='utf-8').readlines())
    positive_examples = [s.strip() for s in positive_examples]
    negative_examples = list(open(data_ph, "r", encoding='utf-8').readlines())
    negative_examples = [s.strip() for s in negative_examples]
    # 単語ごとに分割する
    x_text = positive_examples + negative_examples
    x_text = [clean_str(sent) for sent in x_text]
    x_text = [s.split("/") for s in x_text]
    # ラベルを生成する
    positive_labels = [0 for _ in positive_examples]
    negative_labels = [1 for _ in negative_examples]
    y = np.concatenate([positive_labels, negative_labels])
    return [x_text, y]

def pad_sentences(sentences, padding_word="<PAD/>"):
    """
    すべての文を同じ長さにパディングします。長さは最長の文によって定義されます。
    パディングされた文を返します。
    """
    sequence_length = sequence_lengths
    padded_sentences = []
    for i in range(len(sentences)):
        sentence = sentences[i]
        num_padding = sequence_length - len(sentence)
        if num_padding >= 0:
            new_sentence = sentence + [padding_word] * num_padding
            padded_sentences.append(new_sentence)
        else:
            padded_sentences.append(sentence[:sequence_lengths])
    return padded_sentences

def build_vocab(sentences):
    """
    文から単語のインデックスへのボキャブラリーマッピングを構築します。
    ボキャブラリーマッピングと逆マッピングを返します。
    """
    # ボキャブラリーを構築
    word_counts = Counter(itertools.chain(*sentences))
    # インデックスから単語へのマッピング
    vocabulary_inv = [x[0] for x in word_counts.most_common()]
    vocabulary_inv = list(sorted(vocabulary_inv))
    # 単語からインデックスへのマッピング
    vocabulary = {x: i for i, x in enumerate(vocabulary_inv)}
    return [vocabulary, vocabulary_inv]

def build_input_data(sentences, labels, vocabulary):
    """
    ボキャブラリーに基づいて文とラベルをベクトルにマッピングします。
    """
    x = np.array([[vocabulary[word] for word in sentence] for sentence in sentences])
    y = np.array(labels)
    return [x, y]

def load_data_url():
    """
    データセットの入力ベクトル、ラベル、ボキャブラリー、逆ボキャブラリーを読み込んで前処理します。
    入力ベクトル、ラベル、ボキャブラリー、逆ボキャブラリーを返します。
    """
    # データを読み込んで前処理する
    sentences, labels = load_data_and_labels()
    sentences_padded = pad_sentences(sentences)
    vocabulary, vocabulary_inv = build_vocab(sentences_padded)
    x, y = build_input_data(sentences_padded, labels, vocabulary)
    return [x, y, vocabulary, vocabulary_inv]
