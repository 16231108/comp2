import kfp
import kfp.dsl as dsl
from kfp.v2.dsl import (
    component,
    Input,
    Output,
    Dataset,
    Metrics,
)
from kfp.components import func_to_container_op, InputPath, OutputPath
client = kfp.Client(host='http://ml-pipeline.ingress.isa.buaanlsde.cn/')
def read():
    return dsl.ContainerOp(
        name='read',
        image='star16231108/mynewpy:v1',
        command=['python'],
        arguments=['read.py'],
        file_outputs={
            'data': '/tmp/result',
        }
    )
@func_to_container_op
def trans(text_path: InputPath(),output_text_path: OutputPath()):
    data=''
    with open(text_path, 'r') as reader:
        data=reader.read()
    with open(output_text_path, 'w') as writer:
        writer.write(data + 'trans\n')
@func_to_container_op
def tag(text_path: InputPath(),output_text_path: OutputPath()):
    data=''
    with open(text_path, 'r') as reader:
        data=reader.read()
    with open(output_text_path, 'w') as writer:
        writer.write(data + 'tag\n')
@dsl.pipeline(name='try')
def mytry():
	a=read()
	t=trans(a.outputs['data'])
	k=tag(t.output)
	return
kfp.compiler.Compiler().compile(mytry, __file__ + '.yaml'),
    
# client.create_run_from_pipeline_func(
#     mytry,
#     arguments={},
#     )