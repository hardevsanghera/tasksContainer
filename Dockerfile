FROM ubuntu:24.04
#FROM ubuntu/python:3.12-24.04_stable

ENV PATH="/scripts:${PATH}"

COPY ./requirements.txt requirements.txt
RUN echo 'APT::Install-Suggests "0";' >> /etc/apt/apt.conf.d/000-docker
RUN echo 'APT::Install-Recommends "0";' >> /etc/apt/apt.conf.d/00-docker
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y gcc gnupg python3 python3-pip python3-dev unixodbc python3-venv curl
RUN curl -s https://packages.microsoft.com/keys/microsoft.asc |  gpg --dearmor -o /usr/share/keyrings/microsoft-prod.gpg &&\
    curl -s https://packages.microsoft.com/config/ubuntu/24.04/prod.list | tee /etc/apt/sources.list.d/mssql-release.list &&\
    #sed -i s/\#\$nrconf{restart} = 'i'/\$nrconf{restart} = 'a'/ /etc/needrestart/needrestart.conf &&\
    apt-get update &&\
    ACCEPT_EULA=Y apt-get install -y msodbcsql18 &&\
    ACCEPT_EULA=Y apt-get install -y mssql-tools18 &&\
    #echo export PATH=$PATH:/opt/mssql-tools18/bin >> ~/.bashrc &&\
    PATH=$PATH:/opt/mssql-tools18/bin
    #source ~/.bashrc
#RUN apt install -y 
#RUN DEBIAN_FRONTEND=noninteractive apt-get install -y unixodbc curl
COPY ./requirements.txt /requirements.txt
#RUN python3 -m pip install --upgrade pip --break-system-packages
RUN pip install --break-system-packages -r /requirements.txt

RUN mkdir /prodTasksProj
COPY . /prodTasksProj
WORKDIR /prodTasksProj
RUN mkdir /scripts
COPY ./scripts /scripts

RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN useradd -M -p PASS -s /bin/bash webadmin
RUN chown -R webadmin:webadmin /vol
RUN chown -R webadmin:webadmin /prodTasksProj
RUN chmod -R 755 /vol/web
USER webadmin

#EXPOSE 8000

CMD ["entrypoint.sh"]
#CMD [sh -c "python3 manage.py migrate"]