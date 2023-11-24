# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Create a non-root user and change ownership of /app to the appuser
RUN useradd -m appuser && chown -R appuser /app

# Switch to the appuser
USER appuser

# Copy the current directory contents into the container at /app
COPY --chown=appuser:appuser . /app

# Set the HOME environment variable
ENV HOME /home/appuser

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set the entry point to the script
ENTRYPOINT ["python", "rename.py"]
