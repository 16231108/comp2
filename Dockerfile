FROM python:3.7
COPY ./inst.txt /
RUN pip install -r /inst.txt