from bear_generator import BearGenerator
from bear import Bear
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OneHotEncoder
from sklearn import tree
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.externals.six import StringIO
import features

generator = BearGenerator()
dataset = generator.generate_dataset(1000)
X = dataset[0]
Y = dataset[1]

x_train, x_test, y_train, y_test = train_test_split(X,Y)#, test_size=0.975)

model_names = ["Nearest Neighbors", "Linear SVM", "RBF SVM", "Gaussian Process",
         "Decision Tree", "Random Forest", "AdaBoost",
         "Naive Bayes"]

classifiers = [
    KNeighborsClassifier(3),
    SVC(kernel="linear", C=0.025),
    SVC(gamma=2, C=1),
    GaussianProcessClassifier(1.0 * RBF(1.0)),
    DecisionTreeClassifier(),
    RandomForestClassifier(),
    AdaBoostClassifier(),
    GaussianNB()]

# for name, clf in zip(model_names, classifiers):
#     model = clf.fit(x_train, y_train)
#     res = model.predict(x_test)
#     acc = accuracy_score(y_test, res)
#     print('Model: ' + name + ' Accuracy: ' + str(acc))
#     if name=="Decision Tree":
#         plt.figure(figsize=(20,10))
#         tree.plot_tree(model, feature_names=features.feature_names)
#         plt.show()

model = DecisionTreeClassifier().fit(x_train, y_train)
model2 = DecisionTreeClassifier(max_depth=8).fit(x_train, y_train)
res = model.predict(x_test)
res2 = model2.predict(x_test)
acc = accuracy_score(y_test, res)
acc2 = accuracy_score(y_test, res2)
print('Accuracy: ' + str(acc))
print('Accuracy2: ' + str(acc2))
plt.figure(figsize=(20,10))
tree.plot_tree(model2, feature_names=features.feature_names)
plt.show()