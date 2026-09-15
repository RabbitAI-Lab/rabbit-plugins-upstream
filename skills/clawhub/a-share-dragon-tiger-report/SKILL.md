---
name: a-share-dragon-tiger-report
description: |
  生成 A 股「涨停板龙虎榜深度研判报告」v2.0（21 章结构编号 0–21 + 22 条计算口径 + 财富密码融合层），
  按四层漏斗 L1→L2→L2.5→L3 框架（六条已确认口径 v2，含半年口径 + 增速红线），
  输出 HTML / PDF / PPTX 三件套；内置「十五五 18 方向跟踪池（102 板块 + 12 SW1 + 70 股）」
  及三层核验生成器（reports/build_15th5_report.py），可离线复现 WorkBuddy 侧完整产出。
  当用户要求生成龙虎榜报告、涨停板深度研判、每日收盘复盘、十五五方向四层核验、
  或把 westock / IMA 盘面写入机构风研报时使用。仅交易日生成；非交易日应直接说明休市并结束。
  v1.1（21 章 + §16+，26–38 页 PDF，26 页 PPTX）已被 v2.0 取代：
  v2.0 新增 framework/ 跟踪池数据（102 板块 + 12 SW1 + 70 股 + 口径 v2 结论）与 reports/ 18 方向生成器。
homepage: https://github.com/yjkj999999/a-share-dragon-tiger-strategy
metadata:
  openclaw:
    emoji: 📊
    version: "2.0.0"
    requires:
      binaries:
        - python3
  security:
    credentials_usage: |
      可选：IMA OpenAPI 凭证仅发送至 ima.qq.com；westock MCP 若配置则优先使用。
      未配置时降级为本地 sample_data.json（标注「演示数据 · 非当日行情」），并在报告首页
      显式标注数据口径与延迟。**不构成投资建议**。
    allowed_domains:
      - ima.qq.com
      - '*.myqcloud.com'
---

# A 股龙虎榜深度研判 + 财富密码策略 v2.0

> **口径版本 v2（2026-09-12 定稿，永久生效）**——口径变更须全量重算历史结论并报告 ±N 只敏感度。
>
> **v2.0（2026-09-12 发布）**：在 v1.1 四层漏斗 + 财富密码融合层基础上，新增
> `framework/`（十五五 18 方向跟踪池：102 板块 + 12 SW1 + 70 股 + 口径 v2 结论）
> 与 `reports/build_15th5_report.py`（18 方向三层核验生成器，纯 stdlib、可离线运行）。
> 至此本仓库 = WorkBuddy 侧完整产出（21 章结构 + 22 条口径 + 跟踪池 + 六条口径 v2 + 增速红线 + 26–38 页 PDF / 26 页 PPTX）。

## 0. 触发

- 「生成今日龙虎榜 / 涨停板深度研判报告」
- 「出 HTML / PDF / PPTX 三件套」
- 「跑四层漏斗核验候选 / L1→L2→L2.5→L3」
- 「融合财富密码选股策略」
- 「做十五五六张网 / 新兴支柱 / 未来产业的方向级核验」

## 1. 双平台安装

| 平台 | 技能目录 |
|---|---|
| OpenClaw（大龙虾） | `~/.openclaw/workspace/skills/a-share-dragon-tiger-report/` |
| MiMo Desktop / MiMoCode | `~/.config/mimocode/skills/a-share-dragon-tiger-report/` |

安装命令（CI 或手工均适用）：

```bash
R=/path/to/a-share-dragon-tiger-strategy
mkdir -p ~/.openclaw/workspace/skills/a-share-dragon-tiger-report
mkdir -p ~/.config/mimocode/skills/a-share-dragon-tiger-report
cp $R/skill/SKILL.md $R/skill/README.md $R/skill/skill-card.md ~/.openclaw/workspace/skills/a-share-dragon-tiger-report/
cp $R/skill/SKILL.md $R/skill/README.md $R/skill/skill-card.md ~/.config/mimocode/skills/a-share-dragon-tiger-report/
```

仓库根目录：`<your-org>/a-share-dragon-tiger-strategy`（v1.1 已用真实 org 替换 `your-org` 占位符）。

## 2. 硬性流程

1. **交易日判断**：周一至周五且非 A 股法定节假日；否则回复「今日休市，无需出报告」并 **stop**。
2. **取数优先级**：
   - 第一优先 westock MCP：`data_quote` / `data_kline` / `data_finance` / `data_shareholder` / `data_sector` / `data_changedist` / `data_lhb` / `tool_ranking`
   - 第二降级 IMA 库「A股市场每日盘后复盘」「A股每日涨停板龙虎榜深度研判报告」
   - 第三降级 `strategy/sample_data.json`（演示数据，报告页眉标注）
   - **禁止 WebSearch 作为行情源**
3. **工作目录**：`./dragon-tiger-YYYYMMDD/`，文件前缀 `涨停板龙虎榜深度研判报告-YYYYMMDD`。
4. **四层漏斗**：从候选数据构建 `funnel.Industry` / `funnel.Stock`，调 `funnel.run_funnel` 得 `FunnelResult`（含 L2 入池 / L2.5 剔除 / L3 否决 / 最终通过 + 敏感度）。
5. **评分管道**：把 funnel.l3_pass 喂给 `pipeline.run_pipeline`，得 BUY/WATCH/AVOID 信号表 + α 账本快照。
6. **生成三件套**：调 `scripts/generate_daily.py --date YYYY-MM-DD --out out/dragon-tiger-YYYYMMDD`，HTML/PDF/PPTX 一键产出。
7. **交付**：`present_files` 三件套 + 摘要（定性 / 核心数据 / 主线 / 推荐与规避 / 盘前检查与 α 预算）。

## 3. 报告结构（21 章）

| 章节 | 内容 | 数据源 |
|---|---|---|
| 0 | 报告口径（v2 永久生效）| `calibers.describe()` |
| 1 | 四层漏斗 L1→L2→L2.5→L3 结果表 + 敏感度 | `funnel.run_funnel` |
| 2 | 评分管道 · 风控信号表 | `pipeline.render_signal_table` |
| 3 | α 账本 + 限额检查 | `risk.AlphaLedger.snapshot` |
| 4 | 盘前 6 项检查 | `playbook.PRE_OPEN_CHECKLIST` |
| 5 | 财富密码五层图谱（制度→资金→产业→公司→交易） | `playbook.FIVE_LAYER_MAP` |
| 6 | 行业层（L1）扫描 | `filters.gate_industry` |
| 7 | 个股层（L2）扫描 | `filters.gate_industry`（个股粒度）|
| 8 | 不可交易清单（L2.5）| `filters.gate_tradability` |
| 9 | 财务核验表（L3，含增速红线 + 半年口径）| `filters.gate_fundamental` |
| 10 | 加速剂（熔断阶梯 + 冰点判定）| `formulas.circuit_breaker` + `is_ice_point` |
| 11 | 已确认口径（六条，不得再询问）| `calibers.describe()` |
| 12 | 候选 → 评分 → 风控信号表（管道视角）| `pipeline.run_pipeline` |
| 13 | 凯利建议 + 仓位 N 精算 | `formulas.kelly_fraction` + `position_size` |
| 14 | 五条可证伪预判 | — |
| 15 | 十五五六张网跟踪池（102 板块 + 12 SW1 + 70 股） | westock `data_sector` |
| 16 | 财富密码融合层 §16+ —— 综合分 S、α_max、盘前 6 项、管道信号、账户骨架 | `playbook.playbook()` |
| 17 | 财务核验（半年口径与 ±N 敏感度）| `conclusions_v2.json` |
| 18 | 明日盘前动作清单 | 派生 |
| 19 | 三类风险（系统性 / 主线单点 / 链条分歧） | 派生 |
| 20 | 免责声明 | — |
| 21 | 元数据（数据源 / 时间戳 / 口径版本） | — |

## 3b. 十五五跟踪池与三层核验生成器（v2.0 新增）

仓库内置两套「数据 + 生成器」，使本技能可离线复现 WorkBuddy 侧完整产出：

| 资产 | 路径 | 内容 |
|---|---|---|
| 跟踪池快照 | `framework/baseline_15th5_20260911.json` | 十五五 18 方向（6 张网 + 6 新兴支柱 + 6 未来产业）：**102 板块**（boards_unique=102）、**12 SW1**（ind_layer=12）、**70 股**（stocks_unique=70）；含三层核验分位 / 额比 / 区间位置 |
| 口径 v2 结论 | `framework/conclusions_v2_20260911.json` | 六条已确认口径 v2 + 增速红线（硬线 / 减分线）+ L2 / L2.5 / L3 结果 + ±N 敏感度 |
| L1 行业表 | `framework/L1_industries_20260911.json` | 31 个 SW1 行业代码→名称映射 |
| 18 方向生成器 | `reports/build_15th5_report.py` | 纯 stdlib，读 `reports/cache/`，产出「十五五六张网与产业方向三层核验报告」HTML（≈133 KB，含 18 方向 × 板块 / 个股三层核验）|

运行三层核验生成器（无需联网，用内置快照）：

```bash
cd reports && python3 build_15th5_report.py
# → 生成 十五五六张网与产业方向三层核验报告-20260911.html
```

跟踪池口径校验（与 `conclusions_v2` 一致）：硬线 中报同比 ≤ 0 排除；减分线 中报同比 > 0 但 < 上一年度增速 50% 时 −15 分。50% 相对线为框架默认值，收紧为「任何减速即排除」会使过会再减 1 只（恒瑞医药），须随报告披露 ±N 敏感度。

## 4. 六条已确认口径（v2 · 不得再向用户询问）

唯一来源：`strategy/calibers.py`。

| # | 口径 | v2 取值 | 实现模块 |
|---|---|---|---|
| ① | 国企央企背景 | **偏好项**（+6 分），不是门槛 | `filters.gate_fundamental` soe_background |
| ② | 产业偏好 | **新兴科技成长优先**（+8 分） | `filters.gate_fundamental` emerging_tech |
| ③ | 净利润增长率 | **半年口径**（最新中报年内同比） | `filters.gate_fundamental` interim_yoy |
| ④ | 单年亏损 | **减分项**（−10 分）；连续两年年报亏损 = 否决 | `filters.gate_fundamental` annual_loss_years |
| ⑤ | 「链」形态主题 | **跳过 L1 否决权**（行业层仅定性） | `calibers.CHAIN_THEMES` + `filters.gate_industry` |
| ⑥ | 基础可交易性 | **L2.5 独立层**（位于 L2 与 L3 之间） | `filters.gate_tradability` |

**增速红线**（口径③的量化）：

- 硬线：中报同比 ≤ 0 → 排除
- 减分项：中报同比 > 0 但 < 上一年度增速的 50% → 重大减分 −15 分

**50% 相对线**是框架自定默认值，非市场共识。收紧为「任何减速即排除」会使过会数量再减 1 只（恒瑞医药示例），**必须随报告首页披露该 ±N 只敏感度**。

## 5. 技术规格

| 项 | 规格 |
|---|---|
| 框架 | L1 → L2 → L2.5 → L3 四层漏斗 + 财富密码融合层 |
| HTML | 数据驱动版模板；可选 ECharts（`assets/echarts.min.js`）注入；MS 色 #002B5C / #C5A572 / #60A3D9；涨红跌绿；`@media print` |
| HTML 图 | 6 张（资金流 / 板块热度 / 个股分位 / 估值 / 龙虎榜席位 / 风险矩阵） |
| PDF | Playwright `sync_playwright`，先 `emulate_media("print")` 再 goto，等待 `__chartsReady===true`，**26–38 页** |
| PPTX | python-pptx，**26 页**，3 个原生图表（PIE + 2 BAR），PingFang SC 注入 a:latin/a:ea/a:cs，BAR 类目倒序；**v2.0 已将跟踪池与 18 方向生成器数据驱动化（framework/），PPTX 模板当日数据注入仍待函数式重写（已知限制，不影响 HTML/PDF）** |
| 计算口径 | **22 条**（含 L2.5 可交易性 + 增速红线 + 半年口径）|
| 字体 | PingFang SC（中文），Microsoft YaHei（备选）|
| 色板 | 涨红 #C1272D / 跌绿 #1E8449（中国 A 股习惯） |

## 6. 策略包结构（`strategy/`）

| 模块 | 行数 | 职责 |
|---|---:|---|
| `calibers.py` | 88 | 六条已确认口径（v2 永久生效）+ 增速红线常量 |
| `formulas.py` | 215 | S / α / 仓位 N / 斐波那契 / 凯利 / 熔断 / 冰点 |
| `filters.py` | 180 | 闸门（L1 / L2.5 / L3）+ 批量过闸 |
| `funnel.py` | 175 | 四层漏斗 + 历史分位 / 区间位置 / 额比 |
| `risk.py` | 145 | α 预算账本 + 三道限额 + 熔断检查 |
| `pipeline.py` | 165 | 候选 → 评分 → 风控信号表 |
| `playbook.py` | 130 | 投资理念 / PLAN_TARGET / 盘前 6 项 / 账户骨架 |
| `test_formulas.py` | 240 | **107 条自检断言** |
| `run_demo.py` | 130 | 一键 demo |
| `sample_data.json` | 120 | 演示数据（9 个候选 + 7 个行业）|

**跟踪池与生成器（v2.0 新增）**

| 目录 / 文件 | 职责 |
|---|---|
| `framework/baseline_15th5_20260911.json` | 十五五 18 方向跟踪池（102 板块 + 12 SW1 + 70 股）+ 三层核验快照 |
| `framework/conclusions_v2_20260911.json` | 六条口径 v2 + 增速红线 + L2/L2.5/L3 结论 + 敏感度 |
| `framework/L1_industries_20260911.json` | 31 个 SW1 行业代码→名称 |
| `reports/build_15th5_report.py` | 18 方向三层核验生成器（纯 stdlib） |
| `reports/cache/` | 生成器所需快照（themes_*.json / ind_*.json / reuse_style.html 等） |

总代码量约 **1,700 行**（不含 HTML/PDF/PPTX 模板与跟踪池数据）。

## 7. 策略包工具脚本

```bash
# 公式自检（必跑，0 失败才视为可用）
python3 strategy/test_formulas.py
# → 通过 107 / 失败 0

# 一键 demo（无需联网）
python3 strategy/run_demo.py
# 或指定数据：
python3 strategy/run_demo.py --data strategy/sample_data.json --equity 2000000 --stage II

# 生成一日三件套
python3 scripts/generate_daily.py --date 2026-09-12 --out out/dragon-tiger-20260912

# 生成十五五 18 方向三层核验报告（离线，用内置快照）
cd reports && python3 build_15th5_report.py
```

## 8. 常见失败模式与陷阱

| 陷阱 | 症状 | 修法 |
|---|---|---|
| 月线两套口径混用 | 报告之间分位/额比不可比 | rank/lo/hi **保留**当月；额比 **剔除**当月（`funnel.amount_ratio(amounts[:-1])`）|
| 用 `volume` 算额比 | 忽略价格因素 | 必须用 `amount`（成交额）|
| 字段名错位 | 同比找不到 | `data_finance` 营收同比 = `TORGrowRate`（**非** `OperatingRevenueYOY`）；归母同比 = `NPParentCompanyYOY` |
| 涨跌颜色 | 与海外习惯混淆 | 涨红 #C1272D / 跌绿 #1E8449（中国 A 股）|
| 半年 vs 年度 | 整批结论翻转 | 报告首页必须写死「半年口径」，并报告 ±N 只敏感度 |
| L2.5 与 L3 合并 | 把「不可交易」误报为「基本面不通过」 | L2.5 必须在 L3 之前，剔除结果**单独**列入「不可交易清单」|
| PPTX 复用旧数据 | 当日数据 vs 2026-09-11 硬编码混用 | v1.1 限制已知，v2.0 将 make_pptx 改造为函数式 API |

完整 11 项陷阱见 `docs/wealth-password-strategy.md` §10。

## 9. 推送到 GitHub 与定时任务

```bash
cd a-share-dragon-tiger-strategy
git init
git add .
git commit -m "feat: A-share dragon-tiger v2.0 (caliber v2, tracking pool 102+12+70, 15th-5 generator)"
git remote add origin git@github.com:yjkj999999/a-share-dragon-tiger-strategy.git
git push -u origin main
```

定时任务：将「交易日 18:32 生成全量融合版三件套」注册为 durable cron；非交易日直接结束。
仓库不内置 cron —— 接入方（OpenClaw / MiMoCode / WinAutomation 等）按各自调度器配置。

## 10. 依赖

- **Python 3.10+**：`python-pptx`、`lxml`、`Pillow`、`playwright`
- **PDF**：Playwright 自带 chromium（`pip install playwright && playwright install chromium`）
- **可选**：westock MCP（实时取数）、IMA OpenAPI（T-1 降级）

## 11. 免责声明

本 Skill 仅供教育与研究。数据可能为 T-1；任何收益数字为情景或历史，**不构成投资建议**。
市场有风险，投资需谨慎。

---

**Author**

本 Skill 由 **Wang Dongjie 王东杰** 创作

资深复合型战略财务专家 · 上市公司资本运作操盘手 · 集团化财务管控与风险治理高级工程师

Wdj_@163.com · 13952453499