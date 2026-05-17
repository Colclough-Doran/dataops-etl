FROM python:3.15
WORKDIR /usr/local/app

# Install the application dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy in the source code
COPY etl.py ./src
EXPOSE 8080

# Setup appuser user so the container doesn't run as the root user
RUN addgroup -g 1001 appgroup && adduser -D -u 1001 -g 1001 -G appgroup appuser
USER appuser

CMD ["py", "./src/etl.py"]