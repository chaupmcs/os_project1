import psutil
import time
print("Running MPL...")
t_start = time.time()
p = psutil.Process()
p.cpu_percent()

import warnings
warnings.filterwarnings('ignore')
from keras import regularizers
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
from keras.layers import Activation
from keras.layers import Dropout
from keras.layers import Flatten
from keras.optimizers import Adam
import pandas as pd
import numpy as np
import json
from keras.constraints import max_norm
import keras
from keras import backend as K
from keras.constraints import max_norm
from keras.layers import Dropout
from keras import regularizers
from keras.models import Sequential
from sklearn.metrics import mean_squared_error



## data
with open("../data/X_train_HPCC_1_20_312.json") as of:
    X_train = np.array(json.load(of)).reshape(312, -1)
with open("../data/y_train_HPCC_1_20_312.json") as of:
    y_train = np.array(json.load(of))
with open("../data/X_test_HPCC_1_20_312.json") as of:
    X_test = np.array(json.load(of)).reshape(154, -1)
with open("../data/y_test_HPCC_1_20_312.json") as of:
    y_test = np.array(json.load(of))
    
## model
model = Sequential()
model.add(Dense(300, input_dim=200, kernel_initializer='normal', activation='relu',\
                kernel_constraint=max_norm(3)))
model.add(Dense(200, kernel_initializer='normal', activation='relu', kernel_constraint=max_norm(3)))
model.add(Dropout(rate = 0.5))
model.add(Dense(200, kernel_initializer='normal', activation='relu', kernel_constraint=max_norm(3)))
model.add(Dropout(rate = 0.5))
model.add(Dense(200, kernel_initializer='normal', activation='relu', kernel_constraint=max_norm(3)))
model.add(Dense(1, kernel_initializer='normal'))
# Compile model
opt = Adam(learning_rate=0.005)
model.compile(optimizer=opt, loss='mse')
model.fit(X_train, y_train, batch_size=32, epochs=150)
y_pred_prob = model.predict(X_test)[:,0]
# print("mse:", mean_squared_error(y_test, y_pred_prob))


mem = p.memory_full_info()
print("full mem information:", mem)
print('memory rss:', mem[0]/2.**30 , "GB")
print('memory vms:', mem[1]/2.**30 , "GB")
print('pfaults:', mem[2])
print('pageins:', mem[3])
print('memory uss:', mem[4]/2.**30 , "GB")

print("cpu percent:", p.cpu_percent())
print("cpu time:", p.cpu_times())




import sys
import subprocess
x = subprocess.run(["du",  "-h", "mpl.py"],  stdout=subprocess.PIPE)
encoding = "utf-8"
print("size of the file in hard disk:", end=" ")
print(str.strip(x.stdout.decode(encoding)))

t_end  = time.time()
print("running time = {} seconds".format(np.round( t_end-t_start, 2)))