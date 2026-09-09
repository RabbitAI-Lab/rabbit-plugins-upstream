#!/usr/bin/env bash
# deploy-agent.sh - Main orchestrator: detect, build, and deploy projects via Docker
# Usage: deploy-agent.sh <command> [options]
#
# Commands:
#   install-docker     Install Docker + Compose on this host
#   detect <dir>       Detect project type and generate report
#   generate <dir>     Generate Dockerfile for the project
#   build <dir>        Build Docker image
#   deploy <dir>       Build + deploy as container
#   status             List all running deploy-agent containers
#   stop <name|id>     Stop a running container
#   logs <name|id>     View logs of a container
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

# Colors
RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'; CYAN='\033[0;36m'; NC='\033[0m'
info() { echo -e "${CYAN}[INFO]${NC} $1"; }
ok()   { echo -e "${GREEN}[✓]${NC} $1"; }
warn() { echo -e "${YELLOW}[!]${NC} $1"; }
err()  { echo -e "${RED}[✗]${NC} $1"; }
die()  { err "$1"; exit 1; }

# ── Container name from project dir ──
container_name() {
    local dir="$1"
    basename "$(cd "$dir" 2>/dev/null && pwd || echo "$dir")" | tr '[:upper:]' '[:lower:]' | tr -cd 'a-z0-9_-'
}

# ── Check Docker (with helpful install message) ──
require_docker() {
    if ! command -v docker &>/dev/null; then
        warn "Docker is not installed. Run: deploy-agent.sh install-docker"
        warn "Or: bash $SCRIPT_DIR/bootstrap-docker.sh"
        return 1
    fi
    if ! docker info &>/dev/null; then
        warn "Docker daemon not running or user not in docker group."
        warn "Try: sudo systemctl start docker"
        warn "Then: newgrp docker (or re-login)"
        return 1
    fi
}

# ── Install Docker ──
cmd_install_docker() {
    echo "━━━ Deploy-Agent: Docker Installation ━━━━━"
    bash "$SCRIPT_DIR/bootstrap-docker.sh"
}

# ── Detect project ──
cmd_detect() {
    local dir="${1:-.}"
    [ -d "$dir" ] || die "Directory not found: $dir"
    echo "━━━ Deploy-Agent: Project Detection ━━━━━"
    bash "$SCRIPT_DIR/detect-project.sh "$dir""
}

# ── Generate Dockerfile ──
cmd_generate() {
    local dir="${1:-.}"
    [ -d "$dir" ] || die "Directory not found: $dir"
    echo "━━━ Deploy-Agent: Dockerfile Generation ━━━━━"
    bash "$SCRIPT_DIR/generate-dockerfile.sh "$dir""
}

# ── Build image ──
cmd_build() {
    local dir="${1:-.}"
    [ -d "$dir" ] || die "Directory not found: $dir"
    require_docker || exit 1

    local name
    name="$(container_name "$dir")"
    local tag="deploy-agent/$name:latest"

    # Generate Dockerfile if not exists
    if [ ! -f "$dir/Dockerfile" ]; then
        local compose_files=("docker-compose.yml" "docker-compose.yaml" "compose.yml" "compose.yaml")
        local has_compose=false
        for cf in "${compose_files[@]}"; do [ -f "$dir/$cf" ] && has_compose=true && break; done
        if [ "$has_compose" = true ]; then
            ok "Docker Compose project detected. Building with compose..."
            docker compose -f "$dir/$cf" build
            return $?
        fi
        info "No Dockerfile found. Attempting auto-generation..."
        bash "$SCRIPT_DIR/generate-dockerfile.sh "$dir"" || die "Failed to generate Dockerfile"
    fi

    echo "━━━ Deploy-Agent: Building Image ━━━━━"
    info "Tag: $tag"
    cd "$dir"
    docker build -t "$tag" -f Dockerfile . 2>&1 | while IFS= read -r line; do echo "  $line"; done
    local status=${PIPESTATUS[0]}
    [ "$status" -eq 0 ] && ok "Build successful: $tag" || die "Build failed (exit $status)"
    echo "$tag"
}

# ── Deploy (build + run container) ──
cmd_deploy() {
    local dir="${1:-.}"
    local port="${2:-auto}"
    [ -d "$dir" ] || die "Directory not found: $dir"
    require_docker || exit 1

    local name
    name="$(container_name "$dir")"

    # Check for docker-compose
    local compose_file=""
    for cf in docker-compose.yml docker-compose.yaml compose.yml compose.yaml; do
        [ -f "$dir/$cf" ] && compose_file="$dir/$cf" && break
    done

    if [ -n "$compose_file" ]; then
        echo "━━━ Deploy-Agent: Deploy with Docker Compose ━━━━━"
        info "Compose file: $compose_file"
        # Stop existing if running
        docker compose -f "$compose_file" -p "$name" down 2>/dev/null || true
        docker compose -f "$compose_file" -p "$name" up -d --build 2>&1 | while IFS= read -r line; do echo "  $line"; done
        local status=${PIPESTATUS[0]}
        if [ "$status" -eq 0 ]; then
            ok "Deployment successful: $name"
            docker compose -f "$compose_file" -p "$name" ps
        else
            die "Compose deployment failed (exit $status)"
        fi
        return "$status"
    fi

    # Build first
    local tag
    tag="$(cmd_build "$dir")"
    [ -z "$tag" ] && die "Build failed, cannot deploy"

    # Determine port mapping
    if [ "$port" = "auto" ]; then
        # Try to detect from project
        source <(bash "$SCRIPT_DIR/detect-project.sh" "$dir" 2>/dev/null | grep '^PORT=' || echo "PORT=3000")
        port="${PORT:-3000}"
        # Find available port (start from detected port, increment if taken)
        local try_port="$port"
        while ss -tlnp 2>/dev/null | grep -q ":$try_port " || lsof -i ":$try_port" 2>/dev/null | grep -q LISTEN; do
            try_port=$((try_port + 1))
        done
        port="$try_port"
    fi

    echo "━━━ Deploy-Agent: Starting Container ━━━━━"
    info "Image: $tag"
    info "Container: $name"
    info "Port mapping: $port -> $port"

    # Stop and remove existing container with same name
    docker stop "$name" 2>/dev/null || true
    docker rm "$name" 2>/dev/null || true

    # Run
    docker run -d \
        --name "$name" \
        --restart unless-stopped \
        -p "$port:$port" \
        -e "PORT=$port" \
        -e "NODE_ENV=production" \
        --label "deploy-agent.managed=true" \
        --label "deploy-agent.source=$(cd "$dir" && pwd)" \
        "$tag" 2>&1 | while IFS= read -r line; do echo "  $line"; done

    local status=${PIPESTATUS[0]}
    if [ "$status" -eq 0 ]; then
        echo ""
        ok "${name} is running!"
        echo ""
        echo "   Access: http://localhost:${port}"
        echo "   Container: docker ps --filter name=${name}"
        echo "   Logs: deploy-agent.sh logs ${name}"
        echo "   Stop: deploy-agent.sh stop ${name}"
        echo ""
    else
        die "Container failed to start (exit $status)"
    fi
}

# ── Status ──
cmd_status() {
    require_docker 2>/dev/null || { warn "Docker not available"; return 1; }
    echo "━━━ Deploy-Agent: Managed Containers ━━━━━"
    local containers
    containers=$(docker ps -a --filter "label=deploy-agent.managed=true" --format "table {{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}" 2>/dev/null)
    if [ -z "$containers" ]; then
        echo "  No managed containers."
        echo ""
        echo "  All running containers:"
        docker ps --format "table {{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}" 2>/dev/null || true
    else
        echo "$containers"
        echo ""
        echo "  (Showing only deploy-agent managed containers)"
    fi
}

# ── Stop ──
cmd_stop() {
    local target="${1:-}"
    [ -z "$target" ] && die "Usage: deploy-agent.sh stop <container-name>"
    require_docker || exit 1
    echo "━━━ Deploy-Agent: Stopping Container ━━━━━"
    docker stop "$target" 2>/dev/null || warn "Container '$target' not running"
    docker rm "$target" 2>/dev/null || true
    ok "Container '$target' stopped and removed"
}

# ── Logs ──
cmd_logs() {
    local target="${1:-}"
    [ -z "$target" ] && die "Usage: deploy-agent.sh logs <container-name>"
    require_docker || exit 1
    docker logs -f --tail 50 "$target"
}

# ── Main dispatch ──
cmd="${1:-help}"
shift 2>/dev/null || true

case "$cmd" in
    install-docker|install)
        cmd_install_docker
        ;;
    detect)
        cmd_detect "${1:-.}"
        ;;
    generate|gen)
        cmd_generate "${1:-.}"
        ;;
    build)
        cmd_build "${1:-.}"
        ;;
    deploy|up)
        cmd_deploy "${1:-.}" "${2:-auto}"
        ;;
    status|ps|list)
        cmd_status
        ;;
    stop|down|kill)
        cmd_stop "${1:-}"
        ;;
    logs)
        cmd_logs "${1:-}"
        ;;
    help|--help|-h)
        echo "━━━ Deploy-Agent ━━━━━━━━━━━━━━━━━━━━━━━━━━━"
        echo "Usage: deploy-agent.sh <command> [options]"
        echo ""
        echo "Commands:"
        echo "  install-docker       Install Docker + Compose"
        echo "  detect <dir>         Detect project type"
        echo "  generate <dir>       Generate Dockerfile"
        echo "  build <dir>          Build Docker image"
        echo "  deploy <dir> [port]  Build + Deploy container"
        echo "  status               List managed containers"
        echo "  stop <name>          Stop & remove container"
        echo "  logs <name>          Follow container logs"
        echo ""
        echo "Examples:"
        echo "  deploy-agent.sh detect ./my-project"
        echo "  deploy-agent.sh deploy ./my-app 3000"
        echo "  deploy-agent.sh deploy ./next-app auto"
        echo "  deploy-agent.sh status"
        echo "  deploy-agent.sh logs my-app"
        ;;
    *)
        die "Unknown command: $cmd. See deploy-agent.sh help"
        ;;
esac
