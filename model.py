import numpy as np
import sys

def update(mean1, var1, mean2, var2):
	mean1 = float(mean1)
	var1 = float(var1)
	mean2 = float(mean2)
	var2 = float(var2)
	new_mean = ((var2*mean1) +(var1*mean2)) / (var1+var2)
	new_var = 1/((1/var1+(1/var2)))

	return "new mean:{} new var: {}".format(new_mean,new_var)

print(update(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]))

