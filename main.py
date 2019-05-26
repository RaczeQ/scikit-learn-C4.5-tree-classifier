from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from c45 import C45

iris = load_iris()
clf = C45(attrNames=iris.feature_names)
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.5)
clf.fit(X_train, y_train)
print(f'Accuracy: {clf.score(X_test, y_test)}')
clf.printTree()