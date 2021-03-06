



# ---- sklearn中的岭回归_交通流量预测实例 ---- #
# -2-


import numpy as np
from sklearn.linear_model import Ridge
#from sklearn import cross_validation
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
def main():
    data = np.genfromtxt('data.txt', delimiter=',')
    plt.plot(data[:,5])
    plt.show()
    x = data[:,:5]
    y = data[:,5]
    poly = PolynomialFeatures(9)
    x = poly.fit_transform(x)
    train_x, test_x, train_y, test_y = \
    cross_validation.train_test_split(x, y, 
    test_size=0.3, random_state=0)
    clf = Ridge(alpha=1.0, fit_intercept=True)
    clf.fit(train_x, train_y)
    score = clf.score(test_x, test_y)
    print('score:',score)
    start = 200
    end = 300
    y_pre = clf.predict(x)
    time = np.arange(start, end)
    plt.plot(time, y[start:end],'b', label="real")
    plt.plot(time, y_pre[start:end],'r', label="predict")
    plt.legend(loc="upper left")
    plt.show()
 
if __name__ == '__main__':
    main()