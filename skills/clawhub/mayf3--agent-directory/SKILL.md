# Agent Directory Skill

> 管理所有 Agent 的个人档案、管线归属和长线规划。

## 核心文件

- **数据目录**：`docs/agent-profiles/`
- **格式**：每个 Agent 一个 JSON 文件，文件名 = `{systemName}.json`
- **索引**：`docs/agent-profiles/index.json`（自动生成）

## JSON Schema

每个 Agent 档案必须包含以下字段：

```json
{
  "systemName": "blog-agent",
  "displayName": "博客专家（小博）",
  "role": "内容生产线的核心写手",
  "feishuGroup": "oc_21ced618ce1acc9ff4d76aa2aabde473",
  "workspace": "workspace-oc_21ced618ce1acc9ff4d76aa2aabde473",
  "layer": "main",
  "pipelines": ["content-production", "ai-evangelist"],
  "mainlineDirection": "AI布道师 - 产出实践文章",
  "longTermGoals": [
    "月产4篇高质量实践文章",
    "形成AI Agent实践者系列"
  ],
  "currentTodos": [99, 88],
  "status": "active",
  "createdAt": "2026-05-19",
  "updatedAt": "2026-05-19"
}
```

### 字段说明

| 字段 | 必填 | 类型 | 说明 |
|------|------|------|------|
| systemName | ✅ | string | 唯一标识，对应 cron agentId |
| displayName | ✅ | string | 显示名 |
| role | ✅ | string | 一句话角色定位 |
| feishuGroup | ❌ | string | 飞书群 chat_id |
| workspace | ❌ | string | workspace 目录名 |
| layer | ✅ | enum | `main`(主线) / `exploration`(探索) / `life`(生活) / `infra`(基础设施) / `cross-cutting`(横切) |
| pipelines | ✅ | string[] | 所属管线ID列表（可多个） |
| mainlineDirection | ✅ | string | 主线方向描述 |
| longTermGoals | ❌ | string[] | 长线目标列表 |
| currentTodos | ❌ | number[] | 关联 LLM Todo 任务ID |
| status | ✅ | enum | `active` / `inactive` / `pending-setup` |
| createdAt | ✅ | date | 创建日期 |
| updatedAt | ✅ | date | 最后更新日期 |

### Layer 枚举

- `main` — 直接服务 AI布道师（内容+开源）
- `exploration` — 间接服务，探索线
- `life` — 生活服务，自主运转
- `infra` — 基础设施（研发/安全/运维）
- `cross-cutting` — 横切能力（搜索/知识/学习）

### Pipeline ID 枚举

- `content-production` — 内容生产→发布→运营
- `ai-evangelist` — AI布道师主线
- `open-source` — 开源引擎
- `parenting` — 育儿教育
- `investment` — 投资理财
- `family-health` — 家庭健康
- `smart-home` — 智能家居
- `planning` — 规划线
- `infra-dev` — 基础设施开发
- `life-services` — 生活服务
- `community` — 社区运营

## 脚本

### validate.sh — 校验所有档案格式

```bash
bash scripts/validate.sh
```

检查项：
- 每个 JSON 文件符合 schema
- systemName 唯一
- layer 值合法
- pipelines 中的 ID 合法
- 必填字段不缺

### build-index.sh — 生成索引

```bash
bash scripts/build-index.sh
```

生成 `index.json`，包含所有 Agent 的摘要信息。

## 使用场景

1. **新建 Agent**：创建 JSON 文件 → 运行 validate → 更新 index
2. **修改管线归属**：编辑 JSON 的 pipelines 字段 → validate
3. **查 Agent 信息**：读 JSON 或查 index.json
4. **管线视图**：按 pipeline ID 过滤 index.json
5. **平台迁移**：JSON 数据可直接灌入 Agent 团队管理平台（需求 60518a5c）

## 维护人

- 龙虾合伙人（ceo-agent）+ HR Agent
