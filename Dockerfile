FROM python:3.6

RUN apt-get update -y
RUN apt-get install -y build-essential vim libssl-dev

EXPOSE 5000

WORKDIR /app
ADD ./requirements.txt /app/requirements.txt

RUN python -m easy_install --upgrade pyOpenSSL

RUN pip install -r requirements.txt

#ENTRYPOINT ["python"]
#CMD ["bash"]

CMD ["python","run.py"]
