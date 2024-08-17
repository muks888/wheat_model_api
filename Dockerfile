# pull python base image
FROM python:3.10

RUN pwd
RUN ls -lrt

# copy application files
ADD . .

RUN pwd
RUN ls -lrt


# specify working directory
#WORKDIR /wheat_class_model_api

RUN pwd
RUN ls -lrt

# update pip
RUN pip install --upgrade pip

# install dependencies
RUN pip install -r ./requirements.txt

# expose port for application
EXPOSE 8005

# specify working directory
#WORKDIR /wheat_class_model_api

# start fastapi application
#CMD ["python", "app/main.py"]
CMD ["python", "app.py"]

RUN pwd
RUN ls -lrt