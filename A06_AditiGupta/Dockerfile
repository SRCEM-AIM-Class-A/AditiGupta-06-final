# Use Python base image
FROM python:3.10

# Set the working directory
WORKDIR /usr/src/app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . .

# Expose port 8000
EXPOSE 8000

# Start the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
