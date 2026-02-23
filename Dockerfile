# Use a lightweight base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    APP_HOME=/app

# Create a non-root user and group
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Set working directory
WORKDIR $APP_HOME

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY main.py .

# Change ownership of the application code to the non-root user
RUN chown -R appuser:appuser $APP_HOME

# Switch to the non-root user
USER appuser

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
