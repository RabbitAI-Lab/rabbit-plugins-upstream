# Iran Chemical Database — Dockerfile
# CRITICAL: httrack MUST be installed inside every container that crawls.
FROM python:3.11-slim-bookworm

RUN apt-get update && apt-get install -y --no-install-recommends \
    httrack \
    libhttrack-dev \
    # Playwright browser dependencies
    libnss3 libnspr4 libatk1.0-0 libatk-bridge2.0-0 \
    libcups2 libdrm2 libxkbcommon0 libxcomposite1 \
    libxdamage1 libxrandr2 libgbm1 libpango-1.0-0 \
    libasound2 libxshmfence1 \
    # PDF processing
    poppler-utils \
    # build deps
    gcc g++ \
    && rm -rf /var/lib/apt/lists/*

# Verify HTTrack installation
RUN httrack --version

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Playwright browser (Chromium) for the JS fallback layer
RUN playwright install --with-deps chromium

COPY . .

# Persistent HTTrack mirror store
RUN mkdir -p /var/lib/iran_chem_db/mirrors /var/log/iran_chem_db

CMD ["python", "-m", "src.main"]
