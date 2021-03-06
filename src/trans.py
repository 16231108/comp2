from kfp.components import create_component_from_func
from kfp.components import  InputPath, OutputPath
def trans(text_path: InputPath(),output_text_path: OutputPath()):
    import numpy as np
    import pandas as pd
    data=pd.read_csv(text_path)
    data=data[-2:]
    data.to_csv(output_text_path,index=False)
trans=create_component_from_func(trans,base_image='star16231108/python:3.7',output_component_file='../components/trans.yaml')