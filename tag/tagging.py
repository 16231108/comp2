import hashlib
import pickle
import requests
import time
import json
from sshtunnel import SSHTunnelForwarder
server=SSHTunnelForwarder(('47.92.240.36', 22),  ssh_username='jt',  ssh_password='vdaubCp7yaSreqlT', remote_bind_address=('192.168.0.84', 3306))
server.start()
server_ip='140.143.5.134:27777'
with open('./data/field.pkl', 'rb') as f:
    field_dict = pickle.load(f)
table="ms_paper_ghl_20201026"
sql_get_total = f'select count(*) from {table} where field_l1 is NULL'
sql_get_data = f'select id, title_E, keyword_E, venue_E from {table} '\
                f'where field_l1 is NULL limit 10000 offset {{}}'
sql_update_data = f"update {table} set field_l1=%s, field_l2=%s, field_l1_id=%s, field_l2_id=%s, finished=1 where id='{{}}'"
base_key = 'buaa_label_2019'
def get_api_key(base_key):
    base_key += ("-" + time.strftime("%F-%H"))
    md5 = hashlib.md5()
    base_key = base_key.encode('utf-8')
    md5.update(base_key)
    return md5.hexdigest()
k=[{'id': '00107b49-172b-11eb-a93b-0242ac110002', 'title': '14362107968',
                'keywords': '84267860088', 'venue': 'Study of the decays $\psi(3686)\rightarrow\gamma\chi_{cJ}\rightarrow\gamma\bar{p}K^{*+}\Lambda+c.c.$ and $\psi(3686)\rightarrow\bar{p}K^{*+}\Lambda+c.c.$',
                'abstract': ''}]
response = requests.post(f'http://{server_ip}/sci_label',
                                     data={'api_key': get_api_key(base_key),
                                           'paper_list': json.dumps(k)})
out = json.loads(response.text)
print(out)
