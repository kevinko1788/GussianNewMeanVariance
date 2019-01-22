import numpy as np
import sys

def update(mean1, var1, mean2, var2):
	mean1 = float(mean1)
	var1 = float(var1)
	mean2 = float(mean2)
	var2 = float(var2)
	new_mean = ((var2*mean1) +(var1*mean2)) / (var1+var2)
	new_var = 1/((1/var1+(1/var2)))

	return "updated mean:{} updated var: {}".format(new_mean,new_var)
def predict(mean1, var1, mean2, var2):
	mean1 = float(mean1)
	var1 = float(var1)
	mean2 = float(mean2)
	var2 = float(var2)
	new_mean = mean1 + mean2
	new_var = var1 + var2
	return "predicted mean:{} predicted var: {}".format(new_mean,new_var)

	
if sys.argv[1] == 'update':
	print(update(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5]))

elif sys.argv[1] == 'predict':
	print(predict(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5]))
else:
	print('invalid input, please enter either update or predict')

