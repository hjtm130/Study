import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

# データの読み込み
data = pd.read_csv('processed_data.csv')

# 特徴量とラベルに分割
X = data.drop(columns=['status'])
y = data['status']

# データの分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ロジスティック回帰モデルの定義と学習
model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train, y_train)

# テストデータでの予測と評価
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f'Accuracy: {accuracy:.2f}')
print('Classification Report:')
print(report)
