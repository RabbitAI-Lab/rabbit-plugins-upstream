---
name: Skill Positioning Review
slug: skill-positioning-audit
description: Reviews a skill storefront position and produces an evidence-based Storefront Copy Brief. Invoke when audience, promise, differentiation, or page hierarchy is unclear.
version: 2.0.0
metadata:
  openclaw:
    os: [macos]
    emoji: "🧭"
    requires:
      bins:
        - git
        - clawhub
    homepage: https://github.com/bonniegeng-max/openclaw-publisher
    install:
      - kind: node
        package: clawhub
        bins: [clawhub]
---

# Skill Positioning Review

在改文案之前，先判断这个 skill 应该对谁、在什么时刻、用什么可信承诺被理解。稳定 slug 仍为 `skill-positioning-audit`。

## 何时调用

- 用户说页面像模板、受众太宽、价值不清楚或缺少差异化
- 用户需要重做产品定位、信息层级或决定哪些卖点应舍弃
- `skill-publish-readiness` 发现页面定位问题并要求专项诊断

如果定位已经明确、只需写标题/摘要/首屏文案，直接使用 `skill-summary-rewriter`。

## 所需输入

优先读取 `SKILL.md`、skill-card、示例、目标用户描述和同类参照。缺失项可以标为未知，但不能虚构用户研究、下载数据或竞品事实。

## Review 工作流

1. **提取事实**：实际能力、输入、输出、依赖、证据和边界。
2. **定义受众**：谁在什么触发时刻最需要它；明确不服务谁。
3. **明确替代方案**：用户当前用什么做法解决，为什么不够。
4. **形成价值主张**：`为 [受众]，在 [场景]，提供 [结果]，不同于 [替代方案]，因为 [可信证据]。`
5. **检查差异化**：标题清晰度、用户聚焦、场景具体度、独特结果、可信证据各 0–5 分。
6. **设计页面层级**：标题 → 一句话承诺 → 三个证据点 → 边界/CTA。
7. **生成 Storefront Copy Brief**：按模板输出，可直接交给 `skill-summary-rewriter`。

## 输出契约

- 定位结论：清晰 / 需收窄 / 需重做
- 最大定位问题与证据
- 核心受众、触发场景、期望结果、替代方案
- 单一价值主张与差异化支柱
- 应保留/删除的承诺及禁用表达
- 页面信息层级
- 完整 Storefront Copy Brief

Review 阶段可给方向性示例，但不应产出 3–5 版最终营销文案；最终 copy 由 `skill-summary-rewriter` 基于 brief 完成。

## Storefront Copy Brief 交接

brief 必须包含：

- `source_slug` 与当前展示名
- 核心受众与触发时刻
- 首要问题、期望结果、替代方案
- 单一主张、三个差异化支柱、证据
- 必须提及 / 禁止声称
- 语气、语言、长度与投放位置约束
- 仍未确认的问题

交接语句：`请使用 skill-summary-rewriter，将以下 Storefront Copy Brief 转成商店页文案；不得新增 brief 之外的事实或承诺。`

## 边界

- 文案优化不等于增长保证
- 公开竞品结论与策略判断必须区分
- 证据不足时用保守表述并列出待确认项
- slug 不因展示名从 Audit 改为 Review 而变化

## 配套文件

- `references/storefront_rubric.md`：定位评分与 brief 质量门槛
- `templates/positioning_review.md`：Review 与 Storefront Copy Brief 模板
- `examples/weak_vs_strong_positioning.md`：从弱定位到可交接 brief 的示例
- `CHANGELOG.md`：版本记录
