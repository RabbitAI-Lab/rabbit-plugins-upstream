---
name: ESG Investment Analysis Assistant
slug: security-esg-investing
description: AI-powered ESG investing analysis assistant — covers ESG rating analysis, green finance screening, carbon footprint assessment, and sustainable investment portfolio construction. Built for ESG analysts, sustainable fund managers, and institutional investors. Keywords: ESG investing, sustainability, green finance, carbon footprint, ESG rating, responsible investing, China ESG, ESG分析, 绿色金融, 可持续发展, 碳足迹, ESG评级, 碳中和, 绿色债券, ESG投资组合, 责任投资, 碳核算, 碳交易.
version: "3.0.2"
---

# ESG Investment Analysis Assistant / ESG投资分析助手

> **English:** AI-powered ESG investing analysis assistant — covers ESG rating comparison, green finance products, carbon accounting, and sustainable portfolio construction. Built for ESG analysts and sustainable investors.
>
> **中文:** ESG投资分析助手——覆盖ESG评级对比、绿色金融产品筛选、碳核算、可持续组合构建。适用：ESG分析师、可持续基金经理、机构投资者。

---


### 证券监管最新动态 [2026-09-12更新]

| 动态类型 | 内容摘要 | 影响范围 | ESG侧应对动作 | 责任岗 | 优先级 |
|---------|---------|---------|-------------|-------|-------|
| 证券监管 | 2026年Q1：ESG信息披露要求扩大至非上市企业 | ESG投资分析框架需更新最新信披要求和绿色金融政策 | 供应链ESG数据采集范围同步扩大 | 研究 | 高 |
| 证券监管 | 绿色金融信贷导向政策升级，ESG投资环境改善 | ESG投资分析框架需更新最新信披要求和绿色金融政策 | 绿色资产识别标准与信贷口径对齐 | 研究 | 中 |
| 证券监管 | 证监会加强ESG相关信披监管，ESG评级标准趋严 | ESG投资分析框架需更新最新信披要求和绿色金融政策 | 评级来源与取数日期须在报告中标注 | 合规 | 高 |
| 可持续披露 | 可持续披露规则推进，披露范围与颗粒度提升 | ESG评级输入数据、组合披露 | 建立披露数据映射表，统一口径 | 研究 | 高 |
| 反漂绿 | 绿色宣传与绿色产品命名合规要求趋严 | 绿色基金命名、宣传物料 | 产品命名与投资范围一致性自查 | 合规 | 高 |
| 碳市场 | 碳市场覆盖行业范围与交易规则持续完善 | 碳成本测算、高碳行业敞口 | 碳价情景纳入估值敏感性 | 研究 | 中 |
| 绿色债券 | 绿色债券募集资金用途与存续期披露要求细化 | 绿债筛选与投后跟踪 | 存续期环境效益跟踪清单化管理 | 研究 | 中 |
| 数据合规 | ESG数据来源与第三方数据使用需合规授权 | 外部评级与数据库采购 | 数据来源授权凭证归档，标注使用范围 | 合规 | 中 |

> **数据截止**: 2026-09-12 | 来源：证监会、生态环境部门公开规则、交易所公开信息
> **声明**: 以上动态供参考，具体以官方最新发布为准

**动态解读示例（四类高频场景）**

- **场景A｜反漂绿自查**：某产品命名为"绿色低碳"但持仓含高碳行业标的 → 命中"命名与投资范围一致性"问题 → 要么调整持仓以匹配命名，要么修改产品名称与宣传口径，并留存自查记录。
- **场景B｜披露口径映射**：评级输入中"碳排放"既有总量又有强度，混用于同一模型 → 命中"口径统一"要求 → 建立披露数据映射表，明确每项指标的来源、单位与报告期。
- **场景C｜碳价情景敏感性**：估值模型未考虑碳成本 → 命中"碳成本纳入测算"要求 → 在敏感性分析中增加碳价上下行情景对高碳标的利润率与估值的影响。
- **场景D｜数据授权**：ESG评级数据采购后用于对外报告但无授权范围说明 → 命中"数据来源合规"要求 → 归档授权凭证并注明可使用的场景，超范围使用需另行申请。

## Industry Pain Points / 行业痛点

| Pain Point / 痛点 | Impact / 影响 | Solution / 本Skill解决方案 | 量化基线指标 / Baseline |
|------------------|-------------|------------------------|----------------------|
| **ESG数据分散** | 评级机构超过10家，标准不统一 | 跨评级对比框架+综合评分 | 覆盖机构 ≥4家，分歧度可量化 |
| **"漂绿"风险** | 虚假绿色宣传导致合规风险 | 实质性分析+数据核实 | 绿色收入占比可核查率 100% |
| **碳核算复杂** | Scope 1/2/3核算专业门槛高 | 分级碳核算模板+简化方法 | Scope 1/2 数据覆盖率 100% |
| **政策变化快** | 碳市场/ESG披露要求频繁更新 | 实时政策跟踪+合规提醒 | 政策更新响应 ≤5个工作日 |
| **评级分歧** | 同一公司评级差异大，难以决策 | 分歧归因表+一致性检验 | 分歧>2档时须专项说明 |
| **数据不可比** | 不同来源口径不一致 | 口径映射表 | 指标口径一致率 100% |
| **投后跟踪缺失** | 绿债与绿色项目投后无跟踪 | 存续期跟踪清单 | 环境效益跟踪覆盖率 100% |
| **负面事件滞后** | 重大ESG事件未及时反映 | 事件监控与复核机制 | 重大事件响应 ≤3个工作日 |

---

## Trigger Keywords / 触发关键词

**English Triggers:** ESG investing, sustainability, green finance, carbon footprint, ESG rating, responsible investing, ESG analysis, carbon trading, sustainable portfolio, China ESG

**中文触发词（优先）：** ESG投资 / 可持续发展 / 绿色金融 / 碳足迹 / ESG评级 / 责任投资 / ESG分析 / 碳交易 / 可持续组合 / 碳中和 / 碳达峰 / 绿色债券 / ESG披露 / MSCI ESG / 责任投资 / 影响力投资

---

## Core Capabilities / 核心能力

### 1. ESG Rating Analysis / ESG评级分析

```python
class ESGAnalyzer:
    """ESG评级分析"""
    
    RATING_PROVIDERS = {
        "MSCI": {"scale": "CCC-AAA", "weight": {"E": 0.25, "S": 0.25, "G": 0.50}},
        "Sustainalytics": {"scale": "0-100", "weight": {"E": 0.33, "S": 0.33, "G": 0.33}},
        "商道融绿": {"scale": "D-A+", "weight": {"E": 0.30, "S": 0.30, "G": 0.40}},
        "中证ESG": {"scale": "C-AAA", "weight": {"E": 0.20, "S": 0.20, "G": 0.60}},
        "华证ESG": {"scale": "C-AAA", "weight": {"E": 0.25, "S": 0.30, "G": 0.45}},
        "Wind ESG": {"scale": "1-10", "weight": {"E": 0.30, "S": 0.30, "G": 0.40}}
    }
    
    def normalize_rating(self, provider: str, raw_score: float) -> float:
        """标准化评分到0-100"""
        if provider == "MSCI":
            scale = {"CCC": 10, "B": 20, "BB": 35, "BBB": 50, "A": 65, "AA": 80, "AAA": 95}
            return scale.get(raw_score, 50)
        elif provider == "Sustainalytics":
            return 100 - raw_score  # 反转，风险分数→ESG分数
        elif provider == "商道融绿":
            scale = {"D": 20, "C": 40, "B": 60, "B+": 70, "A": 85, "A+": 95}
            return scale.get(raw_score, 50)
        elif provider == "华证ESG":
            scale = {"C": 20, "CC": 30, "CCC": 40, "B": 50, "BB": 60, "BBB": 70,
                     "A": 80, "AA": 90, "AAA": 95}
            return scale.get(raw_score, 50)
        elif provider == "Wind ESG":
            # Wind 为 1-10 分制，线性映射到 0-100
            return float(raw_score) * 10
        return raw_score
    
    def comprehensive_analysis(self, company: str, 
                               ratings: dict) -> dict:
        """综合ESG分析"""
        normalized = {
            provider: self.normalize_rating(provider, score)
            for provider, score in ratings.items()
        }
        
        # 加权综合评分
        weights = [0.30, 0.25, 0.25, 0.20]  # 权重分配
        providers = list(normalized.keys())
        comprehensive = sum(
            normalized[p] * w 
            for p, w in zip(providers, weights)
        )
        
        return {
            "comprehensive_score": round(comprehensive, 1),
            "rating_level": self._score_to_level(comprehensive),
            "individual_ratings": normalized,
            "key_strengths": self._identify_strengths(normalized),
            "key_concerns": self._identify_concerns(normalized),
            "peer_comparison": self._compare_to_peer(company, comprehensive)
        }
    
    def _score_to_level(self, score: float) -> str:
        levels = {
            (90, 100): "AAA - 卓越",
            (80, 90): "AA - 优秀",
            (70, 80): "A - 良好",
            (60, 70): "BBB - 平均偏上",
            (50, 60): "BB - 平均",
            (40, 50): "B - 低于平均",
            (0, 40): "CCC/B - 落后"
        }
        for (low, high), level in levels.items():
            if low <= score <= high:
                return level
        return "未知"
```

**跨评级机构分歧表（分歧本身也是信息）**

| 评级机构 | 原始评级 | 标准化得分 | 与均值偏离 | 可能的解释 |
|---------|---------|-----------|-----------|-----------|
| MSCI | BB | 35.0 | −18.4 | 对治理与信息披露要求较严 |
| Sustainalytics | 38（风险分） | 62.0 | +8.6 | 偏重风险暴露口径 |
| 商道融绿 | B+ | 70.0 | +16.6 | 侧重国内披露实践 |
| 中证ESG | BBB | 70.0 | +16.6 | 治理权重较高 |
| 综合得分 | — | **53.4（BB-平均）** | — | 分歧较大，需专项说明 |

**示例 1｜评级分歧的两种处理方式**

| 分歧程度 | 判定 | 处理方式 | 报告写法 |
|---------|------|---------|---------|
| ≤1档 | 一致 | 直接采用综合得分 | "各机构评级基本一致" |
| 2档 | 中度分歧 | 取中位数并说明 | "评级存在差异，主要源于治理维度权重不同" |
| >2档 | 高度分歧 | 逐一归因，不强行合并 | "评级分歧显著，建议以原始披露数据为准做独立判断" |

**示例 2｜标准化映射的注意事项**

| 问题 | 原因 | 正确做法 |
|------|------|---------|
| Sustainalytics 分数越高越差 | 其分制为"风险分" | 用 100 减后再入表，并注明已反转 |
| MSCI 无 BBB- 等档位 | 档位为离散七级 | 用映射表而非线性插值 |
| 评级更新不同步 | 各机构更新频率不同 | 每项标注评级发布日期，取最近一期 |
| 分母口径不同 | 有的按市值、有的按营收 | 强度类指标须统一分母并标注 |

### 2. Carbon Footprint Analysis / 碳足迹分析

```python
class CarbonAnalyzer:
    """碳足迹核算"""
    
    def calculate_carbon_footprint(self, company_data: dict) -> dict:
        """
        计算碳足迹（Scope 1, 2, 3）
        """
        # Scope 1: 直接排放
        scope1 = (
            company_data.get("fuel_combustion", 0) * 2.02 +  # CO2系数
            company_data.get("vehicle_fleet", 0) * 2.32 +
            company_data.get("fugitive_emissions", 0) * 25  # CH4当量
        )
        
        # Scope 2: 间接排放（电力）
        scope2 = (
            company_data.get("electricity_kwh", 0) * 
            company_data.get("grid_emission_factor", 0.68)  # 中国电网系数
        )
        
        # Scope 3: 价值链排放（简化版）
        scope3 = {
            "上游采购": company_data.get("purchased_goods", 0) * 0.5,
            "运输配送": company_data.get("transportation", 0) * 0.1,
            "员工通勤": company_data.get("employee_commute", 0) * 0.02,
            "产品使用": company_data.get("product_use", 0) * 0.8,
            "报废处理": company_data.get("end_of_life", 0) * 0.05
        }
        
        total_scope3 = sum(scope3.values())
        
        return {
            "scope1_tCO2e": round(scope1, 2),
            "scope2_tCO2e": round(scope2, 2),
            "scope3_tCO2e": round(total_scope3, 2),
            "total_emissions": round(scope1 + scope2 + total_scope3, 2),
            "intensity_metrics": {
                "per_revenue": round((scope1+scope2+total_scope3) / 
                                    max(company_data.get("revenue_yuan", 1), 1) * 1e6, 2),  # tCO2e/百万营收
                "per_employee": round((scope1+scope2+total_scope3) / 
                                      max(company_data.get("employees", 1), 1), 2)  # tCO2e/人
            },
            "scope_breakdown": {
                "Scope 1": round(scope1/(scope1+scope2+total_scope3+0.001)*100, 1),
                "Scope 2": round(scope2/(scope1+scope2+total_scope3+0.001)*100, 1),
                "Scope 3": round(total_scope3/(scope1+scope2+total_scope3+0.001)*100, 1)
            }
        }
```

**示例 1｜碳核算结果解读（先看结构，再看总量）**

| 项目 | 数值 | 占比 | 解读 |
|------|------|------|------|
| Scope 1 直接排放 | 12,400 tCO2e | 12.1% | 主要来自燃料燃烧 |
| Scope 2 间接排放（电力） | 21,800 tCO2e | 21.3% | 可用绿电替换下降 |
| Scope 3 价值链排放 | 68,300 tCO2e | 66.6% | 占比最高，减排难度大 |
| 合计 | 102,500 tCO2e | 100% | — |
| 强度（tCO2e/百万营收） | 42.7 | — | 需与行业对标 |

解读要点：Scope 3 占比超过六成是制造业常态，若报告只强调 Scope 1/2 的减排成绩，容易形成选择性披露；应说明 Scope 3 的核算边界与数据来源可靠度。

**示例 2｜强度指标行业对标**

| 行业 | 强度中位数（tCO2e/百万营收） | 标的A | 标的B | 判断 |
|------|--------------------------|-------|-------|------|
| 建材 | 180 | 165 | 210 | A优于中位数，B偏高 |
| 电子制造 | 45 | 42.7 | 38.5 | 均在合理区间 |
| 电力 | 320 | 290 | 355 | A优于中位数，B偏高 |
| 消费 | 18 | 12 | 9 | 均优于中位数 |

使用要点：强度指标必须限定在同一行业内部比较，跨行业直接比大小没有意义；对标时应注明数据年份与来源。

**示例 3｜数据缺口处理（不要用0填补）**

| 缺口情形 | 错误做法 | 正确做法 |
|---------|---------|---------|
| 无 Scope 3 数据 | 记为0 | 标注"未披露"，并给出行业估算区间 |
| 仅有集团口径 | 直接按营收比例摊分 | 说明摊分假设，标注为估算值 |
| 电网排放因子过期 | 沿用旧系数 | 使用最新公布系数并标注年份 |
| 子公司未纳入合并 | 忽略 | 明示核算边界，说明未纳入部分 |

### 3. Green Bond Analysis / 绿色债券分析

```markdown
## 绿色债券投资分析框架

### 一、绿色债券认定
| 标准 | 中国绿债标准 | 国际标准（GBP） | 核查要点 |
|-----|------------|---------------|---------|
| 募集资金用途 | ≥80%用于绿色项目 | ≥95%用于绿色项目 | 核对投向清单与项目目录 |
| 项目评估 | 需第三方认证 | 需外部评审 | 核查认证机构资质与结论 |
| 信息披露 | 年度+事件披露 | 发行时+续存期披露 | 是否按期披露环境效益 |
| 募集资金管理 | 专户管理、专款专用 | 独立账户管理 | 核查资金流水与用途一致性 |
| 存续期跟踪 | 需跟踪项目进展 | 需持续报告 | 环境效益指标是否可量化 |
| 目录依据 | 依据绿色债券支持项目目录 | 依据GBP四原则 | 版本年份须标注 |

### 二、绿色债券筛选矩阵
- [ ] 是否获得绿色债券认证
- [ ] 第三方认证机构资质
- [ ] 募集资金用途透明度
- [ ] 环境效益量化指标
- [ ] 续存期管理机制

### 三、环境效益量化
```python
def calculate_green_benefits(bond_data: dict) -> dict:
    """计算绿色债券环境效益"""
    green_proceeds = bond_data["total_amount"] * bond_data["green_ratio"]
    
    benefits = {
        "annual_co2_reduction": green_proceeds / 10000 * bond_data["carbon_factor"],  # 吨CO2/年
        "annual_energy_saving": green_proceeds / 10000 * bond_data["energy_factor"],  # 吨标煤/年
        "equivalent_forests": green_proceeds / 10000 * bond_data["forest_factor"]  # 相当于造林面积(公顷)
    }
    
    return benefits
```
```

**绿色债券筛选打分表（把清单变成可比较的分数）**

| 维度 | 权重 | 评分要点 | 分值（1-5） |
|------|------|---------|-----------|
| 认证有效性 | 25% | 是否取得合规第三方认证 | 5 |
| 募集资金投向 | 25% | 绿色项目占比与目录一致性 | 4 |
| 环境效益可量化 | 20% | 是否有明确减排量测算 | 4 |
| 信息披露质量 | 15% | 存续期披露是否及时完整 | 3 |
| 资金管理规范性 | 15% | 专户管理与用途一致性 | 5 |
| **加权得分** | 100% | — | **4.25** |

判定口径：加权得分 ≥4.0 为优质绿债；3.0-4.0 为合格；<3.0 需评估是否存在"漂绿"风险。

**示例｜环境效益测算的手算核对**

- 输入：债券规模 10 亿元，绿色用途占比 100%，碳减排系数 0.42 吨CO2/万元。
- 年减排量 = 100,000 万元 × 0.42 = **42,000 吨CO2/年**。
- 折合造林 ≈ 42,000 / 每公顷年固碳 6 吨 ≈ **7,000 公顷**/年（折算系数须注明来源）。
- 报告写法："据发行文件披露的测算方法，本期债券对应项目预计年减排CO₂约4.2万吨（折算参数来源：发行文件第X页），该数值为预测值，实际以存续期披露为准。"

### 4. ESG Portfolio Construction / ESG组合构建

**三种主流构建方法对比**

| 方法 | 做法 | 优点 | 局限 | 适用投资者 |
|------|------|------|------|-----------|
| 负面排除 | 剔除烟草、博彩、高碳等行业 | 规则清晰、易执行 | 可能牺牲收益、行业集中 | 有明确价值观约束的机构 |
| ESG整合 | 把ESG评分并入选股模型 | 不显著偏离基准 | 依赖评级质量 | 多数公募与保险资金 |
| 主题投资 | 聚焦低碳、清洁能源等主题 | 契合长期趋势、弹性大 | 波动大、主题可能过窄 | 风险偏好较高的资金 |
| 影响力投资 | 以可量化的社会/环境效益为目标 | 效益可衡量 | 流动性较差 | 长期资金、公益属性资金 |

**ESG组合构建检查表**

| 检查项 | 阈值 | 说明 |
|-------|------|------|
| 组合ESG综合得分 | ≥行业基准或基准+5% | 相对基准的改善幅度须可量化 |
| 高碳行业敞口 | ≤基准的80% | 避免名义ESG实则高碳 |
| 单一ESG主题集中度 | ≤25% | 防止主题过度集中 |
| 争议标的剔除 | 100%剔除重大争议标的 | 依据负面事件清单 |
| ESG数据覆盖率 | ≥90% | 覆盖率不足须说明估算方法 |
| 绿色收入占比 | ≥30%（绿色主题产品） | 与产品命名保持一致 |

**示例｜ESG改善的两种口径**

| 口径 | 定义 | 示例结果 | 使用时注意 |
|------|------|---------|-----------|
| 相对改善 | 组合得分高于基准的幅度 | 组合62分，基准55分，改善+7分 | 须说明基准选择 |
| 绝对水平 | 组合的绝对得分档位 | 组合62分（BBB档） | 高分不等于低风险 |
| 加权碳强度 | 组合碳强度相对基准变化 | 较基准低22% | 须说明核算边界 |

---

## Quick Command Templates / 快速指令模板

**跨评级对比：**
```
对[公司名称]做跨机构ESG评级对比：
- 机构与评级：[MSCI X / Sustainalytics X / 商道融绿 X / 中证 X]
- 输出：标准化得分、与均值偏离、分歧归因与结论
```

**碳核算：**
```
按 Scope 1/2/3 为[公司名称]做碳核算：
- 输入：燃料消耗/外购电量/采购金额/运输量
- 输出：分项排放量、强度指标、结构占比与数据缺口说明
```

**绿色债券筛选：**
```
按认证有效性、募集资金投向、环境效益、信息披露、资金管理五个维度，
对[债券名称]做绿债打分并给出是否认定及漂绿风险提示。
```

**ESG组合构建：**
```
用[负面排除/ESG整合/主题投资]方法构建组合，
输出组合ESG得分、高碳敞口、主题集中度与数据覆盖率检查结果。
```

---

## Disclaimer

This skill provides ESG analysis tools for educational purposes. ESG ratings and analysis are for reference only and should be combined with other investment research methods.
