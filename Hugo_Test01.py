# Data Preprocessing Template

# Importing the libraries
import numpy as np 
import matplotlib.pyplot as plt #畫圖用
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv') # read csv file
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values# or y = dataset.iloc[:, 3]
    # iloc 取某行某列
    # : 整行/列選取
    # :-1 選取整行(列)，唯最後一行(列)不取
    # 在python裡面用ML，需要創健包含自變量的矩陣&因變量的向量(用.value,否則就只會是dataframe)


# Taking care of missing data
    # 直接刪除數據 : 風險大
    # 用平均值代替數據
        # 用工具，不用自己算
from sklearn.preprocessing import Imputer # 從sklearn裡面的preprocessing(預處理)import Imputer(一種包涵缺失數據處理策略的class)
imputer = Imputer(missing_values = 'NaN', strategy = "mean", axis = 0) # 創建object# 設定Nan為missing, 取平均值, 取列平均)
imputer = imputer.fit(X[:, 1:3])# 用數據fit object #相當於1~2(3不算)
X[:, 1:3] = imputer.transform(X[:, 1:3])


# Categorical Data
    # 將類別轉換為數值 (Encoding categorical data)
from sklearn.preprocessing import LabelEncoder, OneHotEncoder # 將種類轉換為數字的class
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0]) # 但這樣變成0123... 這樣姆湯

# -> 自變量use onehotencoder
onehotencoder = OneHotEncoder(categorical_features = [0]) # categorical_features: 告訴是哪一個column
X = onehotencoder.fit_transform(X).toarray() # 上一行已經告知哪一個column為，所以處理的時候已經知道要處裡哪部分 #to array
 
# -> python函數可以直接將因變量變數字，所以不需要onehot, labelencoder即可
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

