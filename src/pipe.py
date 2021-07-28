import kfp.dsl as dsl
import kfp
from kfp.components import load_component
read=load_component('../components/read.yaml')
trans=load_component('../components/trans.yaml')
tag=load_component('../components/tag.yaml')
@dsl.pipeline(name='try')
def mytry(translate):
	a=read()
	with dsl.Condition(translate==True):
		t=trans(a.output)
		k=tag(t.output)
	with dsl.Condition(translate==False):
		k=tag(a.output)
	return
kfp.compiler.Compiler().compile(mytry, '../pipeline/mytry.yaml')

# client = kfp.Client(host='http://ml-pipeline.ingress.isa.buaanlsde.cn/')
# client.create_run_from_pipeline_func(
#     mytry,
#     arguments={'translate':True},
#     )
# client.create_run_from_pipeline_func(
#     mytry,
#     arguments={'translate':False},
#     )