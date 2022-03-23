from Client import Client
from Site import Site
import numpy as np
import os


path = os.path.abspath(os.getcwd())

# 读取边缘节点
sites_read = np.loadtxt(os.path.join(path, 'data', 'site_bandwidth.csv'), dtype=str, delimiter=',')
sites = []
for i in range(1, len(sites_read)):
    sites.append(Site(sites_read[i][0], sites_read[i][1]))



clients_read = np.loadtxt(os.path.join(path, 'data', 'site_bandwidth.csv'), dtype=str, delimiter=',')
clients = []
for i in range(1, len(clients_read)):
    clients.append(Client(clients_read[i][0]))


print(sites[0].site_name, float(sites[0].bandwidth))
print(clients[0].client_name)