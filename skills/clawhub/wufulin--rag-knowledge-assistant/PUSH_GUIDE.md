# RAG 知识库助手发布指南

本文档记录 `rag-knowledge-assistant` 的 GitHub 推送和 ClawHub 发布流程。

## 当前发布信息

| 项目 | 值 |
|------|----|
| Skill slug | `rag-knowledge-assistant` |
| 新版本 | `2.0.1` |
| ClawHub owner | `wufulin` |
| ClawHub page | `https://clawhub.ai/wufulin/skills/rag-knowledge-assistant` |
| GitHub repo | `https://github.com/wufulinit/rag-knowledge-assistant` |
| GitHub email | `wufulinit@gmail.com` |

## 发布前检查

```bash
cd /Users/wufulin/.hermes/skills/openclaw-imports/rag-knowledge-assistant

# 确认版本
grep -n "version:" SKILL.md

# 确认 ClawHub 登录用户
clawhub whoami

# 确认 Git 身份
git config --global user.name
git config --global user.email
```

本包包含 `.clawhubignore`，发布时会排除 `scripts/venv/`、缓存、日志和本地向量库，避免上传本机环境文件。

## GitHub 推送

当前目录可能不是 git 仓库；如需推送到 GitHub，先初始化仓库：

```bash
cd /Users/wufulin/.hermes/skills/openclaw-imports/rag-knowledge-assistant

git init
git branch -M main
git config user.name "wufulin"
git config user.email "wufulinit@gmail.com"
git remote add origin git@github.com:wufulinit/rag-knowledge-assistant.git

git add .
git commit -m "feat(rag): release hybrid search assistant 2.0.1"
git push -u origin main
```

如果使用 GitHub CLI，请先修复登录：

```bash
gh auth login -h github.com
gh auth status
```

不建议把 Personal Access Token 写进 remote URL 或 shell history。优先使用 SSH、GitHub CLI 或系统 credential manager。

## ClawHub 发布

```bash
cd /Users/wufulin/.hermes/skills/openclaw-imports/rag-knowledge-assistant

clawhub skill publish . \
  --slug rag-knowledge-assistant \
  --owner wufulin \
  --version 2.0.1 \
  --changelog "Release 2.0.1: add BM25 + vector hybrid retrieval, FastAPI service, automatic query integration, owner-qualified ClawHub docs, and safer release packaging." \
  --tags latest
```

如需把旧 owner 下的同名 skill 迁移到 `wufulin`，且当前 ClawHub 用户有权限，可以增加：

```bash
--migrate-owner
```

## 发布后验证

```bash
curl -s "https://clawhub.ai/api/v1/skills/rag-knowledge-assistant/versions?owner=wufulin&limit=5"
curl -s "https://clawhub.ai/api/v1/skills/rag-knowledge-assistant/versions/2.0.1?owner=wufulin"
```

当前 ClawHub 上仍存在旧 owner `@aixbinge` 的同名 skill。裸 slug 可能触发 `AMBIGUOUS_SKILL_SLUG`，验证时使用 `owner=wufulin` 可避免歧义。

确认以下文件已包含在发布包中：

- `SKILL.md`
- `README.md`
- `rag-config.yaml`
- `scripts/index_knowledge.py`
- `scripts/rag_query.py`
- `scripts/rag_api.py`
- `scripts/hybrid_retriever.py`
- `references/system_architecture.md`
- `references/hybrid_search.md`
- `references/fastapi_service.md`

确认以下本地文件未被发布：

- `scripts/venv/`
- `scripts/__pycache__/`
- `.DS_Store`
- `vectorstore/`
- `*.log`
