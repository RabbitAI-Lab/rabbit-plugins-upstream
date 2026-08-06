# GitCode AI Review Bot

基于 LangGraph 的 GitCode 仓库智能检视机器人。

## 功能

- 监听 GitCode Webhook 事件（PR 创建/更新/合并、评论）
- 自动拉取 PR 内容进行合规评测
- 标题不合规 → LLM 自动修正为 Conventional Commits 格式
- 内容不合规 → 评论 @提交人说明原因
- PR 合并后 → Squash 同步到目标分支 + 邮件通知
- 评论指令 → @bot 再次检视/帮助/状态（已移除）
- 评测标准以 Skill 插件形式提供，支持热加载扩展

## Skill 插件

| Skill | 功能 | 违规处理 |
|-------|------|----------|
| pr-title-check | PR 标题合规检查（Conventional Commits 或 Skill 格式） | auto_fix (LLM修正) |
| reviewer-check | 检视责任人检查 | comment (@提交人) |
| code-style-check | 代码规范检查 (LLM) | comment |
| security-check | 安全扫描 (正则+LLM) | comment |
| pr-description-check | PR 描述非空+长度检查 | comment |
| file-size-check | 单文件/总变更大小限制 | comment |
| branch-name-check | 分支命名规范检查 | comment |

## 管理 API

| 端点 | 方法 | 功能 |
|------|------|------|
| /admin/skills | GET | 列出所有 Skill 及状态 |
| /admin/skills/reload | POST | 热加载 Skill 配置 |
| /admin/trigger | POST | 手动触发 PR 评测 |
| /admin/config | GET | 查看运行配置（脱敏） |

## 快速开始

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 配置环境变量
cp .env.example .env
# 编辑 .env 填入 GITCODE_ACCESS_TOKEN 和 GITCODE_WEBHOOK_SECRET

# 3. 启动
python main.py
```

## 项目结构

```
src/
├── api/                  # 接入层 (FastAPI)
│   └── routes/           # 路由 (webhook, health, admin)
├── orchestrator/         # 编排层 (LangGraph)
│   ├── review_engine.py  # PR 评测工作流
│   ├── sync_engine.py    # Squash 同步引擎
│   └── event_dispatcher.py # 事件分发
├── business/             # 业务层 (Skill/AutoFix/Comment)
│   └── skills/           # 7 个内置 Skill
├── integration/          # 集成层 (GitCode/AI/Email Client)
└── infrastructure/       # 基础设施层 (Config/Log/Queue/Metrics)
```

## 配置

- `config/app_config.yaml` — 主配置
- `config/skills_config.yaml` — Skill 规则配置
- `.env` — 环境变量（Token、Secret 等）

## 测试

```bash
# 单元测试
python -m pytest tests/unit/ -v

# 集成测试
python -m pytest tests/integration/ -v

# 全量测试
python -m pytest tests/ -v
```

## 版本历史

### v0.2.0
- 新增 3 个 Skill: pr-description-check, file-size-check, branch-name-check
- 启用 code-style-check 和 security-check
- 统一 PR title pattern 为 Conventional Commits（兼容 Skill 格式）
- 修复 /ready 端点真正检查 Redis 连通性
- 修复 CommentEngine recheck 时序问题
- 新增管理 API (/admin/skills, /admin/trigger, /admin/config)
- 新增集成测试（Webhook 链路）
- 重建 .venv

### v0.1.0
- 初始版本：4 个 Skill + LangGraph 评测 + AutoFix + SyncEngine
