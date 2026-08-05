---
name: coding-skill-check
enabled: true
event: PreTask
matcher: "coding|code|implement|fix|bug|review|test|debug|deploy|build|开发|编码|实现|修复|审查|测试|部署"
action: warn
priority: 50
---

# 编程任务技能检查提醒

当检测到编程相关任务时，提醒 AI 执行以下检查：

## 1% 规则检查

在开始编码前，问自己：
- 这个任务是否涉及代码修改？
- 是否有对应的开发阶段技能适用？
- 我是否正在"合理化"跳过某个技能？

## Red Flags（防跳过信号）

以下思维意味着你正在合理化跳过技能：
- "这只是个简单修改" → 简单修改也可能引入 bug
- "我先做这一件事" → 做事之前先检查技能
- "技能太小题大做了" → 简单的事会变复杂

## 行动

1. 加载 `coding-framework` 技能
2. 执行 Step 0 阶段检测
3. 根据阶段加载对应技能

**参考**: coding-framework v11.7 Red Flags 表格
