FROM python:3.13-slim

# Set working directory inside the container
WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Expose Django's default port
EXPOSE 8000

# Run development server (you can override this with docker-compose too)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
