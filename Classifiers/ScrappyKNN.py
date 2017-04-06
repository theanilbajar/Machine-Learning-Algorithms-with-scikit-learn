from scipy.spatial import distance
def euc(a, b):
    return distance.euclidean(a, b)

class ScrappyKNN():
    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train
    #predict function for our model.
    def predict(self, X_test):
        predictions= []
        for row in X_test:
            label = self.closest(row)
            predictions.append(label)
        return predictions
    #Function to calculate closest point to test data point i.e. row
    def closest(self, row):
        best_dist = euc(row, self.X_train[0])
        best_index=0
        for i in range(1, len(self.X_train)):
            dist = euc(row, self.X_train[i])
            if dist < best_dist:
                best_dist = dist
                best_index=i
        return self.y_train[best_index]
#Load iris dataset from sklearn datasets
from sklearn import datasets
iris = datasets.load_iris()
X = iris.data
y = iris.target
#Split data into two parts: 1) training data 2) test data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)

#from sklearn.neighbors import KNeighborsClassifier
#clf = KNeighborsClassifier()
#Replacing KNN with our solution
clf = ScrappyKNN()
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)
#print predictions
from sklearn.metrics import accuracy_score
print y_test
print predictions
print accuracy_score(y_test, predictions)
