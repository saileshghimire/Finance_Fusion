FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirement.txt .
RUN pip install --no-cache-dir -r requirement.txt

# Copy the application code to the container
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Run the development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
