# Official Python Image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the dependencies file to the container
COPY requirements.txt /app/requirements.txt 

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Specify the command to run the application
CMD ["uvicorn", "server.app:app"]