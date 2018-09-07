import numpy as np
from pydbscan import gen_cluster_data, GDBSCAN_RT, GDBSCAN

cld = gen_cluster_data(2255, 1000)
print(np.asarray(cld).dtype)

db = GDBSCAN_RT(50000000,50000000)
db_2 = GDBSCAN(np.asarray(cld))


print(db_2.predict(0.3, 1 ))
for i in range(0,10):
	print(db.predict(np.asarray(cld),0.3, 1 ))
	print(i)
