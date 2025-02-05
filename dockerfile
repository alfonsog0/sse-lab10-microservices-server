# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app into the container
COPY . .

# Expose the port Flask runs on
EXPOSE 8080

# Command to run the app
CMD ["python", "app.py"]