from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

iris = load_iris()
x = iris.data
y = iris.target

x_train , x_test , y_train , y_test = train_test_split(x , y,test_size = 0.2, random_state=42)

model = SVC(kernel='linear')

model.fit(x_train,y_train)

y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test,y_pred)

print(accuracy)




