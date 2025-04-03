# Use Python base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy application files
COPY app.py requirements.txt /app/

# Install dependencies
RUN pip install -r requirements.txt

# Expose the application port
EXPOSE 5000

# Start the app
CMD ["python", "app.py"]
