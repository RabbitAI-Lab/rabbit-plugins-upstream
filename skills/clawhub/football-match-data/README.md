# footy-edge — 足球价值投注分析 CLI

**五大联赛概率预测 · 盘口信号引擎 · 策略回测 · 资金管理**

⚠️ **诚实声明**
- 这是一个**研究/分析工具**，不内置自动下注，不内置违规爬虫。
- 在真实足球博彩市场，**80% 胜率不现实**。顶尖公开模型的长期胜率约 53-58%，靠正期望（+EV）盈利。
- 本系统用 **RPS/ROI/CLV** 等专业指标替代单一胜率，用回测数据说话。
- 历史回测不保证未来（过拟合风险，需样本外验证）。
- 博彩有法律风险——本工具仅供研究学习，**合规责任用户自负**。

---

## 快速开始

```bash
# 安装
cd footy-edge
pip install -e .

# 拉取历史数据（英超 2018-2024，约 2280 场比赛）
footy fetch --league E0

# 拟合 Dixon-Coles 模型
footy fit --league E0 --model dixon-coles

# 预测一场比赛
footy predict "Arsenal vs Chelsea"
# 输出: 1X2 概率 + Over/Under 2.5 + 期望进球

# 查看最近比赛
footy matches --league E0

# 回测（验证模型真实表现）
footy backtest --league E0 --model dixon-coles
```

## 命令总览

| 命令 | 功能 |
|------|------|
| `footy fetch` | 从 football-data.co.uk 下载五大联赛历史 CSV → 入库 |
| `footy fit` | 拟合预测模型（Poisson/Dixon-Coles），保存参数 |
| `footy predict` | 预测单场 1X2 + O/U 2.5 概率 |
| `footy value` | 扫描最近比赛，输出有价值下注（edge/EV/凯利） |
| `footy backtest` | Walk-forward 回测，产出真实 ROI/RPS/胜率 |
| `footy analyze` | 盘口信号分析（凯利方差/离散度/冷门预警） |
| `footy matches` | 查询数据库中的比赛 |
| `footy record` | 下注记录与资金曲线追踪 |

## 模型

### Dixon-Coles（主模型）
双变量 Poisson 模型（1997年论文），足球预测金标准：
- 主/客队进球 ~ Poisson(λ)，λ 由攻防参数 + 主场优势决定
- **ρ 参数**修正低比分相关性（0-0/1-0/0-1/1-1）
- **时间衰减权重**：越近比赛越重要（默认半衰期 180 天）
- 用 L-BFGS-B 最大似然拟合

### Poisson（对照基线）
无 ρ 修正、无时间衰减的纯泊松，用于消融对比。

### 真实表现（英超 2020-2024，Pinnacle 收盘结算）

| 指标 | 数值 | 解读 |
|------|------|------|
| RPS（瞎猜 33/33/33） | 0.2400 | 基线 |
| RPS（Dixon-Coles） | 0.2084 | **比瞎猜准 13%** — 模型有真实预测力 |
| RPS（Pinnacle 盘口） | 0.1965 | 市场比模型再准 6% |
| 整体 ROI | -3.93% | 对最锋利收盘盘亏损（符合学术界共识） |

**核心结论**：公开统计模型无法系统性战胜 Pinnacle 收盘盘口。高 edge（>5%）的值投才是正道。

## 盘口信号引擎

`footy analyze` 运行四大信号维度：

1. **凯利方差** — 各家博彩公司的凯利指数离散度。越小 = 越一致
2. **赔率离散度** — 隐含概率的标准差。高离散+正偏态 = 冷门预警
3. **亚盘口诀** — 升盘降水/降盘升水 等经典看盘法则（需开盘/收盘数据）
4. **市场方向** — 综合判定

输出为信号标签（如 `[high_consensus]` `[cold upset risk elevated]`），供综合判断。

## 数据源

| 来源 | 用途 | 费用 |
|------|------|------|
| football-data.co.uk | 历史赛果 + 收盘赔率（主源） | 免费 |
| The Odds API | 实时赛前赔率（可选） | 500次/月免费 |

中文数据源（澳客/500万/竞彩网等）通过 `BaseDataAdapter` 接口接入——系统**不内置违规爬虫**。

## 资金管理

- 默认 **半凯利**（50% Kelly）——降低方差，防破产
- `footy value` 显示每个推荐的 full-Kelly 下注单位
- `footy record` 追踪实盘资金曲线

## 技术栈

Python 3.10+ · scipy（拟合）· pandas · numpy · click（CLI）· rich（输出）· SQLite

## 项目结构

```
footy-edge/
├── src/footy/
│   ├── cli.py              # 命令行入口
│   ├── config.py           # 配置与路径
│   ├── data/               # 数据层
│   │   ├── schema.py       # 统一 Match schema
│   │   ├── footballdata.py # CSV 适配器（主源）
│   │   ├── oddsapi.py      # The Odds API（实时）
│   │   ├── base.py         # 中文源接入协议
│   │   └── store.py        # SQLite 存储
│   ├── models/             # 预测模型
│   │   ├── poisson.py      # 纯 Poisson
│   │   └── dixon_coles.py  # Dixon-Coles（ρ+时间衰减）
│   ├── analysis/           # 分析层
│   │   ├── value.py        # 去水/Edge/EV/凯利
│   │   └── odds_signals.py # 盘口信号引擎
│   ├── backtest/           # 回测
│   │   ├── engine.py       # Walk-forward 引擎
│   │   └── metrics.py      # 指标计算
│   └── ledger/             # 下注记录
│       └── __init__.py
├── tests/                  # 22 个单元测试
├── data/                   # 本地数据库 + 下载的 CSV
└── pyproject.toml
```

## License

MIT — 仅供研究与学习。使用本工具进行真实博彩请遵守当地法律。
