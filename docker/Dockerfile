# Start from Python base image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy our files in
COPY fraud_model.py .
COPY app.py .

# Install Flask
RUN pip install flask

# Expose port 5000
EXPOSE 5000

# Run the app when container starts
CMD ["python3", "app.py"]
