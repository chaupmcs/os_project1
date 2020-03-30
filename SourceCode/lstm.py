import psutil
import time
print("Running LTSM...")
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

    
## model
def createModel(l1Nodes, l2Nodes, d1Nodes, d2Nodes, inputShape):
    # input layer
    lstm1 = LSTM(l1Nodes, input_shape=inputShape, return_sequences=True)
    lstm2 = LSTM(l2Nodes, return_sequences=True)
    flatten = Flatten()
    dense1 = Dense(d1Nodes)
    dense2 = Dense(d2Nodes)

    outL = Dense(1)
    # combine the layers
    layers = [lstm1, lstm2, flatten,  dense1, dense2, outL]
    # create the model
    model = Sequential(layers)
    opt = Adam(learning_rate=0.005)
    model.compile(optimizer=opt, loss='mse')
    return model



## data
with open("../data/X_train_HPCC_1_20_312.json") as of:
    X_train = np.array(json.load(of))
with open("../data/y_train_HPCC_1_20_312.json") as of:
    y_train = np.array(json.load(of))
with open("../data/X_test_HPCC_1_20_312.json") as of:
    X_test = np.array(json.load(of))
with open("../data/y_test_HPCC_1_20_312.json") as of:
    y_test = np.array(json.load(of))
    
model = createModel(8, 8, 8, 4, (X_train.shape[1], X_train.shape[2]))
model.fit(X_train, y_train, batch_size=8, epochs=30, verbose=1)
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
x = subprocess.run(["du",  "-h", "lstm.py"],  stdout=subprocess.PIPE)
encoding = "utf-8"
print("size of the file in hard disk:", str.strip(x.stdout.decode(encoding)))


t_end  = time.time()
print("running time = {} seconds".format(np.round( t_end-t_start, 2)))