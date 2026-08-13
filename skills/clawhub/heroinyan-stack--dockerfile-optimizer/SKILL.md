---
name: dockerfile-optimizer-security-scanner
version: "1.0.0"
category: devops
tags:
  - docker
  - dockerfile
  - container
  - security
  - optimization
  - best-practices
  - build-performance
  - supply-chain
model: claude-sonnet-4-20250514
trigger_keywords:
  - Dockerfile
  - docker build
  - container security
  - image optimization
  - layer caching
  - multi-stage build
  - docker scan
  - container hardening
  - image size
  - hadolint
pricing: "$9.99 one-time"
---

# Dockerfile Optimizer & Security Scanner

> **Optimize Dockerfiles for build speed, image size, and security.** Detects best practice violations, security issues, layer caching inefficiencies, and generates optimized multi-stage builds with CIS Docker Benchmark compliance.

## Why This Skill Exists

Bloated Docker images cost money (bandwidth, storage, slower deploys), insecure containers are the #1 cloud attack vector, and most teams copy-paste Dockerfiles without understanding them. This skill audits, optimizes, and hardens Dockerfiles with specific, actionable improvements.

## When to Activate

Activate when the user:
- Writes, reviews, or asks about a Dockerfile
- Wants to reduce Docker image size or build time
- Asks about container security or hardening
- Mentions multi-stage builds, layer caching, or build performance
- Has a Dockerfile failing CI or security scan
- Says "optimize my Dockerfile" or "is this Dockerfile secure"

## Workflow

### Step 1: Parse & Analyze Dockerfile

Read the Dockerfile and identify:
- Base image(s) and tags
- Layer order and caching opportunities
- Multi-stage build usage
- User context (root vs non-root)
- Exposed ports and volumes
- Health checks
- Build arguments and environment variables
- COPY/ADD instructions and .dockerignore coverage

### Step 2: Security Audit (CIS Docker Benchmark)

Check each rule and report violations:

| # | Rule | Severity | Check |
|---|------|----------|-------|
| 1 | Run as non-root user | 🔴 Critical | Is `USER` instruction present and not root? |
| 2 | Use specific base image tags | 🔴 Critical | Is base image pinned to specific version (not `latest`)? |
| 3 | No secrets in build args | 🔴 Critical | Are `ARG` values sensitive? Use Docker BuildKit secrets instead |
| 4 | Verify image signatures | 🟠 High | Is `COSIGN` or Notation verification used? |
| 5 | Use `.dockerignore` | 🟠 High | Does `.dockerignore` exist and exclude sensitive files? |
| 6 | Minimize installed packages | 🟠 High | Are package lists cleaned (`rm -rf /var/lib/apt/lists/*`)? |
| 7 | Set proper file permissions | 🟡 Warning | Are `COPY --chown` and `chmod` used correctly? |
| 8 | No `ADD` for remote URLs | 🟡 Warning | Use `COPY` for local files, `curl` for remote |
| 9 | Health check defined | 🟡 Warning | Is `HEALTHCHECK` instruction present? |
| 10 | No `sudo` in Dockerfile | 🟡 Warning | Is `sudo` used? Remove and use `USER` instead |
| 11 | Use digest pinning | 🔵 Suggestion | Pin base images by SHA256 digest for reproducibility |
| 12 | Label metadata | 🔵 Suggestion | Are OCI labels (`org.opencontainers.image.*`) present? |

### Step 3: Build Performance Optimization

#### Layer Caching Analysis
- Identify layers that change frequently and should be moved later
- Check if dependency files (package.json, requirements.txt, go.mod) are copied before source code
- Flag: `COPY . /app` before `RUN npm install` (invalidates cache on every code change)

#### Multi-Stage Build Detection
- If not using multi-stage: recommend it with specific stage structure
- If using multi-stage: check for unnecessary intermediate artifacts

#### Build Context Analysis
- Check `.dockerignore` for missing entries
- Calculate estimated build context size
- Flag large files/directories being sent to daemon

### Step 4: Image Size Optimization

| Optimization | Potential Saving | How |
|-------------|-----------------|-----|
| Use Alpine/slim base | 50-800MB | `python:3.12-slim` instead of `python:3.12` |
| Multi-stage build | 100-500MB | Builder stage with dev deps, runtime stage minimal |
| Clean package caches | 10-50MB | `rm -rf /var/lib/apt/lists/*` after apt-get |
| Combine RUN commands | 5-20MB | Each RUN creates a layer; combine to reduce layers |
| Use `.dockerignore` | Varies | Exclude node_modules, .git, test files, docs |
| Use `--no-install-recommends` | 10-100MB | For apt-get: skip recommended packages |

### Step 5: Generate Optimized Dockerfile

```dockerfile
# ===== Builder Stage =====
FROM python:3.12-slim AS builder

# Install build dependencies
RUN apt-get update && \
    apt-get install --no-install-recommends -y build-essential libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN useradd --create-home --uid 1000 appuser
WORKDIR /app

# Copy dependency files first (better caching)
COPY pyproject.toml poetry.lock ./

# Install dependencies to virtual env
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev --no-root

# ===== Runtime Stage =====
FROM python:3.12-slim AS runtime

# Install runtime dependencies only
RUN apt-get update && \
    apt-get install --no-install-recommends -y libpq5 curl && \
    rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN useradd --create-home --uid 1000 appuser
USER appuser
WORKDIR /app

# Copy virtual env from builder
COPY --from=builder --chown=appuser:appuser /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy application code
COPY --chown=appuser:appuser . .

# OCI labels
LABEL org.opencontainers.image.title="my-app" \
      org.opencontainers.image.version="1.0.0" \
      org.opencontainers.image.source="https://github.com/user/repo" \
      org.opencontainers.image.licenses="MIT"

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
```

### Step 6: Generate .dockerignore

```dockerignore
# Version control
.git
.gitignore

# Dependencies (installed in container)
node_modules
__pycache__
*.pyc
.venv
venv

# Test & docs
tests
test
docs
*.md
LICENSE

# CI/CD
.github
.gitlab-ci.yml
Dockerfile
docker-compose*.yml

# IDE
.idea
.vscode
*.swp

# Env & secrets
.env
.env.*
*.pem
*.key
```

### Step 7: Generate Report

```markdown
# 🐳 Dockerfile Audit Report

## Summary

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| Image size | ~850MB | ~180MB | 79% smaller |
| Build time (cached) | 45s | 12s | 73% faster |
| Security issues | 5 | 0 | All fixed |
| CIS violations | 4 | 0 | All compliant |

## Security Findings
[... findings from Step 2 ...]

## Optimization Changes
[... findings from Steps 3-4 ...]

## Optimized Dockerfile
[... generated Dockerfile ...]

## .dockerignore
[... generated .dockerignore ...]
```

## Output Constraints

- Always provide before/after comparison
- Optimized Dockerfile must be copy-paste ready
- Every change must explain WHY it's better, not just WHAT changed
- Security findings must include severity and CIS Benchmark reference
- Image size estimates based on common base image sizes
- Never recommend `:latest` tag — always pin to specific version

## What This Skill Does NOT Do

- Does not build or run the Docker image
- Does not scan running containers (only Dockerfile analysis)
- Does not manage Docker Compose or Kubernetes manifests (use separate skill)
- Does not handle Windows containers (Linux containers only)
