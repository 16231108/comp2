from kfp.components import create_component_from_func
from kfp.components import  InputPath, OutputPath
def read(output_text_path: OutputPath()):
    from sshtunnel import SSHTunnelForwarder
    import pymysql
    import pandas as pd
    import numpy as np
    f=open(output_text_path,'w');
    server=SSHTunnelForwarder(('47.92.240.36', 22),  ssh_username='jt',  ssh_password='vdaubCp7yaSreqlT', remote_bind_address=('192.168.0.84', 3306))
    server.start()
    conn = pymysql.connect(host='127.0.0.1',  port=server.local_bind_port,user='root',  passwd='root' , charset ='utf8',   database = 'dump',)
    sql_get_total = f"select title from ms_paper_ghl_20201026"
    df = pd.read_sql(sql_get_total, con=conn)[:2000]
    df.to_csv(output_text_path,index=False)
read('../t.csv')
#read=create_component_from_func(read,base_image='star16231108/python:3.7',output_component_file='../components/read.yaml')