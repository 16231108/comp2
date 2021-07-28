import kfp.dsl as dsl
import kfp
from kfp.components import load_component
read=load_component('../components/read.yaml')
tag=load_component('../components/tag.yaml')
clean=load_component('../components/clean.yaml')
k_m=load_component('../components/k_m.yaml')
@dsl.pipeline(name='try')
def km():
    a=read()
    t=tag(a.output)
    m=k_m(t.output)
    return
kfp.compiler.Compiler().compile(km, '../pipeline/km.yaml')

# client = kfp.Client(host='http://ml-pipeline.ingress.isa.buaanlsde.cn/')
# client.create_run_from_pipeline_func(
#     mytry,
#     arguments={'translate':True},
#     )
# client.create_run_from_pipeline_func(
#     mytry,
#     arguments={'translate':False},
#     )