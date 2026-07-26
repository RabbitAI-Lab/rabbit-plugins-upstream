---

slug: "accounting-finance"
name: "accounting-finance"
version: 1.0.1
displayName: "财务分析专业套件"
summary: "企业级财务分析与估值建模全套技能，58个专业分析模块，支持批量处理与自动化报告。。面向专业分析师、机构投资者与企业财务部门的全栈财务分析技能套件。包含58个 专家级分析技能，覆盖估值建模、财"
license: "Proprietary"
edition: "pro"
description: |-，可自动提升工作效率
  面向专业分析师、机构投资者与企业财务部门的全栈财务分析技能套件。包含58个
  专家级分析技能，覆盖估值建模、财务分析、风险评估三大核心领域，支持批量
  处理、自动化报告生成与企业级工作流。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务.
tags:
  - Finance
  - 估值分析
  - 财务建模
  - 风险评估
  - 企业级
  - 金融
  - 财务
  - 数据
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Finance"

---

# 财务分析专业套件

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 财务分析专业套件企业级财务分析 | 不支持 | 支持 |
| 财务分析专业套件与估值建模 | 不支持 | 支持 |
| 财务分析专业套件58个专业分析 | 不支持 | 支持 |
| DCF估值建模与敏感性分析 | 不支持 | 支持 |
| 财务舞弊识别(Beneish M-Score) | 不支持 | 支持 |

## 核心能力分类概览

PRO版共包含58个专业分析技能，分为三大领域：

### 一、估值建模（14个技能）
- **DCF估值系列**：零增长、恒定增长、二阶段、三阶段模型（支持概率加权情景分析、蒙特卡洛模拟）
- **可比估值**：PE/PB/PS/PEG估值
- **资本成本**：WACC计算、CAPM股权成本
- **行业特化估值（PRO专属）**：银行、保险、房地产、科技公司估值

### 二、财务分析（26个技能）
- **财务比率与盈利分析**：财务比率框架、杜邦五因素、ROE/ROIC、毛利率、收入、成本、费用分析
- **现金流分析（PRO完整版）**：现金流预测、自由现金流(FCFF/FCFE)、经营/投资/融资现金流、现金流利润调节、现金周期、营运资本
- **资产结构与报表处理（PRO专属）**：资产结构、资产资本匹配、资本结构、有息负债、报表重组、报表提取、数据标准化、附注分析
- **可比公司与竞争分析**：可比公司筛选、可比公司分析、行业基准、竞争定位

### 三、风险评估（18个技能）
- **风险检测与质量评估**：欺诈风险(Beneish模型)、流动性风险、敏感性分析、盈利质量、利润质量、报表质量
- **特殊事项分析（PRO专属）**：关联交易、审计报告、会计政策、会计估计、税务分析
- **决策支持**：趋势分析、投资论点生成、投资组合跟踪、估值报告撰写

## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景（综合流程示例）

以"某科技公司IPO完整估值分析"为例，PRO执行流程：
1. `tech-company-valuation` - 确定科技公司估值方法
2. `dcf-three-stage` - 三阶段DCF估值（含蒙特卡洛）
3. `peer-selection` / `peer-comparison-analysis` - 可比公司筛选与对比
4. `sensitivity-analysis` - 多变量敏感性分析
5. `valuation-report-writer` - 自动生成估值报告

批量监控场景：通过 `batch_analysis.py` 对多只标的并行执行 `fraud-risk-detection`、`earnings-quality-analysis` 等技能，导出Excel对比矩阵。深度尽调场景按"报表提取→标准化→比率分析→杜邦拆解→现金流调节→关联交易→审计→会计政策→欺诈检测→报告生成"链路执行。

## 运行环境与依赖

1. **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
2. **操作系统**: Windows / macOS / Linux
3. **Python版本**: 3.9+（推荐3.11），建议内存8GB+（批量分析与蒙特卡洛模拟）

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python | 运行时 | 必需 | 系统安装或conda环境 |
| numpy/pandas/scipy | Python库 | 必需 | `pip install numpy pandas scipy`（scipy用于蒙特卡洛） |
| matplotlib/openpyxl/jinja2 | Python库 | 可选 | `pip install matplotlib openpyxl jinja2`（图表/Excel/报告模板） |

**API Key 配置**：支持 Wind（`WIND_API_KEY`，中国市场）、Bloomberg（`BLOOMBERG_API_KEY`，全球市场）、同花顺（`THS_API_KEY`，A股行情）。未配置时支持手动导入财务数据；API Key存储在本地config.yaml，不上传服务器。

**可用性分类**：MD+EXEC（Markdown指令+Python脚本执行）。PRO版特性含批量分析、蒙特卡洛模拟、自动化报告生成、行业特化估值模型，完全兼容免费版全部技能与工作流。

## 输入输出格式

**输入关键字段**：`content`（string，可选，处理内容输入，默认全部维度）、`strict_level`（string，可选，审查严格度 strict/normal/loose，默认normal）。

**输出关键字段**：`success`（bool，执行是否成功）、`data.overall_grade`（评级）、`data.total_score`/`data.max_score`（得分）、`data.summary`（摘要）、`data.details[]`（各项检查 item/status/score/comment）、`data.improvements[]`（改进建议 priority/suggestion/expected_gain）、`error`（错误信息，null表示无错误）。

## 依赖说明(补充)

| 依赖项 | 类型 | 必需 | 说明 |
|----|:--:|---:|----|
| LLM | 模型 | 是 | 需要LLM进行智能审查, 推荐GPT-4/智谱GLM-4/DeepSeek |
| API Key | 凭证 | 否 | 使用云端LLM时需要 |

**国内替代方案**: OpenAI GPT → 智谱GLM-4 / 百度文心一言 / 通义千问 / DeepSeek

## PRO企业级配置（文字说明）

PRO版通过 `config.yaml` 配置工作区目录、数据源（主备双源支持缓存与限流控制）、批量分析参数（最大并行数10、单标的超时300秒、失败重试3次）、报告输出（PDF/DOCX/HTML、zh-CN）、估值参数（蒙特卡洛10000次模拟、置信区间0.05-0.95、敏感性变量 growth_rate/discount_rate/terminal_growth）、风险模型（Beneish M-Score / Piotroski F-Score / Altman Z-Score，压力测试 base/adverse/severe 三场景）。

## 常见问题

### Q1：PRO版与免费版如何切换？
PRO版完全包含免费版全部技能。升级后原有分析工作流无需修改，直接运行即可获得增强结果。如需使用免费版行为，可在配置中关闭PRO增强选项。

### Q2：批量分析支持多少只标的？
PRO版支持单批次最多100只标的的并行分析。建议根据数据源API限额调整并行度，避免触发限流。批量结果自动汇总为对比矩阵并导出Excel。

### Q3：估值报告支持哪些格式？
支持PDF、DOCX、HTML三种格式。PDF适合正式提交，DOCX便于团队协作编辑，HTML适合在线展示。所有报告包含图表、敏感性矩阵和风险提示。

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------:|--------|:-------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 重试请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |
