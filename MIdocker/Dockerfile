FROM python
RUN apt-get update
RUN apt-get -y install python3-pip
RUN pip install flask
COPY index.html /home/devasc/MIdocker/templates/
COPY conect.py /home/devasc/MIdocker/
EXPOSE 8000
CMD python3 /home/devasc/MIdocker/conect.py
