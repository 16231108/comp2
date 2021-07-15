from kfp.components import create_component_from_func
from kfp.components import  InputPath, OutputPath
def tag(text_path: InputPath(),output_text_path: OutputPath()):
    import numpy as np
    import pandas as pd
    data=pd.read_csv(text_path)
    data=data[0:1]
    data.to_csv(output_text_path,index=False)
tag=create_component_from_func(tag,base_image='star16231108/python:3.7',output_component_file='../components/tag.yaml')