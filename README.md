# Serving ML Models as Microservices - Streamlit, FastAPI, and Docker

This repo contains code for a small webapp to predict if passengers would have survived the Titanic disaster. The application consists of a frontend and a backend part and is used to demonstrate how to serve ML models as microservices through an API. The frontend is built with Streamlit and used to acquire passenger information from the user. The backend is built with the FastAPI framework and consists of 2 endpoints: `/preprocess/` used to preprocess the data and transform it into the format used by the model; `/predict/` to get the survival probability in percent as a response from the API. 

# How to run the Application

Both parts are containerized with Docker and combined via Docker-Compose. To run the app, simply clone the repo (or copy the docker-compose.yml) and run `docker-compose up` from the terminal. 
