from kfp.components import create_component_from_func
from kfp.components import  InputPath, OutputPath
def tag(text_path: InputPath(),output_text_path: OutputPath()):
    import pandas as pd
    import numpy as np
    import nltk
    import re
    synopses=pd.read_csv(text_path)
    synopses=synopses = np.array(synopses)
    synopses = synopses.ravel()
    from nltk.stem.snowball import SnowballStemmer
    stemmer = SnowballStemmer("english")
    nltk.download('punkt')
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
    from sklearn.feature_extraction.text import TfidfVectorizer
#define vectorizer parameters
    tfidf_vectorizer = TfidfVectorizer(stop_words='english',
                                 use_idf=True, tokenizer=tokenize_and_stem)
#%time：Time execution of a Python statement or expression. https://ipython.readthedocs.io/en/stable/interactive/magics.html
#%time tfidf_matrix = tfidf_vectorizer.fit_transform(synopses) #fit the vectorizer to synopses
    tfidf_matrix = tfidf_vectorizer.fit_transform(synopses)
    tfidf_matrix = tfidf_matrix.toarray()
    tfidf_matrix = [str(list(i)) for i in tfidf_matrix]
    data={'synopses':synopses,'tfidf_matrix':tfidf_matrix}
    data=pd.DataFrame(data)
    data.to_csv(output_text_path,index=False)
tag=create_component_from_func(
    tag,base_image='star16231108/python:3.7.1',output_component_file='../components/tag.yaml',
    )
#tag('../t.csv','tag.csv')