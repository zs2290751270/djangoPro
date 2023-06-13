FROM python:3.9.13

RUN mkdir -p /root/.pip

RUN mkdir -p /root/Workspace/djangoPro
COPY . /root/Workspace/djangoPro
RUN mv /root/Workspace/djangoPro/pip.conf /root/.pip/

RUN pip3 install -r /root/Workspace/djangoPro/requment.txt

CMD ["/root/Workspace/djangoPro/python", "manage.py", "runserver", "0.0.0.0:8088"]
 