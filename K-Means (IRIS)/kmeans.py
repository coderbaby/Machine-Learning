import numpy as np
from sklearn.cluster import KMeans
def get_data(filename):
    fp = open(filename, 'r')
    D = {}
    for line in fp:
        line = line.strip("\n")
        word = line.split(",")
        for w in word:
            w = w.strip()
            if(w == "Iris-versicolor"):
                word[2] = "Other"
                word[2].strip("\"")
            if(w == "Iris-virginica"):
                word[2] = "Other"
                word[2].strip("\"")
            
        x = word[0]
        y = word[1]
        truth = word[2]
        D[(x, y)] = truth
    return D

if __name__ == "__main__":
    D = get_data("iris_train.arff")
    Arr = []
    for d in D:
        X = d[0]
        Y = d[1]
        V = [X, Y]
        Arr.append(V)
    kmeans = KMeans(n_clusters=2, random_state=0).fit(Arr)
    print("\nAssignment of Training set:-\n")
    for d, k in zip(D.keys(), kmeans.labels_):
        if (k == 1):
            print("("+str(d[0])+", " + str(d[1])+")" + " --> " + "Iris-setosa")
        else:
            print("("+str(d[0])+", " + str(d[1]) + ")" + " --> " + "Other")
    print("\n----------------------------------------------------------------------------------")
    
    print("Centers of the two clusters are: ")
    for x in kmeans.cluster_centers_:
        print("("+str(x[0])+", "+str(x[1])+")")

    print("----------------------------------------------------------------------------------")
    

    print("\nTest Case Results:-\n")

    T = get_data("test.arff")
    TArr = []
    for t in T:
        X = t[0]
        Y = t[1]
        V = [[X, Y]]
        pred = kmeans.predict(V)
        for x in pred:
            if x == 0:
                print("("+str(X)+", "+str(Y)+")"+" ---> "+"Other")
            else:
                print("("+str(X)+", "+str(Y)+")"+" ---> "+"Iris-setosa")
    

