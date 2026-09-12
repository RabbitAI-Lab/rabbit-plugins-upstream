#!/usr/bin/env bash
# generate-dockerfile.sh - Generate a Dockerfile based on project detection results
# Usage: generate-dockerfile.sh <project-dir> [type] [framework] [port]
set -euo pipefail

PROJECT_DIR="${1:-.}"
DETECT_TYPE="${2:-}"
PORT="${3:-}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TEMPLATES_DIR="$SCRIPT_DIR/templates"
GENERATED_FILE="$PROJECT_DIR/Dockerfile"

# Source detection if not provided
if [ -z "$DETECT_TYPE" ] || [ "$DETECT_TYPE" = "unknown" ]; then
    while IFS='=' read -r key value; do
        case "$key" in
            TYPE)       DETECT_TYPE="$value" ;;
            FRAMEWORK)  DETECT_FRAMEWORK="$value" ;;
            PORT)       PORT="$value" ;;
        esac
    done < <(bash "$SCRIPT_DIR/detect-project.sh" "$PROJECT_DIR" 2>/dev/null | grep -E '^(TYPE|FRAMEWORK|PORT)=')
fi

[ -z "$PORT" ] && PORT="3000"

echo "━━━ Deploy-Agent: Dockerfile Generator ━━━━━"
echo "Type: ${DETECT_TYPE:-unknown} | Framework: ${DETECT_FRAMEWORK:-} | Port: $PORT"

# ── Already has Dockerfile ──
if [ -f "$PROJECT_DIR/Dockerfile" ]; then
    echo "[!] Dockerfile already exists — skipping generation."
    echo "$PROJECT_DIR/Dockerfile"
    exit 0
fi

# ── Docker Compose ──
for fn in docker-compose.yml docker-compose.yaml compose.yml compose.yaml; do
    [ -f "$PROJECT_DIR/$fn" ] && echo "$PROJECT_DIR/$fn" && exit 0
done

# ── Generate ──
case "${DETECT_TYPE%%-*}" in
    node)
        cat > "$GENERATED_FILE" <<- DOCKERFILE
		# ── Deploy-Agent: Node.js ──
		FROM node:20-alpine
		WORKDIR /app
		COPY package*.json ./
		RUN npm ci --only=production 2>/dev/null || npm install --production
		COPY . .
		ENV NODE_ENV=production
		ENV PORT=${PORT}
		EXPOSE ${PORT}
		HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \\
		    CMD wget --no-verbose --tries=1 --spider http://localhost:${PORT}/ || exit 1
		CMD ["node", "server.js"]
		DOCKERFILE
        ;;

    python)
        if [ -f "$PROJECT_DIR/manage.py" ]; then
            cat > "$GENERATED_FILE" <<- DOCKERFILE
			# ── Deploy-Agent: Django ──
			FROM python:3.11-slim
			WORKDIR /app
			ENV PYTHONDONTWRITEBYTECODE=1
			ENV PYTHONUNBUFFERED=1
			ENV PORT=${PORT}
			COPY requirements.txt* ./
			RUN pip install --no-cache-dir -r requirements.txt 2>/dev/null || true
			COPY . .
			COPY scripts/templates/entrypoint.django.sh /entrypoint.sh
			RUN chmod +x /entrypoint.sh
			EXPOSE ${PORT}
			HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \\
			    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:${PORT}/')" || exit 1
			ENTRYPOINT ["/entrypoint.sh"]
			DOCKERFILE
        else
            entrypoint="main.py"
            [ -f "$PROJECT_DIR/app.py" ] && entrypoint="app.py"
            cat > "$GENERATED_FILE" <<- DOCKERFILE
			# ── Deploy-Agent: Python ──
			FROM python:3.11-slim
			WORKDIR /app
			ENV PYTHONDONTWRITEBYTECODE=1
			ENV PYTHONUNBUFFERED=1
			ENV PORT=${PORT}
			COPY requirements.txt* ./
			RUN pip install --no-cache-dir -r requirements.txt 2>/dev/null || true
			COPY . .
			EXPOSE ${PORT}
			HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \\
			    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:${PORT}/')" || exit 1
			CMD ["python", "${entrypoint}"]
			DOCKERFILE
        fi
        ;;

    go)
        cat > "$GENERATED_FILE" <<- DOCKERFILE
		# ── Deploy-Agent: Go ──
		FROM golang:1.22-alpine AS builder
		WORKDIR /app
		COPY go.mod go.sum* ./
		RUN go mod download
		COPY . .
		RUN CGO_ENABLED=0 GOOS=linux go build -o /app/app .

		FROM alpine:3.19
		RUN apk add --no-cache ca-certificates tzdata
		WORKDIR /app
		ENV PORT=${PORT}
		COPY --from=builder /app/app .
		EXPOSE ${PORT}
		HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \\
		    CMD wget --no-verbose --tries=1 --spider http://localhost:${PORT}/ || exit 1
		CMD ["/app/app"]
		DOCKERFILE
        ;;

    rust)
        local binary_name
        binary_name=$(grep -E '^name\s*=' "$PROJECT_DIR/Cargo.toml" 2>/dev/null | head -1 | sed 's/.*= *"\(.*\)"/\1/')
        [ -z "$binary_name" ] && binary_name="app"
        cat > "$GENERATED_FILE" <<- DOCKERFILE
		# ── Deploy-Agent: Rust ──
		FROM rust:1.77-slim-bookworm AS builder
		WORKDIR /app
		COPY Cargo.toml Cargo.lock* ./
		RUN mkdir src && echo "fn main() {}" > src/main.rs
		RUN cargo build --release 2>/dev/null || true
		COPY . .
		RUN cargo build --release

		FROM debian:bookworm-slim
		RUN apt-get update && apt-get install -y ca-certificates && rm -rf /var/lib/apt/lists/*
		WORKDIR /app
		ENV PORT=${PORT}
		COPY --from=builder /app/target/release/${binary_name} .
		EXPOSE ${PORT}
		HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \\
		    CMD wget --no-verbose --tries=1 --spider http://localhost:${PORT}/ || exit 1
		CMD ["./${binary_name}"]
		DOCKERFILE
        ;;

    static|html)
        cat "$TEMPLATES_DIR/Dockerfile.static" > "$GENERATED_FILE"
        ;;

    java)
        cat "$TEMPLATES_DIR/Dockerfile.java" > "$GENERATED_FILE"
        ;;

    *)
        echo "[!] Unknown project type: ${DETECT_TYPE:-unknown}"
        echo "    Cannot auto-generate Dockerfile."
        exit 1
        ;;
esac

if [ -f "$GENERATED_FILE" ]; then
    echo "[✓] Dockerfile generated: $GENERATED_FILE"
else
    echo "[✗] Failed to generate Dockerfile."
    exit 1
fi
