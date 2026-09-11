---
name: Skill Storefront Copy
slug: skill-summary-rewriter
description: Turns an approved Storefront Copy Brief into accurate titles, descriptions, and first-screen copy. Invoke when positioning is settled and storefront wording needs rewriting.
version: 2.0.0
metadata:
  openclaw:
    os: [macos]
    emoji: "✍️"
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

# Skill Storefront Copy

把已经确认的定位 brief 转成可直接使用的商店页标题、frontmatter description 和首屏文案。稳定 slug 仍为 `skill-summary-rewriter`。

## 何时调用

- 用户已有明确定位，只需要重写商店页文案
- `skill-positioning-audit` 已输出 Storefront Copy Brief
- 用户要求多版标题、description、首屏、CTA 或不同长度变体

如果受众、场景、核心承诺或证据仍不清楚，先调用 `skill-positioning-audit`，不要用漂亮文案掩盖定位缺口。

## 输入优先级

1. 已批准的 Storefront Copy Brief
2. 用户在当前请求中的明确约束
3. `SKILL.md` 与真实示例中的可验证事实

冲突时先指出冲突并请求确认；不得擅自改变核心受众、添加能力或做增长保证。

## Brief 接收检查

必须确认：`source_slug`、受众、触发时刻、问题、期望结果、单一主张、差异化支柱、证据、必须提及、禁止声称、语气/语言/长度/位置约束。

- 信息完整：直接写 copy
- 非关键项缺失：标注假设并给保守版本
- 受众、主张或证据缺失：退回 `skill-positioning-audit` 补 brief

## Copy 工作流

1. 锁定 brief，不改变策略层事实。
2. 先写一句结果导向的 message spine。
3. 生成三套有明确用途的方案：
   - `Direct`：最清楚，适合 frontmatter description
   - `Distinctive`：强化差异点，适合商店页首屏
   - `Compact`：字符紧张时使用
4. 每套包含展示名、description、首屏标题/段落和可选 CTA。
5. 对照 brief 做 claim check：每个能力与证据可回溯，禁用表达未出现。
6. 推荐一套并说明适用位置，不以“更有创意”替代准确性。

## 写作规则

- 先写用户结果，再写方法
- 点名受众或触发场景，删除“高效、智能、便捷、适合所有人”等空词
- description 保持单一主张，不堆功能清单
- 展示名可以更新，slug 必须保持不变
- 中文 brief 默认输出中文；双语只在 brief 或用户明确要求时提供
- 不声称保证安装、增长、审核通过或已完成验证

## 输出契约

- Brief 完整度与发现的冲突
- Message spine
- Direct / Distinctive / Compact 三套 copy
- 推荐方案与投放位置
- Claim check：每条关键承诺对应的 brief 字段/证据
- 未采用的表达及原因

## 与 Skill Positioning Review 的交接

接收格式见 `templates/summary_rewrite_output.md`。若输入来自 `skill-positioning-audit`，必须原样保留 `source_slug` 与 `must_not_claim`；若修改了策略，明确退回 Review，而不是静默重写 brief。

## 配套文件

- `references/summary_patterns.md`：按 placement 写 copy 与 claim check
- `templates/summary_rewrite_output.md`：brief 接收及交付模板
- `examples/weak_vs_strong_summaries.md`：从 brief 到三套 copy 的示例
- `CHANGELOG.md`：版本记录
