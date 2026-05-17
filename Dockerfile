FROM python:3.12
WORKDIR /usr/local/app

# Install the application dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Python script into the working directory
COPY etl.py .

# Setup non root user appuser
RUN useradd appuser
USER appuser

# Run the script
CMD ["python", "etl.py"]