from sshtunnel import SSHTunnelForwarder
import pymysql
import sys
f=open('/tmp/result','w');
sys.stdout=f;
server=SSHTunnelForwarder(('47.92.240.36', 22),  ssh_username='jt',  ssh_password='vdaubCp7yaSreqlT', remote_bind_address=('192.168.0.84', 3306))
server.start()
conn = pymysql.connect(host='127.0.0.1',  port=server.local_bind_port,user='root',  passwd='root' , charset ='utf8',   database = 'dump',)
sql_get_total = f"select * from ms_paper_ghl_20201026 where title = 'Evidence for the decays of and' OR title IS NULL"
cursor = conn.cursor()
cursor.execute(sql_get_total)
i=0
for x in cursor:
	print(x)
	i+=1
	if(i==3):
		break
f.close()