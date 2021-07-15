import kfp.dsl as dsl
import kfp
from kfp.components import load_component
read=load_component('../components/read.yaml')
trans=load_component('../components/trans.yaml')
tag=load_component('../components/tag.yaml')
@dsl.pipeline(name='try')
def mytry():
	a=read()
	t=trans(a.output)
	k=tag(t.output)
	return
kfp.compiler.Compiler().compile(mytry, '../pipeline/mytry.yaml')
# client.create_run_from_pipeline_func(
#     mytry,
#     arguments={},
#     )