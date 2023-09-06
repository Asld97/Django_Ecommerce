# Chose the image
FROM python:3.9 
# Stream python output to terminal
ENV PYTHONUNBUFFERED=1
# Wroking directory inside image
WORKDIR /django_ecommerce
# Copy the requirements file into image
COPY requirements.txt requirements.txt
# Install copied files
RUN pip3 install -r requirements.txt
