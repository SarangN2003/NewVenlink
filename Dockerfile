

######Final Docker file
#FROM python:3.12-slim
#
## Set environment variables for Chrome and ChromeDriver
#ENV CHROME_BIN=/usr/bin/chromium
#ENV CHROMEDRIVER_BIN=/usr/bin/chromedriver
#ENV PATH="/usr/local/bin:$PATH"
#
## Install required dependencies
#RUN apt-get update && apt-get install -y \
#    wget \
#    unzip \
#    curl \
#    chromium \
#    chromium-driver \
#    awscli \
#    fonts-liberation \
#    libappindicator3-1 \
#    libasound2 \
#    libatk-bridge2.0-0 \
#    libatk1.0-0 \
#    libcups2 \
#    libdbus-1-3 \
#    libxcomposite1 \
#    libxrandr2 \
#    libgbm1 \
#    dbus-x11 \
#    python3-cffi \
#    python3-brotli \
#    libpango-1.0-0 \
#    libharfbuzz0b \
#    libpangoft2-1.0-0 \
#    && rm -rf /var/lib/apt/lists/*
#
## Set working directory
#WORKDIR /test_NewLogin
#
## Copy application files
#COPY . .
#
## Install Python dependencies
#RUN pip install --no-cache-dir -r requirements.txt
#RUN pip install --no-cache-dir pytest pytest-html boto3 pillow fpdf2
#
## Set correct permissions for ChromeDriver
#RUN chmod +x /usr/bin/chromedriver
#
## Create directories inside the container
#RUN mkdir -p /test_NewLogin/reports && \
#    mkdir -p /test_NewLogin/screenshots && \
#    chmod -R 777 /test_NewLogin/reports && \
#    chmod -R 777 /test_NewLogin/screenshots
#
## Set AWS region
#ENV AWS_DEFAULT_REGION=eu-north-1
#
## Keep container alive (Prevents ECS Rollback due to early exit)
#CMD ["sh", "-c", " \
#    echo 'Starting test execution...'; \
#    pytest --maxfail=1 --disable-warnings -v -s test_NewLogin.py --html=/test_NewLogin/reports/report.html; \
#    TEST_EXIT_CODE=$?; \
#    echo 'Generating reports...'; \
#    python -c \"from weasyprint import HTML; HTML('/test_NewLogin/reports/report.html').write_pdf('/test_NewLogin/reports/report.pdf')\"; \
#    echo 'Uploading reports to S3...'; \
#    aws s3 cp /test_NewLogin/reports/report.pdf s3://venlinkfargatereport/reports/report.pdf --region $AWS_DEFAULT_REGION; \
#    aws s3 cp /test_NewLogin/screenshots/screenshots.pdf s3://venlinkfargatereport/reports/screenshots.pdf --region $AWS_DEFAULT_REGION; \
#    echo 'Test execution completed. Keeping container alive...'; \
#    tail -f /dev/null"]



################
FROM python:3.12-slim

# Set environment variables for Chrome and ChromeDriver
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_BIN=/usr/bin/chromedriver
ENV PATH="/usr/local/bin:$PATH"

# Install required dependencies
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    chromium \
    chromium-driver \
    awscli \
    fonts-liberation \
    libappindicator3-1 \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libdbus-1-3 \
    libxcomposite1 \
    libxrandr2 \
    libgbm1 \
    dbus-x11 \
    python3-cffi \
    python3-brotli \
    libpango-1.0-0 \
    libharfbuzz0b \
    libpangoft2-1.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /test_NewLogin

# Copy application files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir pytest pytest-html boto3 pillow fpdf2

# Set correct permissions for ChromeDriver
RUN chmod +x /usr/bin/chromedriver

# Create directories inside the container
RUN mkdir -p /test_NewLogin/reports && \
    mkdir -p /test_NewLogin/screenshots && \
    chmod -R 777 /test_NewLogin/reports && \
    chmod -R 777 /test_NewLogin/screenshots

# Set AWS region
ENV AWS_DEFAULT_REGION=eu-north-1

# Keep container alive (Prevents ECS Rollback due to early exit)
CMD ["sh", "-c", " \
    echo 'Starting test execution...'; \
    pytest --maxfail=1 --disable-warnings -v -s test_NewLogin.py --html=/test_NewLogin/reports/report.html; \
    TEST_EXIT_CODE=$?; \
    echo 'Generating reports...'; \
    python -c \"from weasyprint import HTML; HTML('/test_NewLogin/reports/report.html').write_pdf('/test_NewLogin/reports/report.pdf')\"; \
    echo 'Uploading reports to S3...'; \
    aws s3 cp /test_NewLogin/reports/report.pdf s3://venlinkfargatereport/reports/report.pdf --region $AWS_DEFAULT_REGION; \
    aws s3 cp /test_NewLogin/screenshots/screenshots.pdf s3://venlinkfargatereport/reports/screenshots.pdf --region $AWS_DEFAULT_REGION; \
    echo 'Test execution completed. Keeping container alive...'; \
    tail -f /dev/null"]
