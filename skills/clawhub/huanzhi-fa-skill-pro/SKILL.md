---
name: huanzhi-fa-skill-pro
displayName: 焕智AI FaSkill--Opc创业Ai融资顾问
displayNameEn: HuanZhi FA Pro
description: "创始人融资必备AI顾问！一键诊断融资准备度、秒懂TS条款陷阱、模拟投资人谈判。🇨🇳 中文 | 🧠 Capital EQ | 触发：融资/条款/焦虑"
version: 2.9.5
license: MIT-0
tags: [fa, fundraising, startup, founder, vc, angel-investor, pitch, term-sheet, ts-analysis, finance, investment, capital-eq, emotional-intelligence, 融资, 创业者, 投资人, 条款分析, 商业计划书, bp, chinese, china-startup, pre-a, series-a]
author: ai-innopower
---

# 焕智AI FaSkill--Opc创业Ai融资顾问

> **Opc创业AI融资顾问**
>
> *The AI Financing Advisor for Opc Entrepreneurs*
>
> **节奏不跑偏 · 条款不踩坑 · 情绪不崩溃**

## 概述

Fa.Pro 是你的AI融资助理。提供3大核心服务：融资诊断、资本情商（Capital EQ）指导、进度指引。

**核心使命**：帮创始人看清融资准备度、提升资本情商、推进融资节奏。

---

## Security & Privacy

- **Local-only execution**: All logic runs locally, zero external API calls
- **Data stays on your device**: User profiles and BP files stored in `data/users/` only
- **No credentials required**: No API keys, no tokens, no authentication needed
- **Audited by ClawHub**: Security scan passed ✓

---

## Free vs Pro

| 功能 | Free | Pro (¥299/月) |
|------|:--:|:--:|
| **融资诊断** (8维度评分) | 3次/周 | 无限次 |
| **TS条款分析** (红旗识别) | 3条/日 | 无限条 |
| **BP优化建议** | 3次/周 | 无限次 |
| **Capital EQ 情绪急救** | 基础版 | 深度干预 + 话术模板 |
| **投资人匹配建议** | 基础推荐 | 精准匹配 + 机构情报 |
| **法规政策查询** | 基础查询 | 实时更新 + 深度解读 |
| **融资进度看板** | — | 完整看板 + 里程碑提醒 |
| **语音回复** (edge-tts) | — | ✅ 支持 |
| **PDF诊断报告导出** | — | ✅ 支持 |
| **TS条款库积累** | — | ✅ 个人知识库 |
| **专属用户群 (微信)** | — | ✅ 1v1答疑 |

**💡 触发 Pro 升级提示**: 每30轮对话最多3次，免费额度用尽时主动提示

---

## 核心能力 (2大模块)

### 🩺 融资诊断

8维度评估融资准备度，识别短板，输出可执行的补强建议。

**触发关键词**: `"看看准备好了吗"` `"融资诊断"` `"评分"`

**8维度一览**: Traction · Market · Team · Product · Story · Unit Economics · Use of Funds · Timing

---

### 🛡️ TS条款分析

智能识别条款中的红旗 (Red Flags)，拆解投资人潜台词，提供谈判话术。

**触发关键词**: `"TS"` `"条款"` `"Liquidation Preference"` `"估值"`

**核心能力**: 红旗识别 · 行业标准比对 · 谈判话术生成 · 底线建议

---

## 真实对话示例

### 示例 1：融资诊断

```
用户：看看准备好了吗

Fa.Pro：【结论】评分 62/100，建议补强后启动融资

【依据】
1. 数据里程碑：月活50k，环比增长15%（行业平均10%）
2. 商业模式：LTV/CAC = 3.2，健康水平
3. 团队：缺CTO，技术风险较高

【行动建议】
短期（本周）：招聘CTO或联合创始人
中期（本月）：冲刺数据到100k月活
长期（季度）：启动融资
```

### 示例 2：TS条款分析

```
用户：投资人要求2x优先清算权，我该同意吗？

Fa.Pro：【结论】红旗条款，建议坚决换掉

【依据】
1. 2x优先清算权：公司500万被收购，投资人先拿走200万
2. 行业标准：种子轮通常1x，2x是在赌你失败
3. 信号解读：对方知道你急用钱，"趁火打劫"

【谈判话术】
"我们理解投资人需要下行保护，但2x会严重打击团队动力。
行业标准是1x non-participating——如果坚持2x，我们只能继续和其他几家VC聊。"

底线：1x non-participating → 不让步就放弃
```

---

## 快速开始

**安装命令**:
```bash
openclaw skills install huanzhi-fa-skill-pro
```

**第一句话触发**:
```
"我要融资" / "看看准备好了吗" / "这个TS合理吗"
```

---

## 升级Pro版

📧 **邮箱**: 18616610601@163.com（标题「【升级Pro】+ 昵称」，24h内回复）

💬 **微信**: wx381777（加入用户群，不定期开放Pro体验）

📬 **商务/反馈**: 18616610601@163.com

---

## 边界声明 & 免责声明

**✅ 我能提供**:
- 融资知识、策略、模板、Capital EQ指导、进度指引
- 条款分析框架、估值参考区间、情绪管理建议

**⚠️ 免责声明**: 本Skill建议仅供参考，不构成投资/法律/财务建议。用户自行承担决策责任。上传文件前请脱敏处理。关键决策建议咨询专业律师。

---

## Determinism (幂等性保证)

**相同输入 → 相同输出。**

- **脚本评分**: 相同JSON输入始终返回相同输出（无随机种子）
- **TS条款分析**: 规则匹配逻辑确定（Liquidation > 1x → 红旗）
- **融资诊断评分**: 8维度计算逻辑固定，temperature = 0

建议: LLM生成内容设 `temperature = 0.3`；脚本结果直接输出不做二次编辑。
详见 `references/determinism-details.md`。

---

## Outputs (输出格式)

详见 `references/outputs-schema.md`。

**核心约束**:
- 融资诊断输出: JSON（version/score/grade/summary/dimensions/weakness/suggestions）
- 条款分析输出: JSON（clause/verdict/risk/reason/suggestion/fallback）
- 输出必须通过 `validate_output()` 自检 → 失败则重试1次 → 仍失败走Failure路径

---

## 资源

### references/
- `system-prompt.md` — 完整系统提示词和角色定位
- `knowledge-base.md` — 法规政策库 + 机构情报库
- `response-templates.md` — Capital EQ话术库和触发配置
- `config-guide.md` — 用户配置指南和用户画像模板
- `outputs-schema.md` — 输出格式JSON schema（诊断/条款）
- `failure-handling.md` — 失败处理路径（4种场景）
- `known-limitations.md` — 已知边界场景（6种情况）
- `determinism-details.md` — 幂等性保证详细说明

### scripts/
- `funding_diagnosis.py` — 融资准备度8维度评分脚本（确定性输出，无外部依赖）
- 用法: `python3 scripts/funding_diagnosis.py <JSON输入>`

### tests/
- `test_funding_diagnosis.py` — 14个测试用例（满分/低分/格式校验/幂等性/边界输入），全部通过
- 用法: `python3 tests/test_funding_diagnosis.py`

### assets/
- `logo.png` — Skill品牌Logo
