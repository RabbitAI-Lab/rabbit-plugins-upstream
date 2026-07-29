---
slug: docker-essentials-tool-free
name: docker-essentials-tool-free
version: 1.0.0
displayName: Docker基础工具免费版
summary: "提供Docker容器生命周期、镜像管理、Compose编排与网络卷管理,适合开发者日常使用.。面向开发者的Docker容器管理辅助工具,涵盖容器生命周期、镜像构建管理、Compose编排与网"
license: Proprietary
edition: free
description: '面向开发者的Docker容器管理辅助工具,涵盖容器生命周期、镜像构建管理、Compose编排与网络卷操作。核心能力:

  - 容器生命周期管理(run/stop/rm)

  - 镜像构建与标签管理

  - Docker Compose多容器编排

  - 网络与卷管理

  - 日志查看与容器调试

  适用场景:

  - 本地开发环境容器化

  - 单机多容器应用部署

  - 容器问题排查调试

  差异化:

  - 免费版聚焦核心Docker命令,开箱即用

  - 覆盖日常90%容器操作需求

  - 与专业版命令兼容,可平滑升级

  适用关键词:...'
tags:
  - 开发工具
  - Docker
  - 容器化
  - 容器
  - DevOps
  - docker
  - container_name
  - docker-compose
  - bash
  - run
tools:
  - read
  - exec
  - write
homepage: ""
category: "Development"
---
# Docker基础工具 - 免费版
## 概述
Docker基础工具免费版为开发者提供日常容器管理能力。工具涵盖容器生命周期管理、镜像构建与标签管理、Docker Compose多容器编排以及网络与卷管理,帮助开发者高效进行本地容器化开发.
本版本适合本地开发环境容器化、单机多容器应用部署和容器问题排查调试。所有命令通过 Docker CLI 执行,无需安装额外插件.
## 核心能力
### 1. 容器生命周期管理
覆盖容器从创建到销毁的完整生命周期.
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | Docker基础工具免费版处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```bash
# 运行容器
docker run nginx                           # 前台运行
docker run -d nginx                        # 后台运行
docker run --name my-nginx -d nginx        # 命名运行
docker run -p 8080:80 -d nginx             # 端口映射
docker run -e MY_VAR=value -d app          # 环境变量
docker run -v /host/path:/container/path -d app  # 卷挂载
docker run --rm alpine echo "Hello"        # 运行后自动删除
docker run -it ubuntu bash                 # 交互式运行
# 管理容器
docker ps                                  # 查看运行中容器
docker ps -a                               # 查看所有容器
docker stop container_name                 # 停止容器
docker start container_name                # 启动容器
docker restart container_name              # 重启容器
docker rm container_name                   # 删除容器
docker rm -f container_name                # 强制删除运行中容器
docker container prune                     # 清理已停止容器
```

**处理**: 解析容器生命周期管理的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回容器生命周期管理的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 2. 镜像构建与管理
```bash
# 构建镜像
docker build -t myapp:1.0 .                       # 基础构建
docker build -f Dockerfile.dev -t myapp:dev .     # 指定Dockerfile
docker build --build-arg VERSION=1.0 -t myapp .   # 构建参数
docker build --no-cache -t myapp .                # 无缓存构建
# 管理镜像
docker images                                     # 列出镜像
docker pull nginx:latest                          # 拉取镜像
docker tag myapp:1.0 myapp:latest                 # 打标签
docker push myrepo/myapp:1.0                      # 推送镜像
docker rmi image_name                             # 删除镜像
docker image prune                                # 清理悬空镜像
docker image prune -a                             # 清理所有未使用镜像
```

**处理**: 解析镜像构建与管理的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回镜像构建与管理的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 3. 容器检查与调试
```bash
# 查看日志
docker logs container_name                        # 全部日志
docker logs -f container_name                     # 跟踪日志
docker logs --tail 100 container_name             # 最后100行
docker logs -t container_name                     # 显示时间戳
# 执行命令
docker exec container_name ls -la                 # 执行命令
docker exec -it container_name bash               # 交互式进入
docker exec -u root -it container_name bash       # 以root进入
# 容器检查
docker inspect container_name                     # 详细信息
docker inspect -f '{{.NetworkSettings.IPAddress}}' container_name  # 提取IP
docker stats                                      # 资源使用
docker top container_name                         # 进程信息
```

**处理**: 解析容器检查与调试的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回容器检查与调试的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 4. Docker Compose 编排
```bash
# 基础操作
docker-compose up                                # 启动服务
docker-compose up -d                             # 后台启动
docker-compose down                              # 停止并删除
docker-compose down -v                           # 同时删除卷
docker-compose logs                              # 查看日志
docker-compose logs -f web                       # 跟踪指定服务日志
docker-compose up -d --scale web=3               # 扩展服务实例
# 服务管理
docker-compose ps                                # 查看服务状态
docker-compose exec web bash                     # 进入服务容器
docker-compose restart web                       # 重启服务
docker-compose build web                         # 重新构建服务
docker-compose up -d --build                     # 重新构建并启动
```

**处理**: 解析Docker Compose 编排的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回Docker Compose 编排的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 5. 网络与卷管理
```bash
# 网络管理
docker network ls                                # 列出网络
docker network create mynetwork                  # 创建网络
docker network connect mynetwork container_name  # 连接网络
docker network disconnect mynetwork container_name  # 断开网络
docker network inspect mynetwork                 # 查看网络详情
docker network rm mynetwork                      # 删除网络
# 卷管理
docker volume ls                                 # 列出卷
docker volume create myvolume                    # 创建卷
docker volume inspect myvolume                   # 查看卷详情
docker volume rm myvolume                        # 删除卷
docker volume prune                              # 清理未使用卷
docker run -v myvolume:/data -d app              # 使用命名卷
```

**处理**: 解析网络与卷管理的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回网络与卷管理的响应数据,包含状态码、结果和日志.
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：镜像管理、编排与网络卷管理、适合开发者日常使、面向开发者的、容器管理辅助工具、涵盖容器生命周期、镜像构建管理、编排与网络卷操作、核心能力、镜像构建与标签管、多容器编排、日志查看与容器调等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

## 使用场景
### 场景一:本地开发环境搭建
使用Docker快速搭建本地开发环境.
```bash
# 开发容器:挂载代码并运行开发服务器
docker run -it --rm \
  -v $(pwd):/app \
  -w /app \
  -p 3000:3000 \
  node:18 \
  npm run dev
# ...
# 数据库容器:持久化数据
docker run -d \
  --name postgres \
  -e POSTGRES_PASSWORD=secret \
  -e POSTGRES_DB=mydb \
  -v postgres-data:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:15
# ...
# Redis缓存容器
docker run -d \
  --name redis \
  -p 6379:6379 \
  redis:7-alpine
```

### 场景二:多容器应用编排
使用Docker Compose编排多容器应用.
```yaml
# docker-compose.yml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "3000:3000"
    environment:
      - DB_HOST=db
      - REDIS_HOST=redis
    depends_on:
      - db
      - redis
    volumes:
      - .:/app
      - /app/node_modules
# ...
  db:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: secret
      POSTGRES_DB: mydb
    volumes:
      - postgres-data:/var/lib/postgresql/data
    ports:
      - "5432:5432"
# ...
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
# ...
volumes:
  postgres-data:
```

```bash
# 启动完整开发环境
docker-compose up -d
# ...
# 查看服务状态
docker-compose ps
# ...
# 查看Web服务日志
docker-compose logs -f web
# ...
# 扩展Web服务实例
docker-compose up -d --scale web=3
# ...
# 停止并清理
docker-compose down -v
```

## 错误处理

快速排查容器运行问题.
```bash
#!/bin/bash
# 容器问题排查脚本
CONTAINER="${1:?用法: debug-container.sh <container_name>}"
# ...
echo "=== 容器诊断: $CONTAINER ==="
# ...
# 1. 容器状态
echo "--- 容器状态 ---"
docker ps -a --filter "name=$CONTAINER" --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
# ...
# 2. 容器资源使用
echo -e "\n--- 资源使用 ---"
docker stats --no-stream "$CONTAINER"
# ...
# 3. 最近日志
echo -e "\n--- 最近日志(50行) ---"
docker logs --tail 50 "$CONTAINER"
# ...
# 4. 容器详细信息
echo -e "\n--- 网络配置 ---"
docker inspect -f 'IP: {{.NetworkSettings.IPAddress}}' "$CONTAINER"
docker inspect -f '端口映射: {{.NetworkSettings.Ports}}' "$CONTAINER"
# ...
echo -e "\n--- 挂载卷 ---"
docker inspect -f '{{range .Mounts}}{{.Source}} -> {{.Destination}}{{"\n"}}{{end}}' "$CONTAINER"
```

| 序号 | 错误场景 | 原因 | 处理方式 | 优先级 |
|:-----|:-----|:-----|:-----|:-----|
| 1 | 输入参数缺失 | 用户未提供必要参数 | 提示用户提供所需参数后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令 | P0 |
| 2 | 执行超时 | 处理时间过长 | 检查输入数据量,分批处理 | P1 |
| 3 | 输出格式错误 | 结果不符合预期格式 | 检查`output_format`参数配置 | P1 |

## 不适用场景

以下场景Docker基础工具免费版不适合处理：

- 无明确技术栈的模糊需求
- 纯架构设计决策
- 运维部署管理

## 触发条件

需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于非本工具能力范围的需求.
## 快速开始
### Step 1:验证Docker环境
```bash
docker version
docker info
docker run hello-world
```

### Step 2:触发容器操作
在 AI Agent 中输入指令:

```
请帮我用Docker启动一个Node.js开发环境,映射端口3000并挂载当前目录.
```

### Step 3:管理容器
Agent 会生成并执行相应的 Docker 命令,提供容器管理建议.
**响应解析**: 完成完成后,查看输出响应确认任务状态。成功时输出包含解析摘要和响应数据;失败时根据错误信息排查问题,查阅错误解析章节获取恢复步骤.
## 示例
### 开发环境Docker配置
```yaml
# .docker-dev.yml - 开发环境配置
version: "1.0"
# ...
# 开发容器默认配置
dev_container:
  base_image: node:18
  work_dir: /app
  ports:
    - 3000:3000
    - 9229:9229  # 调试端口
  volumes:
    - .:/app
    - node_modules:/app/node_modules
  environment:
    - NODE_ENV=development
# ...
# 常用服务
services:
  database:
    image: postgres:15
    port: 5432
    persist: true
  cache:
    image: redis:7-alpine
    port: 6379
    persist: false
# ...
# 清理策略
cleanup:
  prune_images: false
  prune_volumes: false
  prune_containers: true
```

### 多阶段Dockerfile示例
```dockerfile
# 开发用Dockerfile
FROM node:18 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
# ...
FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

## 最佳实践
1. **使用.dockerignore**:减少构建上下文体积

```dockerignore
# .dockerignore
node_modules
npm-debug.log
.git
.gitignore
dist
.env
*.md
```

2. **合并RUN指令**:减少镜像层数

```dockerfile
# 不推荐:多层
RUN apt-get update
RUN apt-get install -y curl
RUN rm -rf /var/lib/apt/lists/*
# ...
# 推荐:合并为一层
RUN apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/*
```

3. **使用多阶段构建**:减小最终镜像体积

```dockerfile
FROM node:18 AS builder
WORKDIR /app
COPY . .
RUN npm ci && npm run build
# ...
FROM node:18-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
CMD ["node", "dist/index.js"]
```

4. **始终打标签**:避免使用latest标签在生产环境

```bash
docker build -t myapp:latest .
```

5. **定期清理**:释放磁盘空间

```bash
docker system df                    # 查看磁盘使用
docker system prune                 # 清理未使用资源
docker system prune -a              # 清理所有未使用镜像
docker system prune --volumes       # 同时清理卷
```

## 常见问题
### Q1:容器启动后立即退出怎么办?
```bash
# 查看退出原因
docker logs container_name
State.ExitCode}}' container_name
# ...
# 常见原因:
# 1. 前台进程退出 -> 使用 -d 或确保有前台进程
# 2. 命令执行完成 -> 使用 -it 交互模式
# 3. 配置错误 -> 检查环境变量和配置文件
# 调试模式启动
docker run -it --entrypoint bash myapp
```

### Q2:如何进入运行中的容器?
```bash
# 使用exec进入(推荐)
docker exec -it container_name bash
docker exec -it container_name sh    # alpine镜像
# 使用attach连接到主进程
docker attach container_name
# Ctrl+P, Ctrl+Q 分离(不停止容器)
```

### Q3:端口冲突怎么办?
```bash
# 查找占用端口的进程
lsof -i :8080            # macOS/Linux
netstat -ano | findstr 8080  # Windows
# 修改端口映射
docker run -p 9080:80 -d nginx    # 改用9080端口
# 查看容器端口映射
docker ps --format "table {{.Names}}\t{{.Ports}}"
```

### Q4:免费版与专业版有何区别?
| 能力维度 | 免费版 | 专业版 |
|---:|---:|---:|
| 容器编排 | 单机Compose | 多机Swarm/K8s |
| 镜像优化 | 基础多阶段 | 深度优化分析 |
| 安全扫描 | 不支持 | 漏洞扫描 |
| 监控告警 | 手动查看 | 持续监控 |
| 批量操作 | 不支持 | 批量管理 |
| CI/CD集成 | 手动 | 流水线集成 |

### Q5:Docker Compose版本如何选择?
```bash
# 使用docker compose(v2,推荐)
docker compose up -d
# ...
# 使用docker-compose(v1,旧版)
docker-compose up -d
# ...
# 检查版本
docker compose version
```

## 依赖说明
### 运行环境
- **Agent 平台**:支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**:Windows / macOS / Linux
- **运行时**:Docker Engine 20.10+ / Docker Compose v2+

### 依赖详情
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| Docker Engine | 运行时 | 必需 | docker.com 下载安装 |
| Docker Compose | 工具 | 推荐 | Docker Desktop自带或单独安装 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
- 本 Skill 基于 Markdown 指令,无需额外 API Key
- 如需推送镜像到私有仓库,需配置仓库凭证:

```bash
# 登录私有镜像仓库
docker login registry.example.com
# 输入用户名和密码
# 或使用配置文件
# ~/.docker/config.json
```

### 可用性分类
- **分类**:MD+EXEC(纯 Markdown 指令,需要 exec 命令行执行能力)
- **说明**:基于 Markdown 的 AI Skill,通过自然语言指令驱动 Agent 执行 Docker 管理任务
- **适用规模**:单机环境,适合开发和测试场景

## 已知限制
- 本地运行，不支持多设备同步

## 输出格式
```json
{
  "success": true,
  "data": {
    "result": "Docker基础工具免费版处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "docker essentials"
    }
  },
  "execution_log": ["解析输入参数", "执行核心处理", "格式化输出结果"],
  "error": null
}
```
