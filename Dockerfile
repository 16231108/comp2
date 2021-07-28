FROM star16231108/python:3.7
COPY ./inst.txt /
RUN pip install -r /inst.txt