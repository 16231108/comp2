from kfp.components import create_component_from_func
from kfp.components import  InputPath, OutputPath
def tag(text_path: InputPath(),t2:InputPath(),t3:InputPath(),output_text_path: OutputPath()):
    import pandas as pd
    import numpy as np
    import joblib
    km = joblib.load(text_path)
    clusters = km.labels_.tolist()
    totalvocab_tokenized=
    totalvocab_stemmed=
    terms=
    synopses=pd.read_csv(t3)
    synopses=synopses = np.array(synopses)
    synopses = synopses.ravel()
    ranks = []
    for i in range(0,len(synopses)):
        ranks.append(i)
    films = {'rank': ranks, 'synopsis': synopses, 'cluster': clusters}
    frame = pd.DataFrame(films, index = [clusters] , columns = ['rank', 'cluster'])
#print(frame['cluster'].value_counts())
    grouped = frame['rank'].groupby(frame['cluster']) #groupby cluster for aggregation purposes
#print(grouped.mean())


    vocab_frame = pd.DataFrame({'words': totalvocab_tokenized}, index = totalvocab_stemmed)
    order_centroids = km.cluster_centers_.argsort()[:, ::-1]
    for i in range(5):
        print("Cluster %d words: " %i, end='') #%d功能是转成有符号十进制数 #end=''让打印不要换行
        for ind in order_centroids[i, :6]: #replace 6 with n words per cluster
        #b'...' is an encoded byte string. the unicode.encode() method outputs a byte string that needs to be converted back to a string with .decode()
            print('%s' %vocab_frame.loc[terms[ind].split(' ')].values.tolist()[0][0].encode('utf-8', 'ignore'), end=', ')
        print() #add whitespace
        print() #add whitespace

