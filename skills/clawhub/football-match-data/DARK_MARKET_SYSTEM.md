# 暗盘系统说明书 (Dark Market System)

> 每次新对话开始时，先读这份说明书。所有关键知识都在这里。

---

## 一、系统概述

足球博彩分析系统，目标：**宁缺毋滥，只推荐 4 星以上高置信度比赛**。覆盖 31 个分析维度，Cross-verify 多数据源，Gate 强制拦截不完备分析。

**核心原则**：
- 任何分析缺一个维度都不输出
- 多源交叉验证，差异 > 0.05 自动报警
- 凯利默认 25%（Full Kelly = 100% 破产风险）
- 初盘才是庄家真心话，后续变动是市场博弈

---

## 二、项目结构

```
footy-edge/                        ← 主项目
├── DARK_MARKET_SYSTEM.md          ← 本说明书
├── ampan.py                       ← 入口
├── scripts/
│   └── ampan_analyze.py           ← 一键诊断脚本 ⭐
├── src/footy/
│   ├── data/                      ← 数据采集层
│   │   ├── wubai.py               ← 500.com 欧赔（初盘+即时双解析）
│   │   ├── nowscore.py            ← 捷报网赔率（backup source）
│   │   ├── okooo.py               ← 澳客联赛页赔率
│   │   ├── bifax.py               ← 必发四步验证引擎 ⭐
│   │   ├── ou_data.py             ← 大小球(O/U)盘口采集 ⭐
│   │   ├── understat.py           ← xG 数据
│   │   ├── footballdata.py        ← 历史比赛数据
│   │   ├── intel.py               ← 情报采集
│   │   ├── team_names.py          ← 队名映射
│   │   ├── store.py               ← SQLite 存储
│   │   └── schema.py              ← 数据模型
│   ├── analysis/                  ← 分析引擎层
│   │   ├── orchestrator.py        ← 编排器 + Gate 强制拦截 ⭐
│   │   ├── checklist_runner.py    ← 31 维自动检查清单 ⭐
│   │   ├── cross_verify.py        ← 跨源交叉验证 ⭐
│   │   ├── opening_deviation.py   ← 初盘偏差信号
│   │   ├── company_anomaly.py     ← 公司异常检测
│   │   ├── value.py               ← 凯利/EV/Edge 计算
│   │   ├── cold_detector.py       ← 9 信号冷门检测
│   │   ├── advanced_ah.py         ← 四大操盘模型
│   │   ├── skeleton.py            ← 赔率骨架分类
│   │   ├── bookmaker_mind.py      ← 庄家意图分析
│   │   ├── sniper.py              ← 狙击手
│   │   ├── euro_ah.py             ← 欧亚转换
│   │   ├── odds_signals.py        ← 赔率信号
│   │   ├── confidence.py          ← 置信度计算
│   │   └── discipline.py          ← 纪律约束
│   ├── models/                    ← 数学模型层
│   │   ├── dixon_coles.py         ← Dixon-Coles 泊松模型
│   │   ├── poisson.py             ← 基础泊松模型
│   │   ├── skellam.py             ← Skellam 分布
│   │   ├── form.py                ← 近期状态模型
│   │   └── lambda_adjust.py       ← 泊松系数修正
│   ├── backtest/                  ← 回测
│   │   ├── engine.py              ← 回测引擎
│   │   └── metrics.py             ← 回测指标
│   ├── cli.py                     ← CLI 命令
│   ├── config.py                  ← 配置
│   ├── state.py                   ← 系统状态
│   └── learnings.py               ← 学习记录
└── tests/                         ← 测试 (22个)

ampan-skill/                       ← ClawHub 发布包（同步维护）
```

⭐ = 本次对话新增/重写的核心模块

---

## 三、快速开始

### 3.1 一键诊断（推荐）

```bash
cd footy-edge
python scripts/ampan_analyze.py <fixture_id> --name "主队 vs 客队"
python scripts/ampan_analyze.py <fixture_id> --name "主队 vs 客队" --bifax
```

**输出内容**：
- 📡 实时拉取欧赔（16家）+ 大小球（10家）
- 📋 31 项 Checklist 逐条展示（✅已过 / ❌缺失 / ⚠️警告）
- 📊 已采集数据摘要
- 🚧 Gate 判决（能否输出分析结论）

### 3.2 代码中使用

```python
from footy.analysis.orchestrator import MatchData, gate_analysis, assert_ready

# 创建数据容器
data = MatchData(match_name="德国 vs 美国", fixture_id="1335728")

# 填入数据（手动或自动）
data.odds_instant = (1.85, 3.60, 4.20)
data.odds_opening = (1.72, 3.80, 4.50)
data.odds_count = 16
data.odds_verified = True
data.checklist.mark("01", "16家")

# 查看进度
print(gate_analysis(data))  # ❌ 被拦截: 亚盘未核实, 大小球缺失, ...

# 强制拦截
assert_ready(data)  # RuntimeError 如果缺任何一项！
```

### 3.3 核心 API

```python
# --- 欧赔 ---
from footy.data.wubai import get_odds_full, get_odds, get_opening_odds
full = get_odds_full(fixture_id)         # {"opening": {...}, "current": {...}}
current = get_odds(fixture_id)           # 即时赔率（向后兼容）
opening = get_opening_odds(fixture_id)   # 初盘赔率

# --- 大小球 ---
from footy.data.ou_data import fetch_ou, fetch_ou_batch
ou = fetch_ou(fixture_id)               # MatchOU 对象
batch = fetch_ou_batch(["id1", "id2"])  # 批量

# --- 必发 ---
from footy.data.bifax import BifaxVerifier, quick_verify
result = quick_verify(bifax_data_dict)  # BifaxVerification 对象
# result.verdict → "⭐⭐⭐⭐ 必发看好"
# result.total_score → +4
# result.steps → [StepResult, ...]

# --- 编排器 ---
from footy.analysis.orchestrator import run_full_pipeline
data = run_full_pipeline("队A vs 队B", "队A", "队B", fixture_id)
```

---

## 四、数据源

| 来源 | URL 格式 | 内容 | 编码 |
|------|---------|------|------|
| 500.com 欧赔 | `/fenxi/ouzhi-{id}.shtml` | 16家初盘+即时欧赔 | gb2312 |
| 500.com 大小球 | `/fenxi/daxiao-{id}.shtml` | 10家初盘+即时O/U | gb2312 |
| 500.com 亚盘 | `/fenxi/yazhi-{id}.shtml` | 亚盘数据 | gb2312 |
| nowscore 赔率 | `/odds/match/{id}.htm` | 欧赔+亚盘+O/U (JS渲染) | utf-8 |
| nowscore JS | `/analysisJs/data{id}.js` | 结构化赔率数据 | utf-8 |
| okooo 联赛 | `/soccer/league/{id}/` | 联赛赔率 | gb2312 |
| okooo 必发 | `/soccer/match/{id}/exchanges/` | 必发交易所 (JS渲染) | gb2312 |

---

## 五、关键决策记录

### 5.1 CID=1 是 竞彩官方（86% 返奖率），不是 10Bet
- **文件**: `wubai.py` CID_NAMES
- **影响**: 竞彩给高赔率 = 反常信号（保守公司竟敢高赔）
- **日期**: 2026-06-25

### 5.2 凯利默认 25%（非 50% 非 100%）
- **文件**: `value.py`
- **原因**: Full Kelly = 100% 破产风险。学术共识 25%
- **日期**: 2026-06-25

### 5.3 初盘 = 庄家真心话
- **文件**: `opening_deviation.py`
- **逻辑**: 初盘浅开 > 0.5 球 = 冷门预警（韩国同款信号）
- **原因**: 初盘是庄家开盘时的真实判断，后续变动是市场博弈

### 5.4 Steam 方向定义
- 赔率下降 = 资金涌入（🟢 市场信心增强）
- 赔率上升 = 市场冷却（🔴 市场信心下降）
- 海啸级: > 0.30, 强: > 0.10, 中: > 0.05, 弱: < 0.05

### 5.5 500.com 页面结构
- 欧赔页: 每个公司行有 1 个内表，2 行（初盘/即时），URL 参数只含初盘
- O/U 页: 每个公司行有 2 个内表（初盘表/即时表），各 1 行
- 行 class 交替: `tr1` / `tr2`
- 解析需深度追踪，防嵌套 `<tr>` 误匹配

### 5.6 必发四步验证
- Step 1: 成交量方向（成交占比 vs 隐含概率）
- Step 2: 交易所 vs 传统庄家背离
- Step 3: 庄家盈亏（负盈亏 = 庄家最怕的方向）
- Step 4: 凯利指数（> 1.05 看好，< 0.85 不看好）
- 综合评分 -8 到 +8，自动生成 ⭐ 评级

---

## 六、以前踩过的坑

| 坑 | 教训 |
|----|------|
| Steam 方向看反 | 必须 cross-verify nowscore 初盘 vs 收盘数据 |
| 德国 Steam "稳定" 实际 -0.15 | 30 家公司统一降赔 = 涌入，不是稳定 |
| 荷兰 Steam "稳定" 实际 -0.43 | 100% 公司降赔 = 海啸级涌入 |
| 巴拉圭 Steam "稳定" 实际 +0.60 | 是冷却不是稳定 |
| 美国 Steam "稳定" 实际 -0.60 | 是涌入不是稳定 |
| CID=1 当成 10Bet | 实际是 竞彩官方 (86% 返奖率) |
| Kelly Full Kelly | 默认 100% = 破产，改为 25% |
| 日本/巴拉圭 O/U 无数据 | 追加拉取直到数据到齐 |
| Checklist 未强制执行 | 加了 orchestrator.py 和 assert_ready() |
| 上下文爆了 (1,048,565 tokens) | 用 ampan_analyze.py CLI 减少 token 消耗 |

---

## 七、上下文管理策略

### 对话爆了怎么办
1. 回复 "继续" 或 "在么" → 自动压缩继续
2. 用 CLI: `python scripts/ampan_analyze.py <id>` → 输出简洁，不占 token
3. 下次开新对话: 先读本说明书，所有关键信息都在

### 减少 token 消耗
- ❌ 不要在对话里 `cat` 长文件
- ❌ 不要全文打印 16 家公司赔率
- ✅ 用 CLI 跑分析，只看摘要输出
- ✅ 关键代码改完后，跑 `pytest` 验证，不需要人工 review 每行

---

## 八、测试

```bash
cd footy-edge
python -m pytest tests/ -v        # 22 个测试
# 覆盖: 凯利、赔率信号、泊松模型、去水、EV 计算
```

---

## 九、待办事项

- [ ] 必发数据自动采集（目前需 WebFetch okooo 页面，JS 渲染）
- [ ] 亚盘数据自动采集（500.com yazhi 页面）
- [ ] 泊松模型接入 orchestrator（自动填 checklist 28）
- [ ] EV/Edge 自动计算（自动填 checklist 29）
- [ ] 伤停/阵容自动采集
- [ ] ClawHub 发布 (账号 wht0202, 14天等待期至 2026-07-09)

---

---

## 十、错误记录

详见 [LEARNED_MISTAKES.md](LEARNED_MISTAKES.md)。每次新对话必须读。

核心 8 条：
1. O/U 页 Table0=即时(有箭头), Table1=初盘(无箭头)
2. 水位比盘口重要，矛盾时以水位为准
3. 升盘+升水=诱盘，降盘+降水=诱盘
4. 亚盘上盘=让球方(强队)，不是看正负号
5. Pinnacle 反向 = 重大警报
6. 别爬 500.com 历史数据，用 football-data.co.uk
7. 新规则先回测再应用
8. 平局+下盘不矛盾

**最后更新**: 2026-06-26
**系统状态**: 核心管线完整，22 测试全过，Gate 拦截生效
