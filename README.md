# Scikit-learn C4.5 tree classifier
A C4.5 tree classifier based on the [zhangchiyu10/pyC45](https://github.com/zhangchiyu10/pyC45) repository, refactored to be compatible with the [scikit-learn](https://scikit-learn.org/stable/index.html) library.

To use this classifier, just copy c45 directory to your project and import classifier where you need it using `from c45 import C45` line

Example usage can be found in a main.py file:

```
>>> from sklearn.datasets import load_iris
>>> from sklearn.model_selection import train_test_split
>>> from c45 import C45
>>>
>>> iris = load_iris()
>>> clf = C45(attrNames=iris.feature_names)
>>> X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.5)
>>> clf.fit(X_train, y_train)
C45(attrNames=['sepallengthcm', 'sepalwidthcm', 'petallengthcm', 'petalwidthcm'])
>>> print(f'Accuracy: {clf.score(X_test, y_test)}')
Accuracy: 0.8533333333333334
>>> clf.printTree()
<?xml version="1.0" ?>
<DecisionTree>
        <petallengthcm flag="l" p="0.413" value="3.7">0</petallengthcm>
        <petallengthcm flag="r" p="0.587" value="3.7">
                <petallengthcm flag="l" p="0.591" value="4.8">1</petallengthcm>
                <petallengthcm flag="r" p="0.409" value="4.8">
                        <petallengthcm flag="l" p="0.111" value="5.0">
                                <sepallengthcm flag="l" p="0.5" value="6.3">2</sepallengthcm>
                                <sepallengthcm flag="r" p="0.5" value="6.3">1</sepallengthcm>
                        </petallengthcm>
                        <petallengthcm flag="r" p="0.889" value="5.0">2</petallengthcm>
                </petallengthcm>
        </petallengthcm>
</DecisionTree>
```
