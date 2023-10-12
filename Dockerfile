# Use an official Python runtime as a base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev libxml2-dev libxslt1-dev libssl-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the entire project into the container
COPY . /app/

# Install Python dependencies for Django and Scrapy
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose the ports for Django and Scrapyrt
EXPOSE 8000

# Start both Django development server and Scrapyrt server
CMD bash -c "python manage.py runserver 0.0.0.0:8000 & scrapyrt -p 9080 -i 0.0.0.0 & python scrape-scheduler/index.py"
