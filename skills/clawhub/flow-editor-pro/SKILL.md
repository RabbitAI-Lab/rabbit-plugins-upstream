---
slug: flow-editor-pro
name: flow-editor-pro
version: "1.0.0"
displayName: 流程编辑专家
summary: 解决Node-RED无版本管理、部署易翻车、多实例难管痛点，带回滚与安全加固的流程运维
license: MIT
description: |-
  通过 Admin API 或 CLI 管理 Node-RED 实例的运维专家。聚焦流程部署可回滚、多实例统一管理、
  节点依赖可治理、Context 持久化与安全加固，解决无版本控制、部署即翻车、多实例配置散乱痛点。

  核心能力:
  - 流程全生命周期：列表/部署/更新/删除/状态快照/回滚（每次部署自动留版本）
  - 节点依赖治理：装/禁/启/卸 + 兼容性检查 + 批量升级
  - Context 持久化：flow/global 上下文读写 + 备份导出
  - 多实例管理：单配置中心管理多个 Node-RED 实例（生产/预发/开发）
  - 安全加固：默认凭证校验、Admin API 鉴权检查、危险节点告警

  适用场景:
  - IoT/家居自动化 Node-RED 流程的版本化运维
  - 企业内部多实例 Node-RED 集中管理
  - 流程变更需可审计、可回滚的生产环境
  - 灾备：备份/恢复与跨实例迁移

  差异化:
  - 部署自动留版本 + 一键回滚，原版只有 backup 无版本树
  - 多实例配置中心，原版单实例硬编码 URL
  - 节点兼容性检查与危险节点告警，原版只给装/卸命令
  - 安全加固清单，原版无安全章节

  触发关键词: node-red, nodered, flow, 流程, 部署, 回滚, 节点管理, iot, 自动化, admin api
tags:
- 自动化
- 运维
- 物联网
tools:
- read
- exec
---

# 流程编辑专家

通过 Admin API 与 CLI 管理 Node-RED 实例，把"部署即翻车"变为"可回滚、可审计、可治理"的运维流程。

## 多实例配置中心

替代原版单实例硬编码，单文件管多实例：

```bash
# .env（按实例分块）
NR_PROD_URL=https://flow.example.com
NR_PROD_USERNAME=admin
NR_PROD_PASSWORD=${NR_PROD_PASSWORD}

NR_STAGING_URL=http://staging.internal:1880
NR_STAGING_USERNAME=admin
NR_STAGING_PASSWORD=${NR_STAGING_PASSWORD}

NR_DEV_URL=http://localhost:1880
NR_DEV_USERNAME=
NR_DEV_PASSWORD=
```

CLI 通过 `--instance` 切换，默认 `dev`：

```bash
scripts/nr --instance prod list-flows
scripts/nr --instance staging deploy --file watchdog.json
```

兼容旧变量 `NR_URL` / `NR_USER` / `NR_PASS`（默认实例）。

## 快速开始

1. 复制 `.env.example` 到 `.env`，按实例填入 URL/账号/密码
2. `scripts/nr doctor` — 验证实例连通性与权限
3. `scripts/nr --instance dev list-flows` — 列出流程
4. `scripts/nr deploy --file my-flow.json` — 部署（自动留版本）

## 流程管理（含版本与回滚）

```bash
# 列表与详情
scripts/nr list-flows
scripts/nr get-flow <flow-id>
scripts/nr get-flow-state

# 部署（自动留版本到 .versions/<flow-id>/<timestamp>.json）
scripts/nr deploy --file assets/flows/watchdog.json
scripts/nr deploy --file my-flow.json --instance prod   # 部署到生产

# 更新与删除
scripts/nr update-flow <flow-id> --file updated-flow.json
scripts/nr delete-flow <flow-id>

# 版本树与回滚
scripts/nr list-versions <flow-id>           # 列出该流程所有历史版本
scripts/nr rollback <flow-id> --to <timestamp>   # 回滚到指定版本
scripts/nr rollback <flow-id> --last         # 快速回滚到上一版本

# 状态快照
scripts/nr get-flow-state
scripts/nr set-flow-state --file state.json
```

**部署安全流程**：
1. 先 `--instance staging deploy` 部署到预发
2. 验证无误后 `--instance prod deploy`
3. 生产出问题 → `rollback --last`（< 5 秒回滚）

## 备份与恢复

```bash
# 全量备份（所有流程 + Context + 节点清单）
scripts/nr backup
scripts/nr backup --output my-backup.json
scripts/nr backup --instance prod --include-context

# 跨实例迁移
scripts/nr backup --instance prod --output prod-snapshot.json
scripts/nr restore prod-snapshot.json --instance staging

# 定时备份（建议加入 cron）
scripts/nr backup --schedule "0 2 * * *"   # 每日 2 点
```

备份内容：flows、credentials（加密）、context（flow/global）、节点清单、settings。

## 节点管理（含兼容性检查）

```bash
# 列表与详情
scripts/nr list-nodes
scripts/nr get-node node-red-contrib-http-request

# 安装（自动检查 Node-RED 版本兼容性）
scripts/nr install-node node-red-contrib-http-request
scripts/nr install-node node-red-contrib-influxdb --version 0.5.0

# 启用/禁用/卸载
scripts/nr enable-node node-red-contrib-http-request
scripts/nr disable-node node-red-contrib-http-request
scripts/nr remove-node node-red-contrib-http-request

# 批量升级
scripts/nr upgrade-nodes --all               # 升级所有过期节点
scripts/nr upgrade-nodes --outdated-only     # 仅升级有新版的
```

**兼容性检查**：安装/升级前自动比对节点要求的 Node-RED 版本与当前版本，不兼容则告警并中止。

**危险节点告警**：以下节点安装时强制提示风险：
- 已知有安全漏洞的版本（CVE 库匹配）
- 需要文件系统写权限的节点
- 启用 exec/child_process 的节点

## Context 管理

```bash
# 读取
scripts/nr get-context flow my-key
scripts/nr get-context global shared-data

# 写入
scripts/nr set-context flow my-key '"value"'
scripts/nr set-context global counter '42'
scripts/nr set-context global config '{"key": "value"}'

# 持久化导出（用于灾备）
scripts/nr export-context --output context-backup.json
```

## 运行时信息

```bash
scripts/nr get-settings        # Node-RED 设置
scripts/nr get-diagnostics     # 诊断信息（内存/运行时长/错误统计）
scripts/nr health              # 健康检查（实例连通 + 关键流程状态）
```

## Docker 操作

```bash
cd deployments/node-red && docker compose restart
docker logs mema-node-red --tail 100
docker logs -f mema-node-red

# 多实例
docker compose --profile prod up -d
docker compose --profile staging up -d
```

## 安全加固清单

部署前逐项核对：

- [ ] Admin API 启用鉴权（`adminAuth` 配置）
- [ ] 凭证密钥已设置（`credentialsSecret` 非默认）
- [ ] HTTPS 启用（生产实例）
- [ ] `httpNodeRoot` 非默认 `/`（隐藏 HTTP 端点）
- [ ] 危险节点（exec/file）已禁用或限制
- [ ] 备份定时任务已配置
- [ ] 流程变更走 staging → prod 流程
- [ ] Context 持久化配置正确（避免重启丢失）

## 真实场景示例

### 场景1：家居自动化流程上线

```
用户：把新的"回家模式"流程部署到生产
执行：
1. --instance staging deploy --file home-mode.json
2. staging 验证 10 分钟无报错
3. --instance prod deploy --file home-mode.json（自动留版本）
4. 报告：部署成功，版本 v20260718-1，回滚命令 nr rollback home-mode --last
```

### 场景2：生产流程故障回滚

```
用户：刚部署的流程把灯全关了，快回滚
执行：
1. scripts/nr rollback home-mode --last
2. 确认已回滚到 v20260718-0
3. 报告：回滚完成，问题版本已保留供分析
```

### 场景3：跨实例迁移

```
用户：把开发实例的全部流程迁到新服务器
执行：
1. --instance dev backup --output dev-full.json --include-context
2. 修改 .env 指向新服务器
3. --instance dev restore dev-full.json
4. health 检查全部流程状态
```

### 场景4：节点批量升级

```
用户：升级所有过期节点
执行：
1. upgrade-nodes --outdated-only
2. 兼容性检查：3 个节点有新版本，1 个不兼容（跳过）
3. 升级完成的节点逐个验证流程无报错
4. 报告：升级 2 个，跳过 1 个（node-red-contrib-x 不兼容 v3.1）
```

## FAQ

**Q1: 回滚会丢数据吗？**
A: 流程定义回滚不影响 Context 数据。Context 单独备份恢复。回滚只替换 flows.json 与 credentials。

**Q2: 多实例配置怎么管 token？**
A: 全部走环境变量 `${VAR}`，不入 `.env` 明文。CI/CD 用 secrets 注入。

**Q3: 部署到生产前必须过 staging 吗？**
A: 强烈推荐。安全加固清单第 7 项。若强行直发生产，CLI 会提示风险但允许（`--force`）。

**Q4: 节点升级后流程报错怎么办？**
A: 立即 `rollback <flow> --last` 回滚流程，再 `disable-node <新节点>` 禁用问题节点，最后排查兼容性。

**Q5: 备份文件包含敏感信息吗？**
A: 含加密的 credentials，但需 `credentialsSecret` 解密。备份文件建议存到加密存储，勿提交公开仓库。

## 故障排查

| 现象 | 排查路径 |
|:-----|:---------|
| Admin API 401 | 检查 `.env` 账号密码 → 确认 `adminAuth` 配置 → 重试 |
| 部署后流程不工作 | `get-diagnostics` 查错误 → `list-versions` 比对差异 → `rollback --last` |
| 节点安装失败 | 查 Node-RED 版本兼容性 → 查 npm registry → 手动 `npm install` 看详细错误 |
| Context 重启后丢失 | 检查 `contextStorage` 配置 → 改为 `localfilesystem` 持久化 |
| 多实例切换失效 | 确认 `--instance` 参数 → 检查 `.env` 对应块 → `doctor` 验证 |
| Docker 重启后流程丢失 | 检查 volume 挂载 → 确认 `data` 目录持久化 |
| 回滚后版本树错乱 | `.versions/` 目录可能被手动改过 → 用最近备份重建版本树 |

## 依赖说明

### 运行环境
- **Agent 平台**: 任意支持 SKILL.md 的 AI Agent
- **操作系统**: Windows / macOS / Linux
- **Node-RED**: ≥ 2.0（推荐 3.x），可通过 Docker 或本地安装

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Node-RED 实例 | 软件 | 必需 | docker / npm / 系统包 |
| Docker（可选） | 容器运行时 | 可选 | docker.com |
| `jq` | JSON 处理 | 推荐 | 系统包管理器 |
| `curl` | HTTP 调用 | 必需（CLI 内部用） | 系统自带 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
- Node-RED Admin 账号密码（写入 `.env`，生产用环境变量注入）
- `credentialsSecret`（解密流程凭证，建议存于密钥管理服务）
- 无需第三方 API Key

### 可用性分类
- **分类**: MD+EXEC（Markdown 指令 + 必须通过 exec 执行 `scripts/nr` CLI 与 docker 命令）
- **说明**: 基于自然语言指令驱动 Agent 管理 Node-RED 实例，含版本化、回滚、安全加固
