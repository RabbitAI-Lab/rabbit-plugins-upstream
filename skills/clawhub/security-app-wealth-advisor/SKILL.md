---
name: Bank APP Wealth Advisor Assistant
slug: bank-app-wealth-advisor
description: AI-powered bank APP wealth advisory assistant — covers product recommendation, investment consultation, financial planning, and compliance-compliant customer interaction for bank mobile applications. Built for China commercial bank digital banking teams and wealth management advisors. Keywords: bank APP, wealth advisor, digital banking, mobile banking, AI advisor, product recommendation, China banking digital, 银行APP, 财富顾问, 智能投顾, 手机银行, 数字银行, 产品推荐, 理财推荐, 基金销售, 资产配置.
version: "3.0.3"

capabilities:
  - educational-reference
  - advisory-only
  - requires-human-review
  - illustrative-code-snippets
---

# Bank APP Wealth Advisor Assistant / 银行APP财富顾问助手
> **⚠️ SECURITY NOTICE**
> - **Type:** Educational reference / analytical framework ONLY
> - **Code in this document is illustrative.** The Python snippets are reference material describing matching logic; they are not executed by this skill and are not a drop-in production system. Adapt and test them in your own environment.
> - **This skill does not itself read or write files, call external services, or persist data.** What happens to any customer data you type into the conversation depends on the platform you run it on, not on this skill.
> - **Customer profiles are sensitive.** Risk preference, asset size and transaction intent are personal financial information. Apply data minimisation: use anonymised or synthetic profiles for design and testing, and never paste real customer records into a conversation.
> - **All outputs require human review before real-world application**
> - **NOT financial, legal, or insurance advice** — no output from this skill may be presented to a customer as a personalised recommendation without review by a qualified advisor




### 银行监管最新动态 [2026-09-14更新]

| 动态类型 | 内容摘要 | 影响范围 | 对应话术/系统动作 |
|---------|---------|---------|-----------------|
| 银行监管 | 2026年Q1理财信息披露'三清'推进，财富管理话术需更新 | 投顾话术和策略模板需适配市场新环境 | 业绩展示须同时给出比较基准与区间 |
| 银行监管 | 净息差压力下，银行理财产品收益率下行，投顾建议需调整 | 投顾话术和策略模板需适配市场新环境 | 弱化收益承诺，强化流动性与期限匹配 |
| 银行监管 | 2026年A股量化资金占比30%-40%，财富管理策略需关注量化冲击 | 投顾话术和策略模板需适配市场新环境 | 权益类推荐需提示波动放大风险 |
| 新增·适当性管理 | 投资者适当性管理的持续细化：风险测评有效性、重复购买匹配、超风险购买的特别确认 | 推荐引擎与前端流程均需改造 | 超风险匹配必须阻断或走特别确认流程 |
| 新增·AI应用合规 | 银行业人工智能应用的安全开发与人工复核要求下沉为机构制度 | 智能投顾类功能需可解释、可追溯 | 推荐理由需可追溯到具体字段与规则 |
| 新增·可回溯 | 线上销售与推荐行为的可回溯要求扩展至 APP 端 | 推荐记录需留痕 | 每次推荐保存版本、规则与依据 |

**新动态（截至 2026-09-14）：**
- **适当性匹配从"一次测评"走向"持续匹配"**：监管与行业实践均强调风险测评并非一次性动作，产品风险等级与客户风险承受能力的匹配需在每次推荐时校验，超风险购买须有明确提示与客户确认。对推荐引擎的含义是：匹配逻辑必须输出"为什么匹配"的可解释依据，而不是只给一个排序结果。
- **AI 生成内容的对客使用受严格约束**：智能投顾场景中，AI 输出的对客表述普遍要求"生成—复核—留痕"三步，且不得把模型输出直接作为个性化投资建议推送。本 Skill 的话术模板应始终定位为供顾问参考的草稿。
- **业绩展示口径趋严**：展示历史业绩时普遍要求同时呈现比较基准、完整区间与风险指标，避免只展示表现最好的一段。
- 以上为公开信息综述，**具体条文与执行口径以国家金融监督管理总局、中国证监会、中国银行业协会及所在机构合规部门官方最新发布为准**。

> **数据截止**: 2026-09-14 | 来源：国家金融监督管理总局、安永Q1分析、行业公开信息
> **声明**: 以上动态供参考，具体以官方最新发布为准

> **English:** AI-powered wealth advisory assistant for bank mobile applications — provides product recommendations, investment consultation, and compliance-compliant customer interaction. Built for digital banking teams.
>
> **中文:** 银行APP财富顾问助手——为手机银行提供产品推荐、投资咨询、合规客户交互。适用：数字银行团队、财富管理师。

---

## ⚠️ 使用前必读：数据最小化声明

> 财富顾问场景天然涉及**客户金融个人信息**：风险测评结果、资产规模、可用资金、持仓与交易意图。这类信息属于敏感个人信息，受《个人信息保护法》与金融监管要求约束。
>
> **请遵循数据最小化原则：**
> 1. 设计、测试与演示阶段一律使用**匿名化或合成的客户画像**，不要粘贴真实客户姓名、账号、身份证号或完整持仓
> 2. 话术与匹配逻辑的输出是**参考模板**，不得未经具备资质的顾问复核即直接推送给客户
> 3. 适当性匹配结果不得作为绕过风险测评的依据——风险测评应由客户本人在合规渠道完成
> 4. 若确需在系统中落库，须符合所在机构的数据分级、加密与留痕制度

---

## Industry Pain Points / 行业痛点

| Pain Point / 痛点 | Impact / 影响 | Solution / 本Skill解决方案 | 典型表现 | 可量化指标 |
|------------------|-------------|------------------------|---------|-----------|
| **APP用户粘性低** | 用户用完即走，无深度服务 | AI投顾提升个性化体验 | 月活高但停留时长极短 | 人均停留时长、功能复用率 |
| **产品匹配效率低** | 人工推荐成本高 | 智能产品匹配引擎 | 理财经理一人服务数百客户 | 单次推荐耗时、覆盖客户数 |
| **合规要求严** | 监管禁止虚假宣传 | 合规话术自动检查 | 话术含"稳健""保本"等模糊表述 | 违禁词命中率、复核通过率 |
| **服务覆盖有限** | 人工客服无法7x24 | AI24小时在线解答 | 非工作时间咨询无人应答 | 首响时长、夜间解决率 |
| **交叉销售难** | 客户画像不完整 | 多维度客户分析 | 只买单一产品，AUM 长期不变 | 产品持有数、AUM 增长率 |
| **适当性风险** | 推荐与客户风险等级不匹配 | 匹配规则前置校验 | 保守型客户被推荐 R4 产品 | 超风险推荐拦截率 |

---

## Trigger Keywords / 触发关键词

**English Triggers:** bank APP, wealth advisor, digital banking, mobile banking, AI advisor, product recommendation, financial planning, customer service

**中文触发词（优先）：** 银行APP / 财富顾问 / 智能投顾 / 手机银行 / 数字银行 / 产品推荐 / 理财咨询 / 基金销售 / 资产配置 / 客户分层 / 交叉销售 / 合规话术 / 智能客服 / 风险测评 / 适当性匹配

**使用示例（完整提问）：**
- "稳健型客户、20 万可用资金、偏好 180 天以内，帮我梳理产品匹配逻辑" → 走能力 1，输出过滤条件与评分因子
- "这段基金推荐话术里有'基本没风险'和'预期至少4%'，帮我改成合规版本" → 走能力 3 禁止用语表
- "客户风险测评是保守型，但主动想买 R4，这个流程该怎么设计" → 走能力 1 的超风险确认流程
- "帮我写一段对客的资产配置说明，不能出现收益承诺" → 走能力 2 话术模板 + 合规改写表

---

## Core Capabilities / 核心能力

### 1. Product Matching Engine / 产品匹配引擎

```python
class WealthAdvisor:
    """智能财富顾问"""
    
    def match_products(self, customer_profile: dict, 
                      available_products: list) -> list:
        """
        智能产品匹配
        Args:
            customer_profile: 客户画像
            available_products: 可选产品列表
        """
        # 风险匹配
        risk_level_map = {
            "保守型": ["R1", "R2"],
            "稳健型": ["R1", "R2", "R3"],
            "平衡型": ["R2", "R3", "R4"],
            "成长型": ["R3", "R4", "R5"],
            "激进型": ["R4", "R5"]
        }
        
        allowed_risk = risk_level_map.get(
            customer_profile.get("risk_preference", "稳健型"), ["R2", "R3"]
        )
        
        # 收益匹配
        expected_return = customer_profile.get("expected_return", 0.05)
        
        matched = []
        for product in available_products:
            # 风险等级过滤
            if product["risk_level"] not in allowed_risk:
                continue
            
            # 收益率匹配
            if product["expected_return"] >= expected_return - 0.02:
                score = self._calculate_match_score(
                    customer_profile, product
                )
                matched.append({
                    **product,
                    "match_score": score,
                    "recommendation_reason": self._generate_reason(
                        customer_profile, product
                    )
                })
        
        return sorted(matched, key=lambda x: x["match_score"], reverse=True)
    
    def _calculate_match_score(self, customer: dict, 
                               product: dict) -> float:
        """计算匹配度评分"""
        score = 100
        
        # 期限匹配
        preferred_term = customer.get("preferred_term", 365)
        product_term = product.get("term_days", 365)
        term_diff = abs(preferred_term - product_term) / 365
        score -= term_diff * 10
        
        # 起购金额
        if product.get("min_amount", 0) > customer.get("available_fund", 0):
            score -= 30
        
        # 收益率
        expected = customer.get("expected_return", 0.05)
        actual = product.get("expected_return", 0)
        if actual >= expected:
            score += 10
        else:
            score -= abs(actual - expected) * 100
        
        return max(0, min(100, score))
```

> 以上代码为**逻辑示意**，用于说明匹配因子如何加权，不是可直接投产的实现。真实系统还需处理产品状态（在售/停售/限额）、客户持仓集中度、适当性有效期与超风险阻断。

**调用示例：**

```python
advisor = WealthAdvisor()
profile = {
    "risk_preference": "稳健型",       # 来自客户风险测评，须为有效测评结果
    "expected_return": 0.035,
    "preferred_term": 180,
    "available_fund": 200_000,
}
products = [
    {"name": "稳健添利90天", "risk_level": "R2", "expected_return": 0.032,
     "term_days": 90,  "min_amount": 10_000},
    {"name": "安盈365天",   "risk_level": "R2", "expected_return": 0.038,
     "term_days": 365, "min_amount": 50_000},
    {"name": "进取混合A",   "risk_level": "R4", "expected_return": 0.075,
     "term_days": 365, "min_amount": 1_000},   # R4 超出稳健型，应被过滤
]
# => 返回仅含两只 R2 产品，R4 在风险等级过滤阶段被剔除
```

**三个必须补上的生产级校验：**
1. **适当性有效期**：风险测评过期后不得沿用旧等级，应引导客户重新测评
2. **超风险阻断**：若客户主动要求超出风险等级的产品，不能直接推荐，须走特别确认流程并留痕
3. **集中度校验**：单产品占可用资金比例过高时，即便风险等级匹配也应降权

### 2. Investment Consultation Scripts / 投资咨询话术

```python
INVESTMENT_SCRIPTS = {
    "基金购买引导": {
        "场景": "客户咨询基金",
        "话术": """
        "您好！根据您的风险测评结果【{risk_level}】，
        我推荐您关注【{fund_name}】基金。
        
        这只基金的特点：
        • 基金类型：{fund_type}
        • 风险等级：{risk_level}
        • 近一年收益：{return_1y}%
        • 基金经理：{manager}（从业{years}年）
        
        适合您的理由：
        1. {reason_1}
        2. {reason_2}
        3. {reason_3}
        
        【风险提示】基金有风险，投资需谨慎。过往业绩不代表未来表现。
        请您根据自身情况谨慎决策。"
        """,
        "合规检查": [
            "不得承诺保本",
            "必须说明基金有风险",
            "过往业绩仅供参考"
        ]
    },
    
    "资产配置建议": {
        "场景": "客户有大额资金",
        "话术": """
        "张先生/女士，您好！
        
        根据您目前的资产状况，我们建议做一个科学的资产配置：
        
        【保守配置】40% → 银行存款+国债
        特点：安全稳健，适合保本需求
        
        【稳健配置】30% → 银行理财+债券基金
        特点：收益稳健，波动较小
        
        【成长配置】20% → 混合基金+股票基金
        特点：追求较高收益，承担一定风险
        
        【流动性】10% → 货币基金
        特点：随存随取，应急备用
        
        这个配置方案可以帮助您分散风险，
        同时实现资产的稳健增值。"
        """
    }
}
```

**话术改写示例（合规 vs 违规）：**

| 场景 | 违规表述 | 合规表述 |
|------|---------|---------|
| 介绍业绩 | "这只基金去年赚了 18%，很稳" | "这只基金近一年收益率为 18%，同期业绩比较基准为 X%；过往业绩不代表未来表现" |
| 安抚波动 | "短期波动不用担心，肯定会涨回来" | "该类产品存在净值波动，短期可能出现浮亏，请结合您的持有期限判断" |
| 促单 | "这个产品额度有限，今天不买就没了" | "该产品的开放期至 X 日，您可在此期间内根据安排决定是否购买" |
| 风险说明 | "基本没什么风险" | "该产品风险等级为 R2，主要风险包括 X、Y，详见产品说明书" |
| 收益预期 | "预期收益至少 4%" | "业绩比较基准为 4%，不构成收益承诺，实际以产品运作结果为准" |

**完整对客话术示例（基金咨询）：**

```
"您好。您本次的风险测评结果为【稳健型（C2）】，
 我为您筛选了风险等级在 R2 及以下的产品供参考。

 其中【XX 纯债基金】的基本情况：
 • 风险等级：R2（中低风险）
 • 近一年收益率：3.2%（同期业绩比较基准 2.8%）
 • 开放期：每日开放，赎回 T+1 到账

 需要提示的是：
 1. 过往业绩不代表未来表现，基金有风险，投资需谨慎
 2. 该产品仍存在净值波动，短期可能出现浮亏
 3. 以上信息供您参考，最终是否购买请结合自身情况，
    并在购买前阅读产品说明书与风险揭示书"
```

### 3. Compliance Check / 合规检查

```markdown
## APP投顾合规检查清单

### 必须包含的要素
| 检查项 | 要求 | 出现位置 | 缺失后果 |
|-------|------|---------|---------|
| 风险提示 | 必须出现"投资有风险" | 首次推荐前 | 合规扣分、客户投诉 |
| 收益说明 | 不得承诺保本保收益 | 每次提及收益 | 被认定为误导销售 |
| 历史业绩 | 必须注明"仅供参考"，并给出比较基准与完整区间 | 展示业绩时 | 选择性展示被质疑 |
| 适当性 | 必须匹配客户风险等级，且测评在有效期内 | 推荐前 | 适当性违规 |
| 产品揭示 | 必须包含产品说明书与风险揭示书入口 | 购买路径上 | 告知义务履行不充分 |
| 人工复核 | 对客输出须经具备资质人员确认 | 推送前 | 违规对客推送 |
| 留痕 | 记录推荐版本、规则依据与复核人 | 每次推荐 | 可回溯要求不满足 |

### 禁止用语
| 禁止 | 替代 | 风险等级 |
|-----|------|---------|
| "保本" | "相对稳健" | 高 |
| "稳赚不赔" | "追求稳健收益" | 高 |
| "最低收益X%" | "历史平均收益X%" | 高 |
| "100%安全" | "风险可控" | 高 |
| "肯定会涨回来" | "存在净值波动，请结合持有期限判断" | 中 |
| "额度有限不买就没了" | "开放期至 X 日，请在此期间内决定" | 中 |
| "和存款一样" | "与存款不同，本产品不保本" | 高 |
| "跟着买就行" | "以上供您参考，请结合自身情况判断" | 中 |
```

---

## Disclaimer

This skill provides wealth advisory tools for educational purposes. All recommendations must comply with applicable regulations and be reviewed by qualified financial advisors.
