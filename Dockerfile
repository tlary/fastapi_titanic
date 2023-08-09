# reduced python as base image
FROM python:3.8-slim-buster 

# set a directory for the app
WORKDIR /usr/src/api

# copy all the files to the container
COPY . . 

# pip install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# expose port 8000 
EXPOSE 8000

# command that is run when container is started
CMD ["uvicorn", "api:api", "--host=0.0.0.0"]
