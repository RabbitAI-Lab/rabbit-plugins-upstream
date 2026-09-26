# forklift-expert · 叉车专家技能 / Forklift Expert Skill

> **中文** | [English](#english)

**版本 Version:** 2.5.0  **更新日期 Updated:** 2026-09
**作者 Author:** 杨鹏飞 / 微信公众号「叉车技术老炮」
**许可 License:** MIT（保留版权声明即可商用 / Commercial use allowed with copyright notice retained）

---

## 中文

### 这是什么

一个面向叉车（工业车辆）全领域的专家技能包，覆盖**品牌产品、选型、技术、故障诊断、配件维保、二手评估、法规标准、市场动态、销售排行、招投标播报、安全管理**等维度。

已内置 18 个知识模块，配合实时联网检索，用于把"凭印象回答"变成"有据可查的回答"。

### 触发场景

叉车、电叉、锂电叉车、铅酸叉车、平衡重、前移式、堆高车、托盘车、AGV/AMR、
杭叉、合力、比亚迪、中力、柳工、诺力、丰田、林德、永恒力、卡尔玛、科尼、
门架、液压、电池、BMS、充电机、控制器、GB/T 43756、GB/T 44679、TSG 11、
叉车驾照 N1/N2、叉车销量、叉车出口、叉车招标/投标/中标……
（完整触发词见 `SKILL.md` frontmatter）

### 模块清单

| 模块 | 文件 | 用途 |
|------|------|------|
| 品牌目录 | `references/brands.md` | 国内外品牌、官网、定位、2026 H1 经营数据 |
| 基础知识 | `references/knowledge.md` | 分类、选购、技术、经济性、认知误区 |
| **动力电池** | `references/tech-battery.md` | 电芯体系、成组与电压平台、BMS、充电、衰减、热管理 |
| **大吨位电叉参数** | `references/heavy-spec-electric.md` | 6-8 吨级电动平衡重参数与对标方法 |
| 选型指南 | `references/selection-guide.md` | 选型决策流程 |
| 故障诊断 | `references/fault-diagnosis.md` | 症状→原因→诊断→处理 |
| 安全与驾照保险 | `references/safety-regulation.md` | 驾照、保险、法规 |
| **安全管理实务** | `references/safety-management.md` | 彻底检验、风险管理、LOTO、现场交通管理 |
| 标准库 | `references/standards.md` | 国标/ISO/EN/法规 |
| 标准联网检索 | `references/standard-retrieval.md` | 标准状态与条款核验 |
| 行业趋势 | `references/market-trends.md` | 行业动态 |
| 维保计划 | `references/maintenance-plan.md` | 保养周期与项目 |
| 配件易损件 | `references/parts-consumables.md` | 配件与消耗品 |
| 二手评估 | `references/used-forklift-evaluation.md` | 二手车检查与估值 |
| 销售动态 | `references/sales-news.md` | 联网检索 + 国内外分组 + 图表 |
| 图表生成 | `references/svg-chart.md` | 自包含 SVG 图表（默认输出） |
| 招投标播报 | `references/tender-broadcast.md` | 周度汇总 + HTML 交付 |
| 多语言 | `references/i18n.md` | 中/英自动匹配 + 术语表 |
| 使用详解 | `usage-guide.md` | 模块清单、避坑、扩展定制、性能成本 |

### 安装

```bash
# SkillHub
skillhub install forklift --namespace user_bc886e82 --dir <你的 skills 目录>

# 安装后处理（重要）
# 安装器会生成 @user_bc886e82/forklift 双层目录，需重命名为单层：
mv <skills 目录>/@user_bc886e82/forklift <skills 目录>/forklift-expert
rm -rf <skills 目录>/@user_bc886e82
```

各平台 skills 目录示例：Claude Code `~/.claude/skills/`、Cursor `~/.cursor/skills/`、
Codex `~/.codex/skills/`、Gemini CLI `~/.gemini/skills/`、CodeBuddy `~/.codebuddy/skills/`。

### 核心硬规则

1. **不编造** — 型号参数、标准号、销量、招标信息一律联网实查，查不到如实说
2. **不报价** — 配件价格、二手价格、维保工时费，引导查服务站或实时检索
3. **销售类** — 必须联网 + 国内/国外分组 + 表格 + SVG 图表 + 标注检索日期
4. **图表** — 默认自包含 SVG，零 CDN 依赖；ASCII 仅在明确要求时降级
5. **招投标** — 锁定提问日所在自然周为数据窗口；每条必须带可点击来源链接；无源不收录；不预测中标
6. **标准** — 状态、实施日期、代替关系必须联网核验并标注核验日期
7. **多语言** — 中文提问中文答，英文提问英文答；标准号/品牌/型号/版权行不翻译

### 目录结构

```
forklift-expert/
├── SKILL.md              总入口（路由 + 硬规则 + 输出模板）
├── README.md             本文件（中英双语）
├── LICENSE.md            MIT 协议全文
├── AUTHOR.md             作者信息
├── skill-card.md         发布卡片
├── usage-guide.md        使用详解
├── _meta.json            发布元数据
└── references/           知识库（18 个模块）
```

### 许可

MIT License。唯一硬性要求：在所有副本或实质性部分中保留
`Copyright (c) 2026 杨鹏飞` 与 MIT 协议全文。
商业使用、修改闭源、嵌入产品、训练 AI 均允许，无需事先授权。

---

<a name="english"></a>

## English

### What This Is

An expert skill package for forklifts and industrial trucks, covering **brands & products,
selection, technology, fault diagnosis, parts & maintenance, used-equipment evaluation,
regulations & standards, market trends, sales rankings, public-tender briefings, and safety management**.

Ships with 19 knowledge modules plus live web retrieval — designed to replace
"answers from memory" with "answers that can be traced to a source."

### Trigger Scenarios

forklift, electric forklift, lithium forklift, lead-acid forklift, counterbalance truck,
reach truck, pallet stacker, pallet jack, AGV, AMR, Hangcha, Heli, BYD, EP Equipment,
LiuGong, Noblelift, Toyota, Linde, Jungheinrich, Kalmar, Konecranes, mast, hydraulics,
battery, BMS, charger, controller, ISO 23308, ISO 3691, TSG 11, forklift operator license,
forklift sales, forklift export, forklift tender / bidding / bid award…
(full trigger list is in `SKILL.md` frontmatter)

### Module Index

| Module | File | Purpose |
|--------|------|---------|
| Brand directory | `references/brands.md` | Domestic & global brands, positioning, H1 2026 results |
| Fundamentals | `references/knowledge.md` | Classification, buying guide, technology, TCO, myths |
| **Traction battery** | `references/tech-battery.md` | Cell chemistry, pack & voltage platform, BMS, charging, ageing, thermal |
| **Heavy-class specs** | `references/heavy-spec-electric.md` | 6–8 t electric counterbalance specs & benchmarking |
| Selection guide | `references/selection-guide.md` | Decision workflow |
| Fault diagnosis | `references/fault-diagnosis.md` | Symptom → cause → test → fix |
| Safety, licence & insurance | `references/safety-regulation.md` | Licensing, insurance, regulations |
| **Safety management** | `references/safety-management.md` | Thorough examination, risk management, LOTO, site traffic |
| Standards library | `references/standards.md` | GB / ISO / EN / regulations |
| Online standard lookup | `references/standard-retrieval.md` | Status & clause verification |
| Market trends | `references/market-trends.md` | Industry dynamics |
| Maintenance plan | `references/maintenance-plan.md` | Service intervals & items |
| Parts & consumables | `references/parts-consumables.md` | Spare parts and wear items |
| Used-equipment | `references/used-forklift-evaluation.md` | Inspection and valuation |
| Sales news | `references/sales-news.md` | Live search + domestic/global split + charts |
| Chart generation | `references/svg-chart.md` | Self-contained SVG charts (default output) |
| Tender broadcast | `references/tender-broadcast.md` | Weekly digest + HTML delivery |
| i18n | `references/i18n.md` | Auto ZH/EN matching + glossary |
| Usage guide | `usage-guide.md` | Modules, pitfalls, extension, cost |

### Installation

```bash
# Via SkillHub
skillhub install forklift --namespace user_bc886e82 --dir <your skills directory>

# Post-install step (important)
# The installer creates a nested @user_bc886e82/forklift folder; flatten it:
mv <skills dir>/@user_bc886e82/forklift <skills dir>/forklift-expert
rm -rf <skills dir>/@user_bc886e82
```

Typical skills directories: Claude Code `~/.claude/skills/`, Cursor `~/.cursor/skills/`,
Codex `~/.codex/skills/`, Gemini CLI `~/.gemini/skills/`, CodeBuddy `~/.codebuddy/skills/`.

### Core Hard Rules

1. **No fabrication** — model specs, standard numbers, sales figures and tender data must be
   retrieved live; say "not found" when it is not found
2. **No pricing** — parts prices, used-equipment prices and labour rates are referred back to
   dealers or live search
3. **Sales questions** — live search + domestic/global split + table + SVG chart + retrieval date
4. **Charts** — self-contained SVG by default, zero CDN; ASCII only on explicit request
5. **Tenders** — window locked to the calendar week of the question; every item must carry a
   clickable source link; no source means no entry; no prediction of winners
6. **Standards** — status, effective date and replacement relations must be verified online
   with the verification date shown
7. **Multilingual** — answer in the language of the question; standard numbers, brand names,
   model codes and the copyright line are never translated

### Directory Layout

```
forklift-expert/
├── SKILL.md              Entry point (routing + hard rules + output templates)
├── README.md             This file (bilingual)
├── LICENSE.md            Full MIT text
├── AUTHOR.md             Author info
├── skill-card.md         Release card
├── usage-guide.md        Usage guide
├── _meta.json            Release metadata
└── references/           Knowledge base (18 modules)
```

### License

MIT License. The only hard requirement: retain `Copyright (c) 2026 杨鹏飞`
and the full MIT text in all copies or substantial portions.
Commercial use, closed-source modification, product embedding and AI training are all
permitted without prior authorisation.

---

Copyright (c) 2026 杨鹏飞 / 微信公众号「叉车技术老炮」 · MIT License
