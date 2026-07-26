---
name: company-deep-analysis
version: 1.0.11
description: |
  A股/港股公司深度分析。输入公司名称或股票代码，自动完成数据采集到估值分析的全流程：
  数据采集 → 公司画像 → 产业链五力 → 竞争护城河 → 财务四维 → 相对估值。
  输出双产物：公司深度分析报告 + 投研简报
  支持单步模式：用户指定"财务情况/财务分析/公司画像/公司基本面"时，按路由表只跑对应步骤并输出对应单文件。
  触发词：公司分析 / 深度分析 / 公司调研 / 投资初筛 / 深度调研 / 公司研究 / 行业研究 / 投研简报 / 财务情况 / 财务分析 / 公司画像 / 公司基本面
metadata:
  market: ["A股", "港股"]
  output_format: ["html", "md"]
  display_name: "公司深度分析助手"
  requires:
    pip: ["akshare", "requests", "pandas", "lxml", "html5lib"]
  optional_pip: ["yfinance", "matplotlib"]
  python_bins: ["python3", "python"]
---

# 公司深度分析助手（A 股 / 港股）

输入 A 股/港股公司名称或股票代码，**默认执行全流程分析，输出双产物**：
- MD 深度分析报告（`{公司名}_深度分析报告_{YYYYMMDD}.md`）
- HTML 投研简报（`{公司名}_投研简报_{YYYYMMDD}.html`）

> 单步模式：用户说"看一下 XX 的财务" / "XX 的公司画像" → 只跑对应步骤，输出单文件。

## 执行模式路由

| 用户关键词 | 模式 | 步骤 | 输出 |
|-----------|------|------|------|
| **（默认）** | `full` | Step0-5 全部 | 双产物 |
| **财务** / **财务情况** / **财务分析** | `financial` | Step0 + Step4 | `_财务分析.md` |
| **画像** / **公司画像** / **公司基本面** | `profile` | Step0 + Step1 | `_公司画像.md` |

关键词优先级：`financial` > `profile` > `full`。

路由判定后在对话中展示：
```
🔍 识别到：{公司全称}（{代码}）· {市场} · 即将进入「{模式}」模式，输出：{文件清单}
```

---

## Step0：环境准备与数据采集

> 全部 AI 内部规则（基准年判定、框架选择、权重表、写作硬要求、降级策略）见 `references/ai-internal-rules.md`，跑报告前必须先读。

### 0.0 安装依赖

```bash
pip install -r <skill_dir>/requirements.txt
```

核心依赖：`akshare`（A股/港股三表主力）、`requests`、`pandas`、`lxml`、`html5lib`；可选：`yfinance`（港股容错）、`matplotlib`（图表渲染）。

### 0.1 公司识别

**市场范围**：仅 A 股 + 港股。美股 / 未上市公司 → 直接拒绝。

**代码识别**：

| 输入特征 | 模式 | 市场 |
|---------|-----|-----|
| 5 位纯数字 | 港股 | 港股 |
| 6 位纯数字 | A 股 | A 股 |
| `hk00700` / `sh600519` / `sz000001` / `bj430047` | 带前缀 | 按前缀 |
| `00700.HK` / `600519.SH` | 带后缀 | 按后缀（规整为 `hk01000` / `sh600519`） |
| 公司名 | 搜索 | 候选判定 |

代码规整：所有变体统一为 `hk{5位}` / `sh{6位}` / `sz{6位}` / `bj{6位}`。

- **公司名模式**：WebSearch "<公司名> 股票代码"，然后 `$PY scripts/collect_data.py {CODE}` 验证。多候选列出 ①②③ 让用户选。
- **代码模式**：`$PY scripts/collect_data.py {CODE}` 反查全称。无效则提示检查。
- **公司名+代码模式**：同代码模式验证匹配性，匹配直接进入，不弹确认。

### 0.2 数据采集

```bash
$PY <skill_dir>/scripts/collect_data.py {CODE}
```

写入 `/tmp/{CODE}_data.json`。

降级策略（`collect_data.py` 内置，每数据项独立降级，详见 `ai-internal-rules.md`）：

- **A股**：AKShare → 新浪/东财/腾讯 HTTP → **WebSearch 兜底**
- **港股**：AKShare → yfinance(容错) → 东财 emweb HTTP → **WebSearch 兜底**

衍生项 ebitda（估值用，港股跳过）。每项自动在 `_数据源` 字段标注实际来源。

**批量模式**：

```bash
$PY <skill_dir>/scripts/collect_data.py --quotes {CODE},{竞对1},{竞对2}      # 批量行情
$PY <skill_dir>/scripts/collect_data.py --finances {CODE},{竞对1},{竞对2}    # 批量财务比率
```

### 0.3 定性补充

```
WebSearch "<公司名> 研报 战略"
WebSearch "<公司名> 公告 管理层 重大事项"
```

### 0.4 数据质量评级

- **A级**：AKShare 全部命中 / **B级**：1-3 项降级 / **C级**：多项 WebSearch 兜底，仅定性分析

---

## Step1：公司画像

**输入**：`/tmp/{CODE}_data.json` 的 f10、em_info、blocks。

1. **基本信息** + 业务模式标签（按 `ai-internal-rules.md §1.0`）
2. **主营业务**与收入构成
3. **股权结构**（前十大股东）
4. **用户规模**（条件性触发，规则见 `ai-internal-rules.md §1.1`）

输出：按 `templates/company-profile-template.md` 生成 `{公司名}_公司画像.md`。

---

## Step2：产业链分析

**输入**：Step1 业务模式标签 + data.json 的 f10.行业分析。

1. **行业大盘**：规模 / CAGR / CR5 集中度 / 生命周期
2. **五力分析**：按 `ai-internal-rules.md §2.0` 选框架（A/B/C），加载 `references/porter-five-forces-template.md` 对应章节执行

每项评级：强/中/弱 + 至少 2 条数据支撑。

---

## Step3：竞争与护城河

**输入**：data.json 的 reports、quote。

### 3.1 识别竞对（3-8 家）

> **核心原则**：从"业务模式"和"产业链位置"双维度匹配。先找同行业（高可比），再找上下游/相似业务（中可比），最后是行业参考（低可比）。

步骤：
1. 按营收占比拆目标公司主业（占比最高），可比公司必须对标主业
2. 三层选取：
   - 🟢 **高可比**：业务模式相同 + 主营行业相同
   - 🟡 **中可比**：主营行业不同但业务模式类似
   - 🔴 **低可比**：业务模式差距大，仅作行业参考
3. 每家公司必须给可比性标注 + 理由
4. 行业基准对比**不能替代**可比公司对比

**反例警示**：
- ❌ 把行业平均毛利率/PE 当作"可比公司"
- ❌ 把业务模式差距大的公司（如 FPGA 芯片设计 vs 存储分销）放在同一张估值表比较

**报告呈现**：深度报告 §2.3/§4.1 只列高可比 2 家；§3.6 财务对比列全部可比公司。投研简报不展开可比公司。

### 3.2 护城河分析

按 `ai-internal-rules.md §2.5` 选框架（A-F），加载 `references/moat-analysis-framework.md` 执行。三轮反问机制按数据等级执行（A 级 ≥ 3 轮，B/C 级 ≥ 2 轮）。

### 3.3 竞争优势综合判断（客户视角 3 问）

---

## Step4：财务四维

**输入**：data.json 的 lrb / fzb / llb / finance。

1. 按 `ai-internal-rules.md §0.1` 判定**基准年**
2. 按 `ai-internal-rules.md §3.0` 选**财务权重**
3. 盈利能力 / 偿债能力 / 营运能力 / 成长能力 四维分析
4. **杜邦分解**（必做，亏损公司用替代公式）
5. 综合评分

输出：按 `templates/financial-analysis-template.md` 生成 `{公司名}_财务分析.md`。

---

## Step5：相对估值

按 `ai-internal-rules.md §7.1` 选 1-3 种方法。

```bash
$PY <skill_dir>/scripts/valuation.py {CODE} peers.json
```

交叉验证（至少 2 个变体）：偏差 < 15% 取均值，15-30% 标注分歧，> 30% 取更保守估值。

---

## Step6：生成产物

### 6.0 模板硬约束（最高优先级，生成前必读）

> **模板中每一个表格、每一个小节都是必填项。** 详见 `references/ai-internal-rules.md` §8.3。
> **例外**：标注「（条件性触发）」的小节（如 §1.4）不适用时完全跳过；模板末尾的「输出前自检清单」是内部工具，禁止输出到报告中。详见 `ai-internal-rules.md` §8.3.1 和 §8.3.2。

**核心规则**：
- 模板中的**所有表格**必须保留。数据不足时单元格填 `N/A` 或标注 `口径差异大，不采纳`，**禁止把表格变成文字、禁止删除表格行列**
- 模板中的**小节标题不可删除**，无数据时保留标题 + `暂无数据`
- 表格列数、列名、行标签与模板完全一致

> ⚠️ **生成报告后，必须使用模板末尾的「输出前自检清单」逐条内部勾选，未通过则报告不合格。自检清单本身不输出到报告中。**

### 产物映射

写任何文件前，**必须先用 Read 读取对应模板完整内容**。

| 模式 | 产物 | 模板 |
|------|------|------|
| full | `{公司名}_深度分析报告_{YYYYMMDD}.md` | `templates/deep-analysis-report-template.md` |
| full | `{公司名}_投研简报_{YYYYMMDD}.html` | `templates/briefing-card-template.html` |
| financial | `{公司名}_财务分析_{YYYYMMDD}.md` | `templates/financial-analysis-template.md` |
| profile | `{公司名}_公司画像_{YYYYMMDD}.md` | `templates/company-profile-template.md` |

### 清理

```bash
rm -f /tmp/{CODE}_data.json
```
