FROM python:3.12
WORKDIR /usr/local/app

# Install the application dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy in the source code
COPY etl.py ./src
EXPOSE 8080

# Setup an etl user so the container doesn't run as the root user
RUN useradd elt
USER etl

CMD ["py", "./src/etl.py"]