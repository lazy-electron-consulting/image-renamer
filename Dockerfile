# Use an official Python runtime as a parent image
FROM docker.io/library/python:3.12-alpine

# Set the working directory to /app
WORKDIR /app

# Create a non-root user and change ownership of /app to the appuser
RUN adduser -h /app -D appuser && chown -R appuser /app

# Switch to the appuser
USER appuser

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set the entry point to the script
ENTRYPOINT ["python", "rename.py"]
