import numpy as np
from pydbscan import gen_cluster_data, GDBSCAN

cld = gen_cluster_data(200, 1000)
db = GDBSCAN(np.asarray(cld))

print(db.predict(0.3, 1 ))

