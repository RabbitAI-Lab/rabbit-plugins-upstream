# Pattern: Tool Wrapper（知识封装）

> 控制的不确定性：**知识不确定**——Agent 知道通用知识，但不知道你的团队规范。

## 何时用

当你希望 Agent 在某个技术域里遵守一致规则时。判断标准：**一个规则每次处理这个技术栈都该遵守**。

典型场景：
- 团队代码规范（FastAPI / React / Terraform / SQL 最佳实践）
- 内部 SDK 使用手册
- 数据库查询规范
- 安全策略
- 公司内部 API 调用规范

## 目录结构

```
skill-name/
├── SKILL.md              # 索引 + 执行协议（不是规则仓库）
└── references/
    └── conventions.md    # 真正的规范细节
```

## 核心要素

**SKILL.md 是"索引 + 执行协议"，不是规则仓库。** SKILL.md 里不要堆规范，只告诉 Agent：
1. 什么时候加载这个 Skill
2. 加载后先读哪个 reference
3. 写代码时如何应用规范
4. 审查代码时如何引用规则并给修复建议

**三好处**（为什么外置到 references/）：
1. Skill 激活前上下文更轻
2. 规范更新时不用改主指令
3. 同一套执行协议可换不同 reference 复用

## 最小 SKILL.md 骨架

```markdown
---
name: api-expert
description: 应用 FastAPI 开发规范。当构建、审查或调试 FastAPI 应用、REST API 或 Pydantic 模型时使用。
agent_created: true
---

你是 FastAPI 开发专家。将这些规范应用到用户的代码或问题上。

## 核心规范

加载 `references/conventions.md` 获取 FastAPI 最佳实践的完整列表。

## 审查代码时
1. 加载规范参考
2. 对照每条规范检查用户代码
3. 对每个违规，引用具体规则并建议修复

## 编写代码时
1. 加载规范参考
2. 严格遵循每条规范
3. 为所有函数签名添加类型注解
```

## references/conventions.md 示例

```markdown
# FastAPI Conventions

## Route Definitions
- Use `Annotated` for all dependency injection

## Pydantic Models
- Always add `model_config = ConfigDict(from_attributes=True)` for ORM models

## Error Handling
- Raise `HTTPException` with specific status codes, never generic 500

## Security
- Never store secrets in code — use environment variables
```

## 常见坑

| 坑 | 后果 | 修正 |
|---|---|---|
| 把 200 条规范塞进 SKILL.md | 上下文爆炸 + 规范混入主指令 | 规范全挪 `references/conventions.md`，SKILL.md 只留索引 |
| 混用多个技术栈规范 | Agent 混用规则 | 一个 Tool Wrapper 只封一个技术域 |
| SKILL.md 写成规则仓库 | 失去"索引"价值，更新难 | SKILL.md 只写"加载哪个 reference + 怎么执行" |
