from kfp.components import create_component_from_func
from kfp.components import  InputPath, OutputPath
def k_m(text_path: InputPath(),output_text_path: OutputPath()):
    import pandas as pd
    import numpy as np
    from sklearn.cluster import KMeans
    tfidf_matrix=pd.read_csv(text_path)
    tfidf_matrix=tfidf_matrix['tfidf_matrix']
    tfidf_matrix=[eval(i) for i in tfidf_matrix]
    num_clusters=5
    km=KMeans(n_clusters=num_clusters)
    km.fit(tfidf_matrix)
    clusters = km.labels_.tolist()
    with open(output_text_path) as f:
        f.write(km.cluster_centers_)
k_m=create_component_from_func(
    k_m,base_image='star16231108/python:3.7.1',output_component_file='../components/k_m.yaml',
    )
