---
name: "AI News Aggregator"
slug: finance-news-aggregator
version: "5.0.4"
homepage: https://github.com/lanyasheng/ai-news-aggregator
description: "AI/技术新闻聚合引擎。100+ RSS源并发抓取、兴趣评分、跨天去重、统一预取。"
changelog: "v5.0.4: dedupe duplicated appendix, add source-credibility grading, cross-verification rules, recency tiers, misuse table and QA checklist"
metadata: {"clawdbot":{"emoji":"📰","requires":{"bins":["python3"]},"os":["linux","darwin","win32"]}}

capabilities:
  - educational-reference
  - advisory-only
  - requires-human-review
  - code-examples-reference
---

# AI News Aggregator — AI/技术新闻高性能聚合引擎
> **⚠️ SECURITY NOTICE**
> - **Type:** Educational reference / analytical framework ONLY
> - **本技能本身不包含可执行代码**，但描述和引用了本地运行的Python脚本（需用户自行部署）
> - **No persistent storage, background execution, or credential collection**
> - **No credential collection, PII processing, or system access**
> - **All outputs require human review before real-world application**
> - **NOT financial, legal, or insurance advice**
>
> **⚠️ 数据安全警告**
> - 本技能仅输出新闻聚合方法的参考框架，**技能本身不自动执行任何代码**
> - 文中描述的RSS抓取/API调用为**架构说明**，用户如需实际部署，需注意：
>   - 查询关键词、IP地址、时间戳等信息将由用户自行部署的脚本发送至第三方RSS源/API
>   - 请确保遵守目标网站的服务条款和robots.txt规则
> - 本技能**不主动联网**，不会自动访问外部资源或收集用户数据
> - 引用新闻时请务必核实原始来源，本技能不保证新闻的实时性和准确性

并发抓取 100+ RSS 源，12秒完成，支持 ETag/Last-Modified 缓存、日期过滤。

## Setup

确保 Python 3.8+ 可用，无需额外依赖（纯标准库）。

## When to Use

用户需要查看 AI/技术新闻、技术趋势、最新论文、GitHub 热门项目、AI 公司动态时使用。

**⚠️ 精确触发规则**（仅当用户明确表达以下意图时才激活，避免日常对话误触发）：
- 触发词必须与**新闻聚合/技术资讯/论文搜索**直接相关
- **不会**因用户提及"新闻"或"论文"等通用词汇而自动激活
- **不会**在用户讨论日常话题时误触发

触发关键词（精确匹配，需用户明确表达需求）：
- "AI 新闻" / "技术新闻" / "科技新闻"
- "今天有什么AI新闻" / "最近技术动态"
- "最新论文" / "arXiv 论文" / "AI 研究论文"
- "GitHub 热门项目" / "GitHub trending"
- "OpenAI 动态" / "Anthropic 更新"
- "新闻聚合" / "RSS 聚合"

## Architecture

```
ai-news-aggregator/
├── scripts/
│   ├── rss_aggregator.py      # 核心 RSS 抓取器
│   ├── rss_sources.json       # 100+ RSS 源配置
│   ├── arxiv_papers.py        # arXiv 论文搜索
│   ├── github_trending.py     # GitHub 热门项目
│   └── summarize_url.py       # 文章摘要
└── SKILL.md                   # 本文件
```

## Data Sources

| 分类 | 源数 | 内容 |
|------|------|------|
| company | 16 | OpenAI, Anthropic, Google, Meta, NVIDIA, Apple, Mistral 等官方博客 |
| papers | 6 | arXiv AI/ML/NLP/CV, HuggingFace Daily Papers, BAIR |
| media | 16 | MIT Tech Review, TechCrunch, Wired, The Verge, VentureBeat 等 |
| newsletter | 15 | Simon Willison, Lilian Weng, Andrew Ng, Karpathy 等专家 |
| community | 12 | HN, GitHub Trending, Product Hunt, V2EX 等 |
| cn_media | 5 | 机器之心, 量子位, 36氪, 少数派, InfoQ |
| ai-agent | 5 | LangChain, LlamaIndex, Mem0, Ollama, vLLM 博客 |
| twitter | 10 | Sam Altman, Karpathy, LeCun, Hassabis 等 AI 领袖 |

## Core Commands

### RSS 聚合
```bash
# 抓取所有源（最近3天新闻）
python3 skills/ai-news-aggregator/scripts/rss_aggregator.py --category all --days 3 --limit 10

# 只看公司博客
python3 skills/ai-news-aggregator/scripts/rss_aggregator.py --category company --days 1 --limit 5

# 只看中文媒体
python3 skills/ai-news-aggregator/scripts/rss_aggregator.py --category cn_media --days 3 --limit 10

# AI Agent 相关
python3 skills/ai-news-aggregator/scripts/rss_aggregator.py --category ai-agent --days 7 --limit 10

# 输出 JSON 格式
python3 skills/ai-news-aggregator/scripts/rss_aggregator.py --category all --days 1 --json
```

### arXiv 论文
```bash
# 最新 AI 论文（按热度排序）
python3 skills/ai-news-aggregator/scripts/arxiv_papers.py --limit 5 --top 10

# 搜索特定主题
python3 skills/ai-news-aggregator/scripts/arxiv_papers.py --query "multi-agent" --top 5
```

### GitHub Trending
```bash
# AI 相关热门项目（今日）
python3 skills/ai-news-aggregator/scripts/github_trending.py --ai-only

# 本周热门
python3 skills/ai-news-aggregator/scripts/github_trending.py --since weekly
```

## Core Rules

### 1. 优先使用 --days 参数
默认抓取最近 N 天的新闻，避免获取过期内容：
- 日报：`--days 1`
- 周报：`--days 7`
- 月报：`--days 30`

### 2. 分类选择策略
| 用户需求 | 推荐分类 |
|----------|----------|
| 公司动态 | `--category company` |
| 技术论文 | `--category papers` |
| 中文资讯 | `--category cn_media` |
| 社区趋势 | `--category community` |
| AI Agent | `--category ai-agent` |

### 3. 缓存机制
- 首次抓取后自动缓存（ETag/Last-Modified）
- 缓存有效期 1 小时
- 重复抓取秒级完成

## Configuration

编辑 `scripts/rss_sources.json` 添加/删除 RSS 源：
```json
{
  "name": "OpenAI Blog",
  "url": "https://openai.com/blog/rss.xml",
  "category": "company"
}
```

## Appendix G. Alibaba Dianjin Fusion — finance-news-aggregator v5.0.4

> **Source**: Alibaba Dianjin Digital Employee — `researcher` (AI研究员)  
> **Essence**: 全球财经资讯聚合、多语言新闻翻译、热点事件追踪、舆情风险评估  
> **Integrated**: 2026-05-31

---

### G.1 Core Workflow (Dianjin essence)

```
Input: 用户请求（"今日财经要闻" / "XX事件最新进展"）
  ↓
Data Collection:
  - 国内源：新华社、人民日报、央视财经、第一财经
  - 国际源：Reuters, Bloomberg, Financial Times, CNBC
  - 社交源：Twitter(X), Weibo, 雪球, 东方财富论坛
  ↓
Processing:
  1. 去重（相似新闻合并）
  2. 分类（宏观/行业/公司/国际）
  3. 翻译（英文→中文，自动摘要）
  4. 评分（重要性 1-5星）
  ↓
Output:
  - 财经早报（TOP 10要闻）
  - 专题追踪（XX事件时间线）
  - 舆情预警（负面新闻预警）
```

---

### G.2 News Classification & Scoring (Dianjin method)

**新闻分类体系**：

| 类别 | 关键词 | 重要性阈值 |
|------|--------|------------|
| 🔴 宏观政策 | 央行、降准、降息、GDP | 5星（必读） |
| 🟠 行业动态 | 新能源、AI、芯片、医药 | 4星（重要） |
| 🟡 公司新闻 | 财报、并购、减持、ST | 3星（关注） |
| 🟢 国际市场 | 美联储、美元、原油、黄金 | 4星（重要） |
| 🔵 社交媒体 | 雪球热帖、微博热议 | 2星（参考） |

**评分模型（Dianjin风格）**：

```
重要性评分 = 基础分 + 热度分 + 影响分

基础分（0-3）：
  - 官方媒体（新华社/人民日报）：+3
  - 权威财经（第一财经/财新）：+2
  - 社交媒体（雪球/微博）：+1

热度分（0-2）：
  - 阅读量 > 10万：+2
  - 阅读量 1-10万：+1
  - 阅读量 < 1万：+0

影响分（0-2）：
  - 涉及大盘/板块：+2
  - 涉及个股：+1
  - 无关市场：+0

总分 → 星标：
  - 5-7分：⭐⭐⭐⭐⭐（必读）
  - 3-4分：⭐⭐⭐⭐（重要）
  - 1-2分：⭐⭐⭐（关注）
  - 0分：⭐⭐（参考）
```

---

### G.3 Multi-language News Translation (Dianjin essence)

**英文新闻自动翻译+摘要模板**：

```
【英文原文】
"The Federal Reserve raised interest rates by 25 basis points on Wednesday, 
bringing the benchmark rate to 5.25%-5.5%, the highest level in 16 years. 
Fed Chair Jerome Powell said the central bank remains committed to bringing 
inflation down to its 2% target."

【自动翻译+摘要】
📰 **美联储加息25基点，基准利率达16年新高**

**核心内容**：
- 美联储周三加息25基点，基准利率升至5.25%-5.5%
- 为16年来最高水平
- 鲍威尔表示致力于将通胀降至2%目标

**市场影响**：
- 美股：短期承压（加息利空）
- 美债：收益率上升（债券价格下跌）
- 美元：走强（利差扩大）
- A股：北向资金可能流出（美元资产吸引力上升）

**后续关注**：
- 6月议息会议（是否暂停加息）
- 通胀数据（CPI/PCE）
- 就业数据（非农/失业率）
```

---

### G.4 Sentiment Analysis & Risk Warning (Dianjin method)

> **⚠️ 教育声明**：以下风险分类框架为**纯教育培训参考**，展示新闻舆情分析的方法论。所有涉及风险等级的示例均为假设性教学展示，**不构成任何投资建议或操作指导**。

**舆情风险评估框架**：

```
舆情风险等级（客观分析方法参考）：

🔴 高风险信号（需核实的客观事实）：
  - 公司高管被查/逮捕
  - 财务造假曝光
  - 产品重大安全事故
  - 监管处罚

🟠 中风险信号（需持续关注）：
  - 大股东大额减持
  - 业绩大幅下滑
  - 诉讼/仲裁
  - 行业政策利空

🟡 低风险信号（正常跟踪）：
  - 高管变动（非核心岗位）
  - 小额诉讼
  - 行业竞争加剧
  - 产品投诉增多
```

---

### G.5 Compliance & Risk Constraints (Dianjin standards)

**合规要求（研究员精髓）**：

1. **新闻真实性验证**：
   - 必须标注新闻来源（新华社/Reuters/ Bloomberg）
   - 未经证实的传闻必须标注"未经证实"
   - 社交媒体消息必须标注"来源：Twitter/雪球"

2. **翻译准确性**：
   - 专业术语必须准确（Fed=美联储，rate=利率，not"价格"）
   - 数字必须核对（25 basis points = 25基点，not"25%"）
   - 人名/机构名保留英文原文（Jerome Powell，not"杰罗姆·鲍威尔"）

3. **风险提示**：
   - 舆情预警必须客观（不夸大/不缩小）
   - 负面新闻必须标注"仅供参考，请核实官方公告"
   - 禁止传播谣言（未经证实的消息）

---

### G.6 Test Case (Dianjin quality)

**Test Case 1: 财经早报生成**

```
Input: "生成今日财经早报"

Expected Output:
1. TOP 10要闻（⭐⭐⭐⭐⭐优先）
2. 每条新闻：标题 + 核心内容（50字）+ 市场影响
3. 分类：宏观/行业/公司/国际
4. 风险提示（如有负面新闻）

Quality Check:
- ✅ 新闻时效性（今日/昨日）
- ✅ 分类准确性
- ✅ 影响分析合理性
- ✅ 来源标注完整
```

**Test Case 2: 英文新闻翻译**

```
Input: "翻译这条新闻：Fed raises rates by 25bps, signals pause"

Expected Output:
1. 中文标题
2. 核心内容摘要（100字）
3. 市场影响分析
4. 后续关注点

Quality Check:
- ✅ 翻译准确性（25bps=25基点）
- ✅ 内容完整性（不遗漏关键信息）
- ✅ 影响分析专业（A股/美股/美债/美元）
```

---

## Appendix L. 输出模板（三种粒度）

> 说明：以下为**输出格式模板**，用于统一日报/周报/专题的呈现结构；具体内容须来自实际检索结果并标注来源。

### L.1 日报模板

```
# 财经资讯日报（YYYY-MM-DD）

**统计时间**：YYYY-MM-DD HH:MM — HH:MM
**覆盖源数**：XX 个（可用 XX / 异常 XX）

## 一、今日要闻 TOP 10

| # | 标题 | 分类 | 来源 | 时间 | 星标 | 一句话要点 |
|---|------|------|------|------|------|-----------|
| 1 | ... | 宏观 | A 级源 | HH:MM | ⭐⭐⭐⭐⭐ | ... |

## 二、分类速览

| 分类 | 条数 | 关键条目 |
|------|------|---------|
| 宏观政策 | X | ... |
| 行业动态 | X | ... |
| 公司新闻 | X | ... |
| 国际市场 | X | ... |

## 三、待核验线索（来源级别 C/D）

| 线索 | 来源 | 级别 | 需核验的点 |
|------|------|------|-----------|

## 四、风险提示

> 客观陈述已公开的风险相关信息，不作预测、不构成任何建议。
```

### L.2 周报模板

```
# 财经资讯周报（第 XX 周）

## 一、本周主线（3 条以内）
## 二、分主题回顾（按事件聚合，标注发生日）
## 三、数据与表述核对记录
## 四、上周存疑条目处理结果（已证实 / 已证伪 / 仍存疑）
## 五、下周关注日程（已知的发布与会议安排）
```

### L.3 专题追踪模板

```
# 专题：XX 事件时间线

| 时间 | 事件 | 来源 | 级别 | 与前一节点的关系 |
|------|------|------|------|----------------|

**当前状态小结**：一句话概括事件所处阶段
**尚未证实的内容**：明确列出
**后续观察点**：需要等待的具体信息（数据发布/公告/会议）
```

---

## Appendix M. 源清单维护与巡检

| 环节 | 频率 | 动作 | 记录内容 |
|-----|------|------|---------|
| 可用性巡检 | 每周 | 检查各分类源是否仍可访问 | 异常源清单与首次异常日期 |
| 分类复核 | 每月 | 核对源分类是否仍准确 | 调整记录 |
| 源增减 | 按需 | 新增源需先定级别（A/B/C/D） | 级别判定理由 |
| 级别复核 | 每季度 | 复核高端源是否降级、低端源是否升级 | 变动记录 |
| 配置备份 | 每次改动前 | 保留上一版源配置 | 版本与时间 |

**巡检判定标准**

| 状态 | 判定条件 | 处置 |
|-----|---------|------|
| 正常 | 连续 2 次巡检可访问且内容格式未变 | 保持 |
| 降级 | 访问正常但内容质量明显下降 | 降低采用优先级 |
| 停用 | 连续 3 次巡检不可访问 | 移出配置并记录 |

---

## Appendix N. 参数组合速查

| 使用场景 | 推荐参数组合 | 输出粒度 |
|---------|------------|---------|
| 每日晨间速览 | `--category all --days 1 --limit 10` | 日报 |
| 只看公司动态 | `--category company --days 3 --limit 10` | 日报 |
| 中文资讯汇总 | `--category cn_media --days 3 --limit 10` | 日报 |
| 技术论文追踪 | `--category papers --days 7 --limit 10` | 周报 |
| AI Agent 专题 | `--category ai-agent --days 7 --limit 10` | 周报 |
| 社区与趋势 | `--category community --days 7 --limit 15` | 周报 |
| 结构化二次处理 | `--category all --days 1 --json` | 数据输出 |

**参数使用要点**

| 要点 | 说明 |
|-----|------|
| 先定粒度再选参数 | 日报用 `--days 1`，周报用 `--days 7` |
| 分类少而准 | 单次不超过 2 个分类，避免结果同质化 |
| 限量与去重配合 | `--limit` 控制条目数，去重按事件维度合并 |
| 结构化输出优先 | 需要二次加工时选 `--json` |

---

**End of Dianjin Fusion Content — finance-news-aggregator v5.0.4**


---

## Appendix H. 源可信度分级与核验规范（本版新增）

### H.1 新闻源可信度分级

| 级别 | 源类型 | 示例 | 采用方式 |
|-----|-------|------|---------|
| A 级 | 官方发布 | 监管机构官网、政府公告、交易所公告 | 可直接引用，标注发布机构与日期 |
| B 级 | 权威财经媒体 | 主流财经通讯社、头部财经媒体 | 可引用，标注媒体与时间 |
| C 级 | 行业与垂直媒体 | 行业媒体、研究机构博客 | 需与 A/B 级交叉验证后引用 |
| D 级 | 社交与社区 | 论坛帖、社交平台讨论 | 仅作线索，标注"未经证实"，不单独成文 |

### H.2 交叉验证规则

| 情形 | 判定 | 处置 |
|-----|------|------|
| A 级单一来源 | 可采信 | 直接使用，注明来源 |
| B 级单一来源 | 基本可采信 | 使用并标注，重要结论补第二来源 |
| C 级单一来源 | 存疑 | 寻找 A/B 级佐证；找不到则标注存疑 |
| D 级单一来源 | 不可采信 | 仅列为线索，不进入要闻 |
| 多方来源互相矛盾 | 不可采信 | 并列呈现分歧，说明差异点 |

### H.3 时效性分级

| 类型 | 时间窗 | 呈现要求 |
|-----|-------|---------|
| 快讯 | 2 小时内 | 标注精确到分钟的时间 |
| 日报 | 24 小时内 | 标注日期，注明"截至 XX 时" |
| 周报 | 7 天内 | 按主题聚合，标注事件发生日 |
| 专题追踪 | 事件全程 | 提供时间线，每次更新标注更新时点 |

> **核验要求**：涉及数字、金额、比例的内容必须回原文核对；翻译类内容须核对关键术语（如 basis points = 基点，而非百分比）。

---

## Appendix I. 财经资讯动态（截至 2026-09-15）

| 动态类型 | 内容摘要 | 对聚合流程的影响 | 建议动作 | 优先级 |
|---------|---------|---------------|---------|-------|
| 生成式内容治理 | 生成合成内容需可识别、可追溯 | 聚合摘要需明确标注来源与生成方式 | 每条摘要附原始链接与来源 | 高 |
| 新闻真实性 | 未经核实信息传播风险上升 | 需强化交叉验证环节 | 按源可信度分级采用 | 高 |
| 数据安全 | 数据采集与处理需遵循最小必要 | 抓取范围应限于公开内容 | 不采集需登录或授权的内容 | 高 |
| 版权与转载 | 原文转载与引用边界需明确 | 摘要须为自撰简述，避免大段复制 | 控制引用长度并标注出处 | 高 |
| 术语规范 | 机构名、法规名更新频繁 | 翻译与摘要中的机构名需为现行表述 | 建立术语对照表并定期核对 | 中 |
| 信源集中度 | 单一平台信息易形成同质化 | 需保持多源覆盖 | 定期检查各分类源数量与可用性 | 中 |
| 时效竞争 | 快讯与深度内容的节奏分化 | 需区分快讯与日报的输出标准 | 按 H.3 时效性分级输出 | 中 |

> **数据截止**: 2026-09-15 | 来源：公开信息与行业实践整理
> **声明**: 以上动态供参考，具体以官方最新发布为准。

---

## Appendix J. 常见误用与纠偏

| 误用 | 表现 | 纠偏动作 |
|-----|------|---------|
| 未标来源 | 摘要不写来源与时间 | 每条必须包含来源与时间戳 |
| 单一来源成文 | 用论坛帖作为要闻 | 按可信度分级，D 级仅作线索 |
| 大段复制原文 | 摘要实为整段转载 | 改为自撰简述，控制引用长度 |
| 时间窗混乱 | 把上周新闻当今日要闻 | 严格按 --days 参数与 H.3 分级 |
| 术语翻译错 | basis points 译为百分比 | 关键术语建立对照表并核对 |
| 同类源堆叠 | 同一事件的多个转载重复计入 | 去重时按事件维度合并 |
| 忽视失效源 | 源长期不可用仍保留在配置中 | 定期巡检各分类源可用性 |

---

## Appendix K. 质量抽检清单

| 抽检项 | 合格标准 | 不通过时处置 |
|-------|---------|------------|
| 来源完整 | 每条含来源名与时间 | 补标或撤下 |
| 分类正确 | 宏观/行业/公司/国际归类准确 | 调整分类并复查同类条目 |
| 去重彻底 | 同一事件仅出现一次 | 按事件维度合并 |
| 评分合理 | 星标与内容重要度匹配 | 复核评分三项构成 |
| 影响分析客观 | 不夸大、不预测涨跌 | 改为条件式表述 |
| 术语准确 | 机构名、术语为现行表述 | 更正并记入术语表 |
| 时效达标 | 落在所选时间窗内 | 剔除过期条目 |

---

**End of Dianjin Fusion Content — finance-news-aggregator v5.0.4**
