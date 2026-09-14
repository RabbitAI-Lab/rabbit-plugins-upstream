---
name: cite-holmes
license: MIT
description: >-
  像福尔摩斯一样调查自己信源的深度研究（Verified Deep Research 深度调研×引用验真）：
  先反问式校准范围（3-5 个关键问题）→ 制定研究计划 → 迭代多源检索（中英文、信源金字塔）→
  每条引用机器核实（DOI 经 DOI.org 解析、PMID 经 PubMed E-utilities 官方接口交叉验证；
  五态判定：verified 可靠 / partial 部分 / unverified 未验 / unreachable 未达 / invalid 无效）。
  报告头部自动输出 CiteScore 置信度评分（0-100，A–D 级）；正文结论按 🟢🟡🔴
  三级置信度标注。未验证的引用绝不作为正文结论引用，仅列入人工复核区；
  专治 AI 幻觉引用，编造 DOI、假 PMID 与死链均为一级抓捕目标。
  内置医学证据模式（Cochrane/BMJ/ClinicalTrials/NMPA/CDC/NICE/万方 期刊层预设 + PMID 核实）
  与已验证文献导出（BibTeX + 审计 CSV）。触发词：深度研究、深入调研、查证、核查引用、
  这个说法是真的吗、参考文献验真、信源验证、AI 幻觉引用、综述一下、做个调研、
  fact check、verify citations、deep research。
when_to_use: >-
  用户说"深度研究""深入调研""帮我研究一下""查证""核实一下""这个说法是真的吗"
  "参考文献验真""这些引用是真的吗"，需要带信源的研究报告、文献综述、医学证据检索，
  或投稿前需要核验引用时使用——即使没说"研究"二字也应触发。
metadata:
  clawdbot:
    emoji: "🔍"
    category: research
---

# cite-holmes（引文福尔摩斯）：带引用验证的深度研究

一句话：**问题进 → 经过验证的报告出。**

与普通"搜索一下然后总结"的三个本质区别：

1. **动手前先校准**——先问尖锐的问题；最贵的浪费是研究了错误的问题。
2. **结论带证据强度**——🟢 两个独立来源一致 / 🟡 单一权威源 / 🔴 来源冲突存疑。
3. **每条引用都被检查**——机械层（可达性、域名权威度、字段完整性、去重）+
   语义层（来源内容是否真的支撑论断）。未验证的引用绝不伪装成真实。

## ⛔ 铁律（零例外）

1. **不编造**：引用必须来自本次会话真实抓取过的页面。记不清的 URL 宁可重查，
   不凭记忆写。
2. **不伪装**：未检查的引用标 `unverified`；抓取失败标 `unreachable`
   （≠ 不存在——转入人工复核）。
3. **不回避冲突**：来源互相矛盾时如实呈现分歧，标 🔴，写明双方各自的依据。
4. **检索有预算**：QUICK ≤6 次搜索，FULL ≤15 次。预算耗尽仍有缺口 → 在报告中
   如实交代，而不是硬凑结论。
5. **先校准后开搜**（FULL 模式）：范围 / 时间跨度 / 受众 / 输出格式必须先锁定。

## 第 0 步：模式选择

| 模式 | 适用 | 校准 | 预算 | 产出 |
|---|---|---|---|---|
| **QUICK** | 单点事实核查："这个说法是真的吗""XX 是哪年发布的" | 免 | ≤6 | 简版报告 |
| **FULL** | 开放性研究："XX 领域现状""A 和 B 怎么选""做个综述" | 必须反问 | ≤15 | 完整报告 |

一个问题能被单个可验证事实回答 → QUICK；需要综合权衡或利弊对比 → FULL。
用户说"快查/简单核实"强制 QUICK；说"深挖/彻底/全面"强制 FULL。拿不准默认 FULL。

## 五阶段工作流

### 1. CALIBRATE 校准（仅 FULL）

一次性提出 3–5 个高杠杆问题（不挤牙膏）：范围、时间跨度、受众与深度、输出格式、
决策背景。用户已给过的信息不重复问；用户说"你看着办"→ 按合理默认走并在计划里
声明假设。

### 2. PLAN 规划

亮出简短计划：3–7 个子问题、信源优先级（一手/官方 > 权威媒体 > 社区/博客仅作
线索）、预算。

### 3. SEARCH 检索（迭代，不是一遍过）

**先读 `references/search-strategies.md`**（菱形扩展、信源金字塔、搜索词矩阵、
缺口驱动迭代）。要点：每轮搜索只回答一个子问题；检索词跟随已发现的术语演化；
中英文话题两种语言各搜一遍；对最有价值的 2–5 个来源抓全文细读（绝不只凭搜索
摘要下结论）；关键数字/日期在原始页面定位后才可引用。

### 4. VERIFY 验证（本 skill 的灵魂）

每条引用登记进 `research_refs.json`（schema 见
`references/report-template.md`），然后做两层验证：

**语义验证（模型必须自己做）**：对每条引用问"来源页面真的支撑我引用它的那句话
吗？"→ `supports` / `partial_support` / `not_in_source`（丢弃或降级为线索）。

**机械验证（跑脚本）**：

```bash
python scripts/verify_refs.py --refs research_refs.json --out verify_report.md
```

五态判定：`verified` / `partial` / `unreachable`（需人工复核）/ `invalid` /
`unverified`。选项：`--offline`（仅结构检查）、`--strict`（CI 模式）、
`--profile medical`（医学期刊层预设：Cochrane/BMJ/ClinicalTrials/NMPA/CDC/
NICE/万方并入 journal 层；社区层来源自动标注"不得支撑医学结论"）、
`--export bibtex,csv`（仅 verified 条目的 BibTeX 文献台账 + 全量审计 CSV）。
引用可携带 `url`、`doi` 或 `pmid`（自动解析为 PubMed 链接）——每条 PubMed 链接
都会经 NCBI E-utilities 核实 PMID 真实存在，这才是真正能抓住 AI 编造 PMID 的
一招（PubMed 网页对不存在的 PMID 也返回 2xx）。去重覆盖 URL + DOI + PMID。

**CiteScore 置信度评分（v1.3）**：每份报告头部自动输出 0-100 评分与 A-D 级
（verified +10 / partial +4 / unreachable 0 / unverified −2 / invalid −8，
按条数归一），一眼判断整组引用的可信程度。

**离线模式（--offline）**：只做结构核验（格式/字段/层级/去重），不验证可达性，
因此不产出 verified，最高判 partial——诚实优先于好看。

**医学研究模式（v1.2）**：临床问题——药物疗效、患病率、指南、诊断/治疗论断——
先读 `references/medical-mode.md`（信源金字塔、PubMed 检索式、CEBM 分级对照、
监管/注册信源），再用 `--profile medical --export bibtex,csv` 跑验证器。

### 5. SYNTHESIZE 综合

按 `references/report-template.md` 骨架输出：执行摘要先行；每条关键结论带
置信度分级 + 引用编号；引用表带五态列；`unverified/unreachable` 只出现在
"人工复核"区；以研究缺口、来源分歧、后续追问收尾。

## 文件

| 文件 | 何时用 |
|---|---|
| `scripts/verify_refs.py` | VERIFY 阶段机械验证（纯标准库、跨平台、控频） |
| `references/search-strategies.md` | SEARCH 阶段前必读 |
| `references/report-template.md` | SYNTHESIZE 骨架；引用 schema |
| `references/medical-mode.md` | 医学/临床研究前必读（v1.2） |
| `examples/demo_refs.json` | 通用演示：8 条引用，3 个埋雷伪造 |
| `examples/medical_refs.json` | 医学演示：PMID/DOI 引用 + 假 PMID 与重复 PMID 埋雷 |

## 诚实边界

- 指向真实存在、内容可信页面的伪造引用能通过机械层；语义层可能抓住——那是模型
  判断，不是保证。
- `unreachable` ≠ 假。
- 可复现演示：`python scripts/verify_refs.py --refs examples/demo_refs.json`
  （8 条引用、3 个埋雷全被抓住——实测 7.7 秒）。
- 医学演示：`python scripts/verify_refs.py --refs examples/medical_refs.json
  --profile medical --export bibtex,csv`（真实托珠单抗/sJIA 文献；编造 PMID 被
  E-utilities 抓住，重复 PMID 被 PMID 去重抓住）。

## FAQ（常见疑问）

**问：verified 的引用就一定真实吗？**
不一定。机械层只能抓可机检的伪造：假 DOI（DOI.org 查无）、假 PMID（E-utilities 查无）、
死链、重复。v1.4 起 DOI 会与官方登记元数据比对标题相似度和年份，"真 DOI 假论文"
这类最像真引用的伪造也能抓出；但指向真实且内容可信页面的伪造引用，仍依赖语义层
（模型判断），无法百分之百保证。

**问：unreachable 的引用该怎么处理？**
它只代表"这次没打开"（404/超时/反爬），不等于编造。人工打开复核；若有网页存档
（如 Wayback Machine）可参考存档版。反复失败且来源关键 → 换信源。

**问：PMID 检查失败是网络问题吗？**
不是。E-utilities 核实走的是官方 API：返回"不存在"就是 PubMed 库里查无此号，
基本可判定编造；只有"校验失败"字样才是网络/接口异常（此时按可达处理并注明）。

**问：每次都要加 --profile medical 吗？**
用 `--easy` 一条命令即可：自动识别医学引用开启医学预设，并自动导出 BibTeX+CSV
台账。通用场景直接跑默认参数就行。

**问：国内网络访问 DOI.org / PubMed 慢怎么办？**
两者均可直接访问且已内置控频与瞬态重试；超时可用 `--timeout 20` 调大。PMID 核验
走 NCBI E-utilities，如遇网络受限，该步会按可达处理并在备注中注明。

**问：能把验证过的引用直接进论文吗？**
可以：`--export bibtex` 只导出 verified 条目（含 PMID 备注列），BibTeX 可直接
导入 Zotero/EndNote；`--export csv` 是全量审计台账，适合导师/编辑核查。

## 环境降级

无联网工具时：如实告知只能做"用户提供材料 + 机械验证"模式，绝不假装能联网搜索。
