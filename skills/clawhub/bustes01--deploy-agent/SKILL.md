# Deploy-Agent Skill

Local deployment agent that auto-detects project types and deploys them via Docker. Default workflow: detect → Dockerfile generate → build → deploy.

## Architecture

```
skills/deploy-agent/
├── SKILL.md                          ← This file (instructions for OpenClaw agent)
├── scripts/
│   ├── deploy-agent.sh               ← Main orchestrator (all-in-one CLI)
│   ├── bootstrap-docker.sh           ← Install Docker Engine + Compose
│   ├── detect-project.sh             ← Auto-detect project type
│   ├── generate-dockerfile.sh        ← Generate Dockerfile dynamically
│   └── templates/
│       ├── Dockerfile.node           ← Node.js template
│       ├── Dockerfile.python         ← Python/Django template
│       ├── Dockerfile.go             ← Go template
│       ├── Dockerfile.static         ← Static Nginx template
│       ├── Dockerfile.java           ← Java Maven template
│       └── entrypoint.django.sh      ← Django entrypoint (migration + run)
```

## Capabilities

| Feature | Description |
|---|---|
| **Auto-detect** | Identifies project type from file structure (Node.js, Python, Go, Rust, static HTML, Java, etc.) |
| **Docker auto-gen** | Generates Dockerfile if none exists |
| **Compose native** | Detects docker-compose.yml and deploys with compose |
| **Smart ports** | Auto-detects project port and finds next available |
| **Health checks** | Built-in HEALTHCHECK in every generated Dockerfile |
| **Restart policy** | Containers set to `--restart unless-stopped` |
| **Managed tracking** | All containers labeled with `deploy-agent.managed=true` |

## Supported Project Types

- **Node.js** — npm, yarn, pnpm; frameworks: Express, Fastify, NestJS, Next.js, Nuxt, SvelteKit, Astro, Vite
- **Python** — pip, pipenv, poetry; frameworks: Django, Flask, FastAPI
- **Go** — go.mod detection, multi-stage build
- **Rust** — Cargo.toml, multi-stage build
- **Static HTML** — nginx-alpine serve
- **Java** — Maven (pom.xml), multi-stage
- **Docker Compose** — native support
- **Ruby/Rails, PHP/Laravel, Deno** — basic detection (Dockerfile under development)

## Usage (CLI)

```bash
# 1. Install Docker (first time only)
bash scripts/deploy-agent.sh install-docker

# 2. Detect a project
bash scripts/deploy-agent.sh detect ~/my-project

# 3. Deploy (auto-detect, generate Dockerfile, build, run)
bash scripts/deploy-agent.sh deploy ~/my-project

# 4. Deploy with specific port
bash scripts/deploy-agent.sh deploy ~/my-project 8080

# 5. List managed containers
bash scripts/deploy-agent.sh status

# 6. Stop a container
bash scripts/deploy-agent.sh stop my-project

# 7. View logs
bash scripts/deploy-agent.sh logs my-project
```

## Usage (OpenClaw Agent — this file)

When the user says "帮我部署这个项目" or provides a project path:

### Step 1: Resolve project path
The project path may come as:
- A local path (e.g. `~/projects/my-app`)
- A git URL (e.g. `https://github.com/user/repo.git`)
- A zip/tar archive (extract first)
- An attached file/folder (use the provided path)

### Step 2: Check Docker availability
```bash
# If Docker not available, install
bash <skill_dir>/scripts/bootstrap-docker.sh
```

### Step 3: Detect project
Read detection output, confirm with user if ambiguous:
```bash
bash <skill_dir>/scripts/detect-project.sh <project_dir>
```

### Step 4: Deploy
```bash
bash <skill_dir>/scripts/deploy-agent.sh deploy <project_dir>
```

### Step 5: Report results
Tell the user:
- Project type detected
- Port the service is running on
- Container name
- How to access (http://host:port)
- How to stop / view logs

### Uploaded projects
When user uploads project files:
1. Determine where files landed (check `/tmp/`, `~/Downloads/`, workspace paths)
2. If it's a single archive (zip/tar.gz), extract it
3. Run detection on the extracted/landed directory
4. If it has Dockerfile → build+deploy
5. If docker-compose → compose up
6. If detectable (Node/Python/Go/etc) → generate Dockerfile, build, deploy
7. If unknown → tell user what was found and ask for guidance

### Edge Cases
- **Port conflict**: If the port is already in use, deploy-agent auto-increments to find a free port
- **Permission denied**: User may need `sudo usermod -aG docker $USER` or `newgrp docker`
- **Large projects**: Node.js `node_modules` already present → COPY will be large. Suggest .dockerignore generation
- **PostgreSQL/Redis dependencies**: If the project needs databases, generate a docker-compose.yml instead

## Script Reference

### deploy-agent.sh
Main CLI: `deploy-agent.sh <command> [args]`
Commands: `install-docker`, `detect`, `generate`, `build`, `deploy`, `status`, `stop`, `logs`

### bootstrap-docker.sh
Idempotent Docker Engine + Compose Plugin installation for Ubuntu/Debian.
Safe to run multiple times.

### detect-project.sh
Scans project directory structure, outputs TYPE, FRAMEWORK, BUILD_CMD, RUN_CMD, PORT.
Exit codes: 0 = detected, 1 = unknown.

### generate-dockerfile.sh
Reads detection output, selects template, writes Dockerfile.
Skips if Dockerfile/docker-compose.yml already exists.

## Container Management

All deploy-agent containers are labeled:
- `deploy-agent.managed=true`
- `deploy-agent.source=<absolute-source-dir>`

To clean up all:
```bash
docker rm -f $(docker ps -aq --filter "label=deploy-agent.managed=true")
```

## ⚖️ 权限声明

| 权限 | 范围 | 用途 | 说明 |
|------|------|------|------|
| 执行 | sudo | Docker 安装、用户组管理 | `bootstrap-docker.sh` 安装 Docker |
| 执行 | docker | 容器管理 | 构建、运行、停止容器 |
| 文件系统 | 读取 | 项目目录 | 检测项目类型、读取构建配置 |
| 文件系统 | 写入 | 项目目录 | 生成 Dockerfile |
| 网络 | 出站 | Docker Hub / 镜像源 | 拉取基础镜像 |
| 网络 | 端口绑定 | 宿主机端口 | 容器端口映射，检测可用端口 |

> ⚠️ 除非使用 `install-docker` 命令，否则不需要 sudo 权限。Docker 操作建议通过 `docker` 用户组运行。
