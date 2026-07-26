# ClawHub 发布指南

## 快速使用

```bash
# 1. 确认登录
clawhub whoami

# 2. 进入 skills 目录
cd D:\openclaw-data\workspace\skills

# 3. 干跑预览
clawhub sync --dry-run

# 4. 正式发布
clawhub sync --all --bump patch --changelog "更新说明"

# 5. 验证
clawhub inspect 你的技能slug
```

详细步骤见 `SKILL.md`。

## 文件

- `SKILL.md` — 完整发布步骤（含 publish/sync 两种方式、常见问题）
- `README.md` — 本文件

## 依赖

- `clawhub` CLI（npm i -g clawhub）
- 已登录账号（clawhub login）