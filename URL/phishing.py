from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import numpy as np
import optuna
from sklearn.model_selection import cross_validate

training_data = np.genfromtxt('processed_data.csv', delimiter=',', dtype=np.int32)
X = training_data[:,:-1]
y = training_data[:,-1]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=True, random_state=101
)

# 訓練用データを使った検出器の訓練
classifier = LogisticRegression(solver='lbfgs')
classifier.fit(X_train, y_train)
# 予測
predictions = classifier.predict(X_test)
# 正解率を出力させる
accuracy = 100.0 * accuracy_score(y_test, predictions)
print("**********************************The accuracy of your Logistc Regression on testing data is: {}".format(accuracy))

from sklearn.model_selection import cross_val_score
# 交差検証(5分割)による汎化性能の評価
scores = cross_val_score(classifier, X_train, y_train, cv=5)
# 評価結果の出力
print("**********************************Evaluated score by cross-validation(k=5): {}".format(100 * scores.mean()))