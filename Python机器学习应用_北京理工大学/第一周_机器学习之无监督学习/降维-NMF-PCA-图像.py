

# ----* 降维-NMF-PCA-图像 *---- #



#******************************************************************
''' 

    --非负矩阵分解（Non-negative Matrix Factorization ，NMF）
        是在矩阵中所有元素均为非负数约束条件之下的矩阵分解方法。
    
    基本思想：给定一个非负矩阵V，NMF能够找到一个非负矩阵W和一个
            非负矩阵H，使得矩阵W和H的乘积近似等于矩阵V中的值。

    • W矩阵：基础图像矩阵，相当于从原矩阵V中抽取出来的特征。
    • H矩阵：系数矩阵。
    • NMF能够广泛应用于图像分析、文本挖掘和语音处理等领域。
 
'''
#--------------------------------------------------
'''

    -NMF人脸数据特征提取-

    目标：已知Olivetti人脸数据共400个，每个数据是64*64大小。由于
        NMF分解得到的W矩阵相当于从原始矩阵中提取的特征，那么就可
        以使用NMF对400个人脸数据进行特征提取.

    通过设置k的大小，设置提取的特征的数目。在本实验中设置k=6，
        随后将提取的特征以图像的形式展示出来。

'''
#******************************************************************



#1-导入相关包： 
import matplotlib.pyplot as plt     #数据的可视化。
from sklearn import decomposition   #PCA算法包。
from sklearn.datasets import fetch_olivetti_faces   #加载Olivetti人脸数据集导入函数。 
from numpy.random import RandomState   #加载RandomState用于创建随机种子。


#2-设置基本参数并加载数据：
n_row, n_col = 2 ,3     #设置图像展示时的排列。
n_components = n_row * n_col    #设置提取的特征的数目。
image_shape = (64, 64)     #设置人脸数据图片的大小。

#加载数据，并打乱顺序。
dataset = fetch_olivetti_faces(shuffle = True, 
            random_state=RandomState(0))
#faces = datasets.data  #NameError: name 'datasets' is not defined
faces = dataset.data


#3-设置图像的展示方式： 
def plot_gallery( title, images, n_col = n_col, n_row = n_row ): 
    plt.figure( figsize = (2. * n_col, 2.26 * n_row ))  #创建图片，并指定图片大小。
    plt.suptitle( title, size = 16 )    #设置标题和字体大小。

    for i , comp in enumerate(images): 
        plt.subplot( n_row, n_col, i + 1 )   #选择画制的子图。
        vmax = max(comp.max(), -comp.min())

        #对数值归一化，并以灰度图形式显示。
        plt.imshow(comp.reshape(image_shape), cmap = plt.cm.gray, 
                   interpolation = 'nearest', vmin = -vmax, vmax = vmax )

        #去除子图的坐标轴标签。
        plt.xticks(())
        plt.yticks(())

    plt.subplots_adjust( 0.01, 0.05, 0.99, 0.93, 0.04, 0. )     #对子图位置及间隔调整。


#创建特征提取的对象NMF，使用PCA作为对比。 
estimators = [ 
    ( 'Eigenface - PCA using randomized SVD', #提取方法名称,
    decomposition.PCA(n_components=6, whiten=True ) ), #PCA实例 , 
    ('Non-negative components - NMF', # 提取方法名称 , 
    decomposition.NMF(n_components=6, init = 'nndsvda', 
    tol = 5e-3)) #NMF实例。
            ] 


#4-降维后数据点的可视化： 
for name, estimator in estimators:      #分别调用PCA和NMF。
    estimator.fit(faces)    #调用PCA或NMF提取特征。
    components_ = estimator.components_     #获取提取的特征。

    plot_gallery(name, components_[:n_components])  #按照固定格式进行排列。

plt.show( )     #可视化。



