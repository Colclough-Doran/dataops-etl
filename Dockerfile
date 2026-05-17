FROM aws/codebuild/amazonlinux-x86_64-standard:6.0

WORKDIR /usr/local/app

# Install Python 3.12 (if not already available)
RUN yum install -y python3.12 && \
    alternatives --set python /usr/bin/python3.12

# Install the application dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy in the source code
COPY etl.py ./src
EXPOSE 8080

# Setup appuser user so the container doesn't run as the root user
RUN groupadd -g 1001 appgroup && \
    useradd -u 1001 -g 1001 -m -d /usr/local/app -s /bin/bash appuser
USER appuser

CMD ["python", "./src/etl.py"]