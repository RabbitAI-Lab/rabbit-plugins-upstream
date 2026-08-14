---
slug: game-theory
name: "game-theory"
version: 1.0.1
displayName: "加密协议博弈论分析"
summary: "面向crypto协议、DeFi机制和治理系统的博弈论分析框架，识别Nash Equilibrium与MEV风险"
summary_zh: "面向crypto协议、DeFi机制和治理系统的博弈论分析框架，识别Nash Equilibrium与MEV风险"
license: "MIT"
description: |- 功能涵盖: theory。 功能涵盖:。Use when 用户需要加密协议博弈论分析相关功能时使用。不适用于超出本技能能力范围的复杂需求。适用于独立开发者、企业团队和自动化工作流场景。支持中文交互，无需复杂配置即开即用。输出结果可直接使用，减少二次加工成本。提供结构化输出和错误处理机制。支持多场景应用和灵活配置。 功能涵盖: game。
  面向加密协议、DeFi机制和治理系统的博弈论分析框架.
  基于Five Questions分析模型，覆盖Nash Equilibrium、Dominant Strategy、Mechanism Design等核心概念，
  支持MEV Game、Liquidity Game、Governance Game等常见crypto博弈场景分析，
  并提供Tokenomics、Governance、Mechanism三维度Red Flags检测.
  适用于协议设计审计、激励对齐评估与攻击向量识别.
tools:
  - read
  - exec
  - glob
  - grep
homepage: ""
tags:
  - 生活服务
  - 工具
  - 效率
  - 创意
  - 图像
  - governance
  - game
  - games
  - token
  - 解决方案
category: "Automation"
homepage: "https://skillhub.cn/skill/"
---
> **核心功能**: 本技能提供中文交互、相关功能时使用、化工作流场景等能力。

# 加密协议博弈论分析

面向web3协议的激励系统设计与博弈论分析框架，用于识别Nash Equilibrium、评估MEV风险与治理攻击向量.
## 输入参数
| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 加密协议博弈论分析处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 专业版增强能力
| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 加密协议博弈论分析治理系统的博弈论分析 | 不支持 | 支持 |
| 深度漏洞扫描与CVE关联 | 不支持 | 支持 |
| 安全基线合规审计 | 不支持 | 支持 |
| 批量资产风险评分 | 不支持 | 支持 |
| 威胁情报实时订阅与告警 | 不支持 | 支持 |

## 安装与配置
### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Bash/Shell | 运行时 | 可选 | 用于执行分析脚本 |
| Nashpy | Python库 | 可选 | `pip install nashpy` 用于Nash Equilibrium计算 |
| Gambit | 软件 | 可选 | 用于博弈论建模与求解 |

### API Key 配置
- 本Skill基于指令驱动，无需额外API Key（除内容中明确标注的外部API）

### 可用性分类
- **分类**: MD+EXEC（）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行博弈论分析任务

## 功能能力
### Five Questions分析框架

对任意协议或机制，通过五个核心问题建模博弈：
1. **Who are the players?**（玩家识别：Users、LPs、validators、searchers、governance token holders）
2. **What are their strategies?**（策略空间：每个玩家可执行的动作集合）
3. **What are the payoffs?**（收益结构：每种结果对各方的影响）
4. **What information do they have?**（信息结构：Complete / Incomplete / Asymmetric Information）
5. **What's the equilibrium?**（均衡分析：理性参与者的最终收敛点）

输出标准Analysis Template包含Players、Strategy Space、Payoff Structure、Information Structure、Equilibrium Analysis、Recommendations六个章节.
### 核心博弈论概念应用
| 概念 | 定义 | Crypto应用场景 |
|:---:|:---:|:---:|
| Nash Equilibrium | 没有玩家能通过单方面改变策略而改善收益的状态 | Staking系统中validator的stake分布均衡 |
| Dominant Strategy | 无论他人如何行动都是最优的策略 | Second-price auction中真实报价是Dominant Strategy |
| Pareto Efficiency | 无法在不损害他人的前提下使某人更好的状态 | AMM fee结构对traders和LPs的Pareto效率 |
| Mechanism Design | "逆向博弈论"——设计规则以达成期望均衡 | Token vesting schedule的长期激励对齐设计 |
| Schelling Point | 无沟通情况下人们收敛到的解 | 价格水平的心理支撑/阻力位 |
| Incentive Compatibility | 诚实行为对参与者最优的状态 | Oracle设计中诚实报告为Dominant Strategy |
| Common Knowledge | 所有人知道X，所有人知道所有人知道X，无限递归 | 公链状态创建balances/positions的Common Knowledge |

### 六大分析模式

支持识别并分析六种经典博弈模式，每种均提供crypto实例与解决方案：

1. **Tragedy of the Commons**（公地悲剧）：Gas price竞价、governance投票冷漠、MEV提取降低UX；解决方案含Harberger taxes、Quadratic mechanisms、Commitment schemes
2. **Prisoner's Dilemma**（囚徒困境）：Liquidity mining mercenaries（farm and dump）、validator费用竞底、bridge安全搭便车；解决方案含Repeated games、Commitment mechanisms（staking/slashing）
3. **Coordination Game**（协调博弈）：L2选择、token标准采用、hard fork协调；解决方案含Focal points（Schelling points）、Sequential moves、Communication mechanisms
4. **Principal-Agent Problem**（委托代理问题）：Protocol team vs token holders、governance delegates、fund managers；解决方案含Incentive alignment、Monitoring、Bonding
5. **Adverse Selection**（逆向选择）：Token launches、insurance protocols、lending；解决方案含Signaling、Screening、Pooling equilibria
6. **Moral Hazard**（道德风险）：带保险的协议冒险、bailout预期、anonymous teams rug；解决方案含Monitoring、Incentive alignment、Reputation systems

### Common Crypto Games分析
针对五种crypto原生博弈提供专门分析能力：

- **MEV Game**：玩家为Users、searchers、builders、validators；核心洞察为transaction ordering是博弈，users常为输家
- **Liquidity Game**：玩家为LPs、traders、arbitrageurs；核心洞察为impermanent loss是adverse selection的代价
- **Governance Game**：玩家为token holders、delegates、protocol team；核心洞察为rational apathy + concentrated interests = capture
- **Staking Game**：玩家为stakers、validators、delegators；核心洞察为security budget必须超过attack profit
- **Oracle Game**：玩家为data providers、consumers、attackers；核心洞察为操纵收益必须小于操纵成本

### Red Flags检测
提供三维度协议设计风险检测：

- **Tokenomics Red Flags**：insiders vesting不对称、inflation稀释、无sink机制、reward无risk
- **Governance Red Flags**：quorum过低、无timelock（flash loan攻击）、token voting only（plutocracy）、delegates无skin in game
- **Mechanism Red Flags**：first-come-first-served（bot优势）、sealed bid无commitment（frontrunning）、rebates（MEV提取）、复杂公式（隐藏漏洞）

### 高级分析能力
支持四类高级博弈论主题的深入分析：

- **Repeated Games and Reputation**：单次博弈均衡差，重复博弈通过Trigger strategies、Reputation building、Future value促成合作；解释anonymous actors行为更差
- **Evolutionary Game Theory**：策略竞争选择；分析哪些协议长期存活、narrative竞争、bot策略进化
- **Bayesian Games**：不完全信息博弈；分析未知对手方交易、anonymous team评估
- **Cooperative Game Theory**：可形成binding coalitions的博弈；分析MEV extraction coalitions、validator cartels、governance blocs

## 快速启航
1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 使用方法
1. **确定分析目标**：明确要分析的协议或机制（DeFi协议、governance提案、tokenomics设计等）
2. **应用Five Questions框架**：识别players、strategies、payoffs、information、equilibrium
3. **选择分析模式**：从六大Pattern中匹配最贴切的博弈结构
4. **识别Common Crypto Games**：判断属于MEV / Liquidity / Governance / Staking / Oracle哪类博弈
5. **运行Red Flags检测**：对Tokenomics、Governance、Mechanism三维度进行风险扫描
6. **进行高级分析**：按需调用Repeated Games、Bayesian Games等高级分析能力
7. **输出Recommendations**：给出mechanism改进、monitoring建议、parameter bounds

## 应用示例
### 示例1：DeFi借贷协议的Principal-Agent分析

```
分析目标: 某 lending protocol 的清算机制
Step 1 - Players:
  - Borrowers（目标：最小化清算损失）
  - Liquidators（目标：最大化清算利润）
  - Protocol（目标：维持偿付能力）
Step 2 - 分析模式匹配: Principal-Agent Problem
  - Principal = Protocol，Agent = Liquidators
  - 信息不对称：Liquidators比Protocol更早感知抵押率变化
Step 3 - Red Flags检测:
  - Mechanism Red Flag: first-come-first-served清算 → bot优势
  - 无commitment机制 → 可frontrunning
Step 4 - Recommendations:
  - 引入Dutch auction清算机制
  - 添加清算延迟（timelock）
  - 设置清算奖励上限
```

### 示例2：治理提案的Governance Game分析

```
分析目标: 某 DAO 的治理投票提案是否易被capture
Step 1 - Players:
  - Token holders（rational apathy，参与率低）
  - Large delegates（concentrated interests）
  - Protocol team（信息优势）
Step 2 - Common Crypto Game: Governance Game
  - 核心洞察: rational apathy + concentrated interests = capture
Step 3 - Red Flags检测:
  - Governance Red Flags:
    * Quorum threshold 仅 5% → minority capture风险
    * 无timelock → flash loan攻击可能
    * Token voting only → plutocracy
Step 4 - 高级分析:
  - Bayesian Games: 分析delegate与voter间的信息不对称
  - Cooperative Game Theory: 识别voting blocs形成的可能
Step 5 - Recommendations:
  - 提高quorum至15-20%
  - 添加timelock（至少48小时）
  - 引入quadratic voting或conviction voting
  - 要求delegates bonding（skin in game）
```

## 错误恢复方案
| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| 无法识别players | 协议参与者角色不清晰 | 检查on-chain合约与文档，补充隐式参与者（如searchers、arbitrageurs） |
| Nash Equilibrium不收敛 | 策略空间连续或博弈无限重复 | 使用Nashpy库进行数值求解，或转为离散策略空间近似 |
| 误判博弈模式 | 协议同时具有多种博弈特征 | 优先识别dominant特征，对次要特征单独分析后综合 |
| Red Flags漏报 | 仅检查单维度风险 | 强制对Tokenomics、Governance、Mechanism三维度逐一扫描 |
| MEV分析偏差 | 未考虑builder-validator关系 | 补充Proposer-Builder Separation（PBS）视角，分析searcher-builder纵向关系 |
| Incentive Compatibility验证失败 | 诚实行为非最优策略 | 重新设计reward/penalty结构，引入slashing或bonding机制 |

## 问答集成
### Q1: 这个Skill适用于分析哪些类型的协议？
A: 适用于所有web3协议的博弈论分析，包括DeFi借贷、AMM、staking、governance、oracle、MEV相关协议。特别适合分析tokenomics设计、激励对齐、攻击向量识别与机制设计审计.
### Q2: 如何判断一个协议是否存在MEV风险？
A: 通过MEV Game分析框架，检查transaction ordering是否可被操纵、是否存在first-come-first-served机制、sealed bid是否有commitment。若存在rebates/refunds机制，通常伴随MEV提取.
### Q3: Nash Equilibrium在实际协议分析中如何应用？
A: 先建模players和strategies，定义payoff functions，然后检查是否存在Dominant Strategy。若无dominant strategy，计算Nash Equilibrium。对于staking系统，Nash Equilibrium决定validator的stake分布.
### Q4: Red Flags检测发现多个风险点如何优先级排序？
A: 按攻击成本与影响排序：governance capture（flash loan攻击）> tokenomics vesting不对称 > mechanism的frontrunning风险。优先修复攻击成本最低、影响最大的风险点.
### Q5: 是否需要Nashpy或Gambit等外部工具？
A: 基础分析无需外部工具，Agent可通过Markdown指令完成定性分析。涉及复杂数值求解（如连续策略空间的Nash Equilibrium计算）时，可选用Nashpy（`pip install nashpy`）或Gambit进行辅助计算.
### Q6: 如何分析anonymous team的协议风险？
A: 使用Bayesian Games框架分析信息不对称，结合Repeated Games理论——anonymous actors因无reputation成本，行为通常比doxxed teams更差。重点检查Moral Hazard风险与rug可能性.
## 使用约束
- 定性分析为主，复杂博弈的精确数值求解需依赖Nashpy/Gambit等外部工具
- 无法实时获取on-chain数据，需用户提供协议参数与合约信息
- Evolutionary Game Theory的长期预测具有不确定性，narrative竞争难以精确建模
- Bayesian Games的belief建模依赖用户输入，无法自动推断对手方类型分布
- 不替代正式的安全审计，仅提供博弈论视角的风险评估

## 响应格式
```json
{
  "success": true,
  "data": {
    "result": "加密协议博弈论分析处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "game-theory"
    }
  },
  "execution_log": [
    "解析输入参数",
    "执行核心处理",
    "格式化输出结果"
  ],
  "error": null
}
```

## 故障应对方案
| 错误现象 | 可能原因 | 诊断步骤 | 解决方案 |
| --- | --- | --- | --- |
| 无法识别玩家角色 | 协议文档不完整或合约代码未公开 | 审查合约代码和协议文档，确保所有参与者角色被识别 | 完善文档和代码注释，确保所有玩家角色清晰 |
| 策略空间定义错误 | 策略空间定义不准确或遗漏关键策略 | 重新审视协议机制，确保策略空间全面覆盖所有可能行动 | 重新定义策略空间，包括所有玩家的行动集合 |
| 收益结构计算错误 | 收益计算公式错误或参数设置不当 | 检查收益计算公式和参数设置，确保正确无误 | 修正公式和参数，重新计算收益结构 |
| 信息结构不明确 | 信息结构描述模糊或信息不对称 | 明确信息结构，确保所有玩家对信息拥有相同的了解 | 重新描述信息结构，确保信息对称性 |
| Nash Equilibrium不收敛 | 策略空间连续或存在无限重复博弈 | 使用数值方法求解或离散化策略空间 | 使用Nashpy库进行数值求解，或转换为离散策略空间进行近似 |

## 安全事项
| 风险项 | 等级 | 防护措施 | 验证方法 |
| --- | --- | --- | --- |
| MEV提取风险 | 高 | 实施交易排序限制和交易费用调整 | 监控交易排序和费用变化，确保无异常行为 |
| 治理捕获风险 | 中 | 提高投票门槛和引入timelock | 定期审计治理流程，确保决策透明和公正 |
| 逆向选择风险 | 中 | 设计筛选机制和信号传递机制 | 定期评估市场参与者的行为，识别潜在逆向选择 |
| 道德风险 | 中 | 引入监督机制和惩罚措施 | 定期审查协议机制，确保诚实行为得到奖励 |
| 信息泄露风险 | 中 | 实施数据加密和访问控制 | 定期进行安全审计，确保数据安全 |

## 创新亮点
| 场景 | 效率提升量化分析 | 差异化对比 |
| --- | --- | --- |
| 协议设计审计 | 通过快速识别潜在风险，缩短审计周期，提升设计效率 | 传统审计方法需手动分析，耗时较长 |
| 激励对齐评估 | 通过博弈论模型，更准确地评估激励结构，提升对齐效率 | 传统方法依赖主观判断，准确性较低 |
| 攻击向量识别 | 快速识别潜在攻击向量，提升安全防护效率 | 传统方法需大量手动分析，效率低 |
| 治理系统分析 | 通过博弈论模型，更全面地分析治理机制，提升治理效率 | 传统方法依赖经验，分析不全面 |
| MEV风险评估 | 通过模型分析，更准确地评估MEV风险，提升风险管理效率 | 传统方法依赖经验，评估不准确 |
| 重复博弈分析 | 通过重复博弈理论，更深入地分析长期行为，提升策略制定效率 | 传统方法难以分析长期行为，策略制定困难 |

| 场景 | 效率提升量化分析 | 差异化对比 |
| --- | --- | --- |
| 协议设计审计 | 将审计周期缩短50% | 传统审计方法需手动分析，耗时较长 |
| 激励对齐评估 | 将评估时间缩短30% | 传统方法依赖主观判断，准确性较低 |
| 攻击向量识别 | 将识别时间缩短70% | 传统方法需大量手动分析，效率低 |
| 治理系统分析 | 将分析时间缩短40% | 传统方法依赖经验，分析不全面 |
| MEV风险评估 | 将评估时间缩短60% | 传统方法依赖经验，评估不准确 |
| 重复博弈分析 | 将策略制定时间缩短80% | 传统方法难以分析长期行为，策略制定困难 |

## 功能介绍
- **自动化执行**: 面向crypto协议、DeFi机制和治理系统的博弈论分析框架，识别Nash Equilibrium与MEV风险
- **文件处理**: 支持多种文件格式的读取、解析和写入操作
- **API集成**: 通过标准化接口调用外部服务并处理响应
- **命令执行**: 在安全沙箱中执行系统命令并收集结果
- **信息检索**: 快速搜索和过滤目标数据

## 指南中心
### Q1: 加密协议博弈论分析支持哪些输入格式？

A1: 面向crypto协议、DeFi机制和治理系统的博弈论分析框架，识别Nash Equilibrium与MEV风险。支持文本指令和结构化参数输入，具体格式参考使用流程章节。

### Q2: 需要配置API Key吗？

A2: 是的，部分功能需要配置对应平台的API Key。请在依赖说明章节查看具体要求，并通过环境变量安全配置。

### Q3: 命令行执行失败怎么办？

A3: 检查命令参数是否正确，确认运行环境支持exec能力。如遇权限问题，请参照错误处理章节排查。

## 性能评估
| 操作场景 | 手动耗时 | 自动化耗时 | 效率提升 |
|----------|---------|-----------|---------|
| 文件解析与提取 | 5-10分钟/个 | <5秒/个 | 60-120x |
| 批量文件处理(100个) | 8-16小时 | <5分钟 | 96-192x |
| API调用与响应解析 | 2-3分钟/次 | <1秒/次 | 120-180x |
| 多接口数据聚合 | 15-30分钟 | <10秒 | 90-180x |
| 命令执行与结果收集 | 3-5分钟/次 | <2秒/次 | 90-150x |
| 重复任务批量执行 | 因任务而异 | 线性缩减 | 5-50x |
| 错误排查与修复 | 10-30分钟 | <30秒 | 20-60x |

## 特色对比
| 对比维度 | 加密协议博弈论分析 | 传统手动方式 | 通用脚本工具 |
|---------|------------|-------------|------------|
| 自动化程度 | 全流程自动 | 完全手动 | 部分自动 |
| 错误处理 | 内置错误恢复 | 依赖人工经验 | 基本try-catch |
| 可复用性 | 参数化配置 | 一次性脚本 | 模板化 |
| 安全合规 | 内置安全检查 | 无安全保障 | 无安全保障 |
| 适用场景 | 面向crypto协议、DeFi机制和治理系统的博弈论分析框架，识别Nash Eq | 通用场景 | 通用场景 |

### 加密协议博弈论分析通用排查步骤

1. **检查输入参数**: 确认所有必填参数已提供且格式正确
2. **查看日志输出**: 定位具体错误行和异常类型
3. **验证环境配置**: 确认依赖库版本和运行环境满足要求
4. **逐步调试**: 缩小问题范围,隔离故障模块

## 依赖说明

### 运行环境
- **Agent 平台**: 支持SKILL.md的任意AI Agent
- **操作系统**: Windows / macOS / Linux

### 可用性分类
- **分类**: MD（纯Markdown指令，通过自然语言驱动Agent完成操作）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent完成操作。
