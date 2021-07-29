FROM python:3.7
COPY ./inst.txt /
RUN pip install -r /inst.txt && python -c "import nltk;nltk.download('punkt')"