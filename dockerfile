FROM python:3.11.3

RUN mkdir -p /root/.pip

RUN mkdir -p /root/Workspace/djangoPro

WORKDIR /root/Workspace/djangoPro

COPY . /root/Workspace/djangoPro
RUN mv /root/Workspace/djangoPro/pip.conf /root/.pip/

RUN pip3 install -r requments.txt

EXPOSE 8001

CMD ["uwsgi", "--http", ":8001", "--wsgi-file", "djangoPro/wsgi.py"]
