# Use Red Hat Universal Base Image (UBI) as the base
FROM registry.access.redhat.com/ubi8/python-39

# Set the working directory
WORKDIR /app

# Copy application files
COPY . /app

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Set environment variables
ENV FLASK_APP=app/main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production

# Expose application port
EXPOSE 5000

# Run the application
CMD ["flask", "run"]
