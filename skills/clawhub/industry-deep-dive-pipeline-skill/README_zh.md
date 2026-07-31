# 产业深度文章全流程编排（Industry Deep-Dive Pipeline）

> 将单篇科技 / AI / 数据 / 云 / 企业软件产业选题推进到审核通过的正式 Markdown——含来源核验、原创性复核、完整策划、双人类门禁、确定性红线检查与八角色会审。

[![ClawHub](https://img.shields.io/badge/ClawHub-industry--deep--dive--pipeline--skill-blue)](https://clawhub.ai/haiyangchenbj/industry-deep-dive-pipeline-skill)
[![GitHub](https://img.shields.io/badge/GitHub-haiyangchenbj-black)](https://github.com/haiyangchenbj/industry-deep-dive-pipeline-skill)

---

## 它做什么

采用 Prompt Chaining + Evaluator-Optimizer 的固定流水线：固定主链保证可追踪，八角色会审后的修订循环保证质量。把单篇产业选题从简报推进到审核通过的定稿。

## 何时使用

- 你有一份选题简报、事件、厂商案例、政策变化或研究材料，需要一篇有判断、有证据、有边界的深度文章。
- 你需要在正文前完成目标读者、核心判断、论证链、反方、结构、标题、风险的完整策划，并形成完整证据包。

## 何时不使用

- 新闻快讯、摘要、产品说明书、技术教程或营销稿。
- 厂商大会全景报告 → 改用 `vendor-summit-report`。
- LinkedIn 单平台短观察 → 改用 `linkedin-industry-observation`。
- 微信排版 / 封面 / 发布 → 交给独立发布套件。

## 流程一览

1. 输入诊断 → 2. 事实表 → 3. 原创性与竞争复核 → 4. 策划简报 → **Gate A（人工）** → 5. 起草 → 6. 机器红线门禁 → 7. 八角色会审 → **Gate B（人工）** → 8. 修订 → 9. 复检 → 10. 打包。

## 关键硬规则

- 搜索用于发现，关键事实回到一手来源。
- 「原创 / 首创 / 唯一」类判断须有检索证据与边界。
- Gate A 未确认不得写正文；Gate B 只处理真实价值张力。
- 输出止于审核定稿与证据包——绝不自动发布。

## 目录结构

```
industry-deep-dive-pipeline/
├── SKILL.md
├── SKILL_zh.md
├── README.md
├── README_zh.md
├── _meta.json
├── references/   # 策划 schema、证据与原创性、写作 profile 接口、回放标准
├── scripts/      # 案例包校验、草稿红线扫描
└── templates/    # 简报、事实表、策划、会审、交付模板
```

## 许可证

MIT
