import random
import joblib
from nltk.corpus import movie_reviews
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics


# 加载影评数据 [(word列表, 标签)]
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

# 打乱数据
random.shuffle(documents)

# 变成文本 + 标签
texts = [" ".join(words) for words, label in documents]
labels = [1 if label == 'pos' else 0 for words, label in documents]

# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

# 构建模型
model = make_pipeline(CountVectorizer(), MultinomialNB())

# 训练模型
model.fit(X_train, y_train)

# 评估模型
y_pred = model.predict(X_test)
print("情感预测准确率:", metrics.accuracy_score(y_test, y_pred))

# 保存模型
joblib.dump(model, "sentiment_model.pkl")