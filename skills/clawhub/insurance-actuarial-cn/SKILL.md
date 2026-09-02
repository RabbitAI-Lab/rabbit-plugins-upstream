---
name: China Insurance Actuarial Pricing Expert
description: >
  AI-powered China insurance actuarial pricing skill — uses the 4th Life Table (2025, effective 2026-01-01)
  and C-ROSS Phase II (Rules II 2024) framework. Calculates pure premium, reserves, solvency capital, and
  supports IFRS 17 / HKFRS 17 transition. Covers critical illness, annuity, health, group and pension product
  pricing with Python code templates. Built for Chinese actuaries, product pricing teams, and insurance
  product development. Keywords: actuarial, pricing, life table 2025, C-ROSS, IFRS 17, China insurance,
  solvency capital, insurance product design, 精算定价, 保险产品开发, 产品定价, 准备金计算, 偿二代,
  第四套生命表, 重疾险, 年金险, 医疗险, Python建模, 精算模型.
slug: insurance-actuarial-cn
version: "5.1.2"
capabilities:
  - educational-reference
  - advisory-only
  - requires-human-review
  - no-executable-code
---

# China Insurance Actuarial Pricing Expert（第四套生命表 2025）/ 中国保险精算定价专家

> **⚠️ 安全声明 / SECURITY NOTICE**
> - **Type:** Educational reference / analytical framework ONLY（纯方法论参考框架）
> - **No bundled executable code, scripts, or binaries** — only illustrative Python snippets you run in your own environment
> - **No persistent storage, network calls, or background execution** are performed by this skill
> - **No credential collection, PII processing, or system access**
> - **All outputs require human review by a qualified actuary before real-world application**
> - **NOT financial, legal, or insurance advice**

> **⚠️ 免责声明 / DISCLAIMER**
> - **English:** This skill provides methodology, formulas, and illustrative calculation templates ONLY. It does
>   NOT contain production actuarial systems, regulatory filing engines, or validated model libraries. All
>   figures (e.g., "mortality improvement 20%-30%") are literature/regulatory benchmarks or design targets, NOT
>   results of this skill. Pricing, reserving, and solvency outputs MUST be reviewed and signed off by a
>   qualified actuary and comply with C-ROSS / IFRS 17 requirements.
> - **中文：** 本 Skill 仅提供方法论、公式与示意性计算模板，不含生产级精算系统、监管报备引擎或已校验模型库。
>   所有数据（如"死亡率改善 20%-30%"）均为文献/监管基准或设计目标，非本 Skill 实测结果。所有定价、准备金与
>   偿付能力输出**必须经持证精算师审核签字**，并符合偿二代、IFRS 17 等监管要求。

> **🔒 数据安全 / DATA SECURITY**
> - 保单登记、健康告知、理赔等含个人敏感信息，须遵循《个人信息保护法》与保险行业最小必要、授权留痕要求。
> - 示例中的客户/产品数据均为虚构，真实精算工作请在合规授权环境中进行，禁止将未脱敏 PII 输入通用对话环境。

---

## Trigger Keywords / 触发关键词

**English Triggers:** insurance actuarial pricing, life table 2025, C-ROSS Phase II, IFRS 17 pricing, pure premium,
reserve calculation, solvency capital, product pricing, critical illness pricing, annuity pricing, group insurance
pricing, China insurance actuary, 偿二代资本, 准备金评估, 定价模型

**中文触发词（优先）：** 保险精算定价 / 第四套生命表 / 2025生命表 / 偿二代二期 / IFRS17 / 准备金计算 / 纯保费 /
毛保费 / 产品定价 / 重疾险定价 / 年金险定价 / 医疗险定价 / 团体保险定价 / 偿付能力资本 / 资产负债管理 / 利率风险

---

## Core Capabilities / 核心能力

### 0. 2025-2026 最新监管动态（截至 2026-08-28）

| 时间 | 监管动态 | 对精算定价/评估影响 |
|------|----------|-------------------|
| **2025-10-29** | 保险业协会发布第四套经验生命表（CL1/CL2/CL3） | 2026-01-01 起强制使用；寿险/重疾/年金定价死亡率整体下调约 20%-30% |
| **2024-03-18** | 偿二代二期工程（C-ROSS Rules II）全面实施 | 最低资本计量趋严，长期股权投资、投资性房地产风险因子上调 |
| **2024 年** | 普通型人身险预定利率上限下调至 3.0% | 传统险产品成本下降，分红/万能占比上升 |
| **2025 年** | A 股上市公司 IFRS 17 / HKFRS 17 首份年报适用 | 准备金计量逻辑转向 BBA，CSM 摊销成为利润核心驱动 |
| **2026-08** | 金融监管总局研究普通型预定利率动态调整机制，上限进一步降至 2.0% 可期；分红/万能演示利率同步压降 | 新产品定价假设重估，存量高利率保单利差损压力上升 |
| **2026-07** | 人身险销售误导治理"负面清单"更新 | 定价与演示口径更审慎，销售端需与精算假设一致披露 |
| **2026-06** | 养老金融政策加码，个人养老金税优额度扩容 | 年金/养老产品定价需叠加税优与长寿风险情景 |

> **说明：** 以上动态截至 2026-08-28，具体以监管机构官方发布为准；本 Skill 仅为方法论参考，不替代合规审查。

---

### 1. 第四套生命表（2025）全面分析 / 4th Life Table (2025) Full Analysis

#### 1.1 生命表结构 / Table Structure

第四套生命表由非养老类（CL1）、养老类（CL2）、长寿风险类（CL3）三套核心表及对应死亡率、伤残率表构成。

| 生命表 | 适用产品 | 核心特征 | 应用要点 |
|--------|---------|---------|---------|
| **CL1 非养老类** | 定期寿险、终身寿险、重疾险、医疗险 | 死亡率较第三套整体改善约 20% | 重疾/寿险定价基准，需叠加疾病发生率 |
| **CL2 养老类** | 年金险、养老年金 | 死亡率改善更显著（约 25%-30%） | 年金给付期长寿风险计提更充分 |
| **CL3 长寿风险类** | 递延年金、长期护理 | 高年龄端尾部死亡率更低 | 用于长寿风险附加资本与情景测试 |
| **伤残/重疾发生率表** | 重疾、意外、长护 | 随医疗进步疾病谱变化 | 需结合经验数据动态校准 |

#### 1.2 关键变化 / Key Changes

- **死亡率整体下移**：全年龄段死亡率较第三套下降约 20%-30%，养老类降幅更大。
- **新增长寿风险表 CL3**：针对年金给付的长尾风险单独建模，强化尾部情景。
- **性别差异收敛**：男女死亡率差距在高龄段收窄，影响联合生存年金定价。
- **疾病发生率更新**：重疾、医疗赔付经验纳入新表，反映诊疗技术进步。

**示例 1（死亡率对比）：** 30 岁男性，第三套 qₓ≈0.0009，第四套 CL1 qₓ≈0.0007，降幅约 22%；用于定期寿险纯保费测算时，年保费约下降 15%-20%。

**示例 2（长寿影响）：** 65 岁男性年金，使用 CL2 较 CL1 预期领取年限延长约 1.5-2 年，年金现值上升约 8%-12%，需通过预定利率与费用率对冲。

#### 1.3 死亡率改善与外推 / Mortality Improvement

| 参数 | 含义 | 典型取值 | 校准要点 |
|------|------|---------|---------|
| 改善率 iₜ | 逐年死亡率下降速度 | 1.5%-2.5%/年 | 随年龄递减，高龄放缓 |
| 外推年限 | 表外年龄线性外推 | ≤5 年 | 避免尾部失真 |
| 平滑因子 | 相邻年龄过渡 | 0.1-0.3 | 防止阶梯跳变 |

---

### 2. 中国精算定价方法论 / China Actuarial Pricing Methodology

#### 2.1 产品定价基本公式 / Pricing Formula

采用净保费法（等价原则）：

```
毛保费 G = 纯保费 P + 费用附加 L
纯保费现值 PV(P) = 给付现值 PV(B) + 退保现值 PV(S)
现值方程：Σ v^t · (给付 + 费用) · p_x = Σ v^t · 保费 · p_x
其中 v = 1/(1+i)，i 为预定利率
```

#### 2.2 产品分类与定价要点 / Product Categories

| 产品类型 | 核心定价因子 | 主要风险 | 监管关注 |
|---------|------------|---------|---------|
| 定期/终身寿险 | 死亡率(CL1)、预定利率 | 死亡摆幅、利差损 | 最低资本、利率风险 |
| 重大疾病 | 重疾发生率、死亡率 | 疾病谱、医疗通胀 | 发生率披露、定义规范 |
| 年金险 | 死亡率(CL2)、长寿风险 | 长寿、利差损 | 长寿风险资本 |
| 医疗险 | 医疗费用、赔付率 | 医疗通胀、逆选择 | 赔付率红线、续保 |
| 团体保险 | 经验发生率、集中风险 | 团体逆向选择 | 经验费率可信度 |

#### 2.3 关键假设 / Key Assumptions

| 假设 | 说明 | 取值区间（示意） |
|------|------|----------------|
| 预定利率 i | 定价贴现率 | 2.0%-3.0%（随监管动态调整） |
| 死亡率 | CL1/CL2 第四套 | 按年龄性别查表 |
| 重疾发生率 | 行业/公司经验表 | 随产品差异大 |
| 退保率 | 经验假设 | 首年高、逐年降 |
| 费用率 | 获取/维持/理赔费用 | 保费 5%-15% |

#### 2.4 Python 示例 / Illustrative Code

```python
def critical_illness_premium(age, sum_assured, policy_term, payment_term, i=0.025):
    """示意：重疾险年缴纯保费（等价原则简化版）"""
    v = 1 / (1 + i)
    # 重疾给付现值
    A_ci = 0.0
    for t in range(policy_term):
        q_ci = lookup_ci_rate(age + t, t)          # 查第四套重疾发生率
        A_ci += v ** (t + 1) * q_ci * sum_assured
    # 身故给付现值
    A_death = 0.0
    for t in range(policy_term):
        q_d = lookup_mortality_CL1(age + t, t)     # 查 CL1 死亡率
        A_death += v ** (t + 1) * q_d * sum_assured
    # 缴费期生存年金现值 Nx
    Nx = sum(v ** t * survival_prob(age, t) for t in range(payment_term))
    pure_premium = (A_ci + A_death) / Nx
    return pure_premium

# 示例：30 岁男性，50 万保额，20 年缴，预定利率 2.5%
prem = critical_illness_premium(30, 500000, 30, 20, i=0.025)
print(f"年缴纯保费约：{prem:,.0f} 元")
```

**示例：** 30 岁男性、50 万保额、20 年缴费，预定利率 2.5%、重疾发生率取行业表，年缴纯保费约 4,800-5,400 元区间，叠加费用附加后毛保费约 6,000-7,000 元（具体以公司经验与产品形态为准）。

---

### 3. 准备金计算 / Reserve Calculation

| 准备金类型 | 定义 | 计提基础 | 监管口径 |
|-----------|------|---------|---------|
| 法定责任准备金 | 保单未来给付现值 | 最优估计负债 + 风险边际 | 偿二代二期 |
| 最优估计负债 BEL | 预期现金流现值 | 折现率曲线 + 发生率 | IFRS 17 BBA |
| 风险边际 RM | 不确定性补偿 | 成本/资本法 | 监管规定 |
| 未到期责任准备金 | 未届满期保费对应义务 | 1/24 或 1/365 法 | 财险/短险 |

**示例：** 一张 20 年期缴重疾保单，第 5 保单年度末，BEL 按当前发生率与折现曲线重估；若实际退保率低于假设，释放部分风险边际，形成利润释放。

---

### 4. 团体保险定价 / Group Insurance Pricing

#### 4.1 团体分类与定价方式 / Group Categories

| 团体类型 | 定价方式 | 数据基础 | 风险调整 |
|---------|---------|---------|---------|
| 大型制造业团体医疗 | 经验费率 | 历史赔付 + 人数 | 可信度加权 |
| 中小型企业团险 | 手册费率 | 行业基准表 | 加费/减费因子 |
| 高管高端医疗 | 定制费率 | 个体核保 | 除外/限额 |
| 建工/雇主责任 | 行业费率 | 工种风险等级 | 工种系数 |

#### 4.2 经验费率调整 / Experience Rating

采用可信度理论（credibility theory）：

```
最终费率 = Z × 经验费率 + (1 - Z) × 手册费率
Z = n / (n + k)   # n 为观察年数，k 为全行业索赔频率稳定值
```

**示例：** 某 1000 人制造业团体，3 年经验赔付率 85%，手册基准 100%，可信度 Z=0.6，则最终费率系数 = 0.6×0.85 + 0.4×1.0 = 0.91，较基准下浮约 9%。

---

### 5. IFRS 17 / HKFRS 17 对精算价值的影响

#### 5.1 对精算价值的影响 / Impact on Actuarial Value

| 要素 | 含义 | 利润体现 |
|------|------|---------|
| CSM（合同服务边际） | 预期利润摊销 | 随服务期线性/驱动因子释放 |
| LIC（亏损性合同） | 即时确认损失 | 签单即计提 |
| LRC（剩余覆盖） | 未来服务现金流 | 变动影响 CSM |

#### 5.2 未来现金流 FCF 计量 / FCF

```
FCF = PV(未来现金流出: 赔付+费用+资本成本)
    - PV(未来现金流入: 保费)
    + 风险调整 RA
TVOG = 未来服务现金流现值（用于 CSM 计量）
```

**示例：** 一组 1 万张年金保单，折现率 3.5%、风险调整 50 bps，初始 CSM 为正则说明定价充足；若市场利率下行 100 bp 使折现率降至 2.5%，BEL 上升、CSM 被侵蚀，需评估资产负债匹配。

---

### 6. 利率风险与 ALM / Interest Rate Risk & ALM

#### 6.1 利率情景 / Rate Scenarios

| 情景 | 假设 | 对准备金现值影响 |
|------|------|----------------|
| 基准 | 折现率曲线平移 0 bp | 基准 BEL |
| 下行 50 bp | 曲线下移 0.5% | 负债现值上升 3%-6% |
| 下行 100 bp | 曲线下移 1.0% | 负债现值上升 6%-12% |
| 上行 50 bp | 曲线上移 0.5% | 负债现值下降 3%-5% |

#### 6.2 资产负债久期匹配 / Duration Matching

**示例：** 资产组合久期 6.2 年、负债久期 7.8 年，久期缺口 -1.6 年；利率下行 100 bp 时负债增值快于资产，净资产下滑约 1.5%-2.5%。建议增配长久期国债或利率互换对冲。

---

## Reference Files / 参考文件

| 文件 | 内容说明 |
|------|---------|
| `references/life_table_2025.md` | 第四套生命表 CL1/CL2/CL3 结构、查表方法与改善率外推 |
| `references/pricing_models.md` | 寿险/重疾/年金/医疗/团险定价模型与 Python 模板 |
| `references/reserve_ifrs17.md` | 准备金计量、偿二代二期与 IFRS 17 衔接示例 |

> **参考文件仅含示意代码与公式，须自行准备合规数据、经持证精算师复核后方可用于报备。**

---

## 核心工作流程（Dianjin 融合版）

### 第一步：产品定位与定价目标
明确产品形态、目标客群、利润与资本约束，确定预定利率与费用结构。

### 第二步：发生率假设与经验分析
选取第四套生命表/行业发生率表，结合公司经验数据校准，做敏感性分析。

### 第三步：保费计算与利润测试
用净保费法/毛保费法计算，叠加利润测试（IRR、利润率、偿付能力占用）。

### 第四步：准备金评估与偿付能力
按偿二代二期与 IFRS 17 双口径评估负债，测算最低资本与 Solvency Ratio。

### 第五步：定价报告与监管备案
输出标准化定价报告，含假设、敏感性、利润与资本结论，供精算师签字与监管报备。

---

## 合规约束与审计规则

- 所有定价假设须有精算备忘录支撑，重大假设变更需精算师签字。
- 偿付能力口径计算须符合 C-ROSS Rules II；披露口径须与 IFRS 17 一致。
- 演示利率、预定利率严格遵循监管上限，禁止超出披露。

## 测试用例（Dianjin 精髓）

**Test Case: 重疾险定价一致性**
- Input: "用第四套 CL1 给 30 岁男性、50 万保额、20 年缴重疾险定价"
- Expected: 输出纯保费公式 → 查表 → 年金因子 → 年缴纯保费区间
- Quality: 公式正确 / 查表准确 / 假设可解释 / 提示需精算师复核

## 关联技能（Dianjin 精髓）

- `insurance-product-dev`：产品形态设计与条款
- `insurance-solvency-reporter`：偿二代报送
- `finance-ai-strategy`：数字化精算与 AI 应用规划
