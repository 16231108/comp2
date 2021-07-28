from kfp.components import create_component_from_func
from kfp.components import  InputPath, OutputPath
def clean(text_path: InputPath(),output_text_path: OutputPath(),o2: OutputPath()):
    import numpy as np
    import pandas as pd
    import nltk,re
    #nltk.download('punkt')
    synopses = pd.read_csv(text_path)[:100]
    synopses = np.array(synopses)
    synopses = synopses.ravel()
    from nltk.stem.snowball import SnowballStemmer
    stemmer = SnowballStemmer("english")
    def tokenize_and_stem(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
        tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
        filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
        for token in tokens:
            if re.search('[a-zA-Z]', token):
                filtered_tokens.append(token)
        stems = [stemmer.stem(t) for t in filtered_tokens]
        return stems
    def tokenize_only(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
        tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
        filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
        for token in tokens:
            if re.search('[a-zA-Z]', token):
                filtered_tokens.append(token)
        return filtered_tokens
    totalvocab_stemmed = []
    totalvocab_tokenized = []
    for i in synopses:
        allwords_stemmed = tokenize_and_stem(i) #for each item in 'synopses', tokenize/stem
        totalvocab_stemmed.extend(allwords_stemmed) #extend the 'totalvocab_stemmed' list   
        allwords_tokenized = tokenize_only(i)
        totalvocab_tokenized.extend(allwords_tokenized)
    data={'stemmed':totalvocab_stemmed}
    frame=pd.DataFrame(data)
    frame.to_csv(output_text_path,index=False)
    data={'tokenized':totalvocab_tokenized}
    frame=pd.DataFrame(data)
    frame.to_csv(o2,index=False)
#clean('../t.csv','../t2.csv')
clean=create_component_from_func(clean,base_image='star16231108/python:3.7',output_component_file='../components/clean.yaml')
