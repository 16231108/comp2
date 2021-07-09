import kfp
import kfp.dsl as dsl
from kfp.v2.dsl import (
    component,
    Input,
    Output,
    Dataset,
    Metrics,
)
client = kfp.Client(host='http://localhost:8082')
def read():
	return dsl.ContainerOp(
        name='read',
        image='python:3.7',
        file_outputs={'out': '/tmp/result'},
        )
def transs(a:str)->str:
	return(a+":翻译")
def tagg(a:str)->str:
	return(a+"--1")
trans=kfp.components.func_to_container_op(transs)
tag=kfp.components.func_to_container_op(tagg)
@dsl.pipeline(name='try')
def mytry():
	a=read()
	t=a.outputs['out']
	if(t=='hj'):
		a=trans(a.output)
	k=tag(a.output)
	return
client.create_run_from_pipeline_func(
    mytry,
    arguments={},
    )