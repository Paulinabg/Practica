echo "FROM python" > Dockerfile
echo "RUN apt-get update" >> Dockerfile
echo "RUN apt-get -y install python3-pip" >> Dockerfile
echo "RUN pip install flask" >> Dockerfile
echo "COPY index.html /home/devasc/MIdocker/templates/" >> Dockerfile
echo "COPY conect.py /home/devasc/MIdocker/" >> Dockerfile
echo "EXPOSE 8000" >> Dockerfile
echo "CMD python3 /home/devasc/MIdocker/conect.py" >> Dockerfile
