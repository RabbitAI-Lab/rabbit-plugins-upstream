---
name: 防爆阀设计选型
description: |
  防爆阀（呼吸阀）设计选型工具。基于 Pack 箱体参数（体积、温度范围、海拔范围、时间）
  计算所需透气量，并根据压差-透气量特性曲线推荐满足安全约束的防爆阀规格。
  核心约束：防爆阀排气速率必须不低于单个电芯产气速率。
  触发场景：防爆阀选型、呼吸阀选型、Pack 箱体透气量计算、电池包压力平衡设计、
  温度变化透气量估算、海拔变化透气量估算、电池包排气设计、explosion-proof valve sizing。
agent_created: true
---

# 防爆阀设计选型

## Overview

提供温度变化和海拔变化两种工况下的 Pack 箱体透气量计算，结合阀门压差-流量特性曲线
完成防爆阀规格选型。核心安全约束：**阀门排气速率 ≥ 电芯产气速率**。

## 工作流程

### Step 1: 收集输入参数

从用户处获取或确认以下参数：

| 参数 | 符号 | 单位 | 必填 | 说明 |
|------|------|------|------|------|
| 箱体体积 | V0 | L | 是 | Pack 箱体内部净容积 |
| 温度范围 | T0→T1 | ℃ | 是 | 如 55→20 或 -20→55 |
| 温度变化时间 | t_temp | min | 是 | 温度从 T0 到 T1 所需时间 |
| 海拔/气压范围 | P0→P1 | kPa | 条件 | 可用海拔(m)替代，自动转换 |
| 海拔变化时间 | t_alt | min | 条件 | 若涉及海拔变化则必填 |
| 电芯产气速率 | G_cell | L/min | **是** | 关键安全约束，不可遗漏 |
| 额定压差 | P_rated | kPa | 否 | 默认 7.0 kPa |
| 安全系数 | SF | - | 否 | 默认 1.5 |

用户可能以自然语言描述，将定性描述转为定量参数：
- "快充升温" → 约 2~5 ℃/min
- "极限高温" → 55~60 ℃
- "高原运输" → 海拔 3000~4000m (气压 ~70→61 kPa)
- "标准集装箱" → 根据长宽高计算 V0

### Step 2: 执行计算

调用计算脚本 `scripts/breathing_calc.py`：

```bash
python scripts/breathing_calc.py '{"volume_L":20,...}'
```

JSON 参数格式（所有键为 string）：

```json
{
  "volume_L": 20,
  "T0_C": 55,
  "T1_C": 20,
  "temp_time_min": 60,
  "P0_kPa": 101.325,
  "P1_kPa": 89.87,
  "alt_time_min": 60,
  "cell_gas_rate_L_per_min": 0.5,
  "rated_pressure_kPa": 7.0,
  "safety_margin": 1.5
}
```

若用户提供了海拔而非气压值，使用 Python 内置函数转换：

```python
from scripts.breathing_calc import altitude_to_pressure
p0 = altitude_to_pressure(altitude0_m)
p1 = altitude_to_pressure(altitude1_m)
```

脚本输出包含：
- `temperature_cooling` / `temperature_heating`: 降温/升温透气量、压差等
- `altitude_ascent` / `altitude_descent`: 海拔上升/下降透气量
- `valve_selection`: 各压差点评估 + 推荐结论

### Step 3: 解析结果并给出选型建议

从脚本输出的 `valve_selection` 中：

1. **推荐阀门**：读取 `recommendation` 字段
2. **检查 eligibility**：`eligible=true` 的候选点满足所有约束
3. **安全系数**：`safety_factor ≥ safety_margin` 为合格

输出给用户的建议应包含：
- 需求透气量（L/min @额定压差）
- 推荐阀门工作压差与对应透气量
- 安全系数
- 不满足时的对策（多阀并联 / 增大规格 / 优化设计）

### Step 4 (可选): 详细计算过程展示

当用户需要理解计算过程时，加载 `references/formulas.md` 获取完整公式推导，
并结合脚本输出的中间值（ΔV、Δp、压差变化率等）向用户解释。

## 计算原理速查 (v2 — 压差驱动模型)

温度变化和海拔变化统一为「压差驱动」模型：透气速率 ∝ 压差变化率。

核心参数 **透气系数 K** = V0 / P_ref (L/min per kPa/min)，表示每 1 kPa/min 压差变化率需要多少 L/min 的透气速率。

### 温度变化 (恒外压)

```
dT/dt = (T1 - T0) / t                            ← 温度变化率 (℃/min)
dP/dt = P_atm × dT/dt / T0(K)                    ← 密闭时压差变化率 (kPa/min)
K     = V0 / P_atm                               ← 透气系数 (L/min per kPa/min)
Φ     = K × dP/dt                                ← 实际透气速率 (L/min)
Φ_rated = K × P_rated                            ← 标化至额定压差
       = V0 / P_atm × P_rated
```

> 标化结果 Φ_rated 与温变速率无关，仅取决于 V0、当地大气压和额定压差。

### 海拔变化 (恒温)

```
dP_ext/dt = |P1 - P0| / t                        ← 外压变化率 (kPa/min)
K         = V0 / min(P0, P1)                     ← 透气系数, 取较低气压为参考
Φ_rated   = K × P_rated
          = V0 / P_ref × P_rated
```

> P_ref 取 P0 和 P1 中较小值，保守估算最大透气需求。

### 选型约束

```
Φ_valve ≥ max(Φ_breathing, Φ_cell_gas)
安全系数 = Φ_valve / Φ_design ≥ 1.5
```

### 中间过程量说明

脚本输出新增以下中间字段便于验证：

| 字段 | 含义 | 温度 | 海拔 |
|------|------|------|------|
| `temp_change_rate_C_per_min` | 温度变化率 dT/dt | ✅ | — |
| `pressure_change_rate_kPa_per_min` | 压差变化率 | dP/dt (密闭) | \|dP_ext/dt\| |
| `flow_coefficient_L_per_kPa` | 透气系数 K | V0/P_atm | V0/P_ref |

## 资源文件

| 文件 | 用途 |
|------|------|
| `scripts/breathing_calc.py` | 核心计算脚本，包含所有计算函数和 CLI 入口 |
| `references/formulas.md` | 公式推导详解、海拔-气压对照表、安全约束说明 |
| `references/valve_data.md` | 阀门特性曲线数据、典型工况参数、决策流程图 |

## 常见场景示例

### 场景 1: 仅温度变化

用户: "Pack 箱 30L，温度从 55℃ 降到 20℃ 需要 30 分钟，电芯产气速率 1 L/min，选什么防爆阀？"

→ 调用脚本，P0=P1=101.325（无海拔变化），alt_time_min 设为任意值即可（结果取 max）。

### 场景 2: 温度 + 海拔

用户: "20L 电池包，快充时 30 分钟从 20℃ 升到 55℃，运输最高海拔 4000m，电芯产气 0.8 L/min"

→ 计算温度升温透气量 + 海拔上升透气量（~61.64 kPa），取最大值选型。

### 场景 3: 仅电芯产气约束

用户: "已知电芯产气速率 3 L/min，需要多阀并联还是单阀？"

→ 直接以 cell_gas_rate 为 demand，检查单阀是否满足；不满足则建议并联数量 = ceil(demand / 单阀最大流量)。
