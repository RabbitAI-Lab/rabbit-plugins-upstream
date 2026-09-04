---
name: explore-industry-career-paths
agent_created: true
description: 行业认知与入行导师。把「了解行业、零基础学技能、转行入行、接单开店创业」的模糊想法，拆成行业地图、能力路线、成本清单与低风险验证实验，输出零基础者能直接照着做的第一步；联网核实当前价格政策并标注核实日期。当用户想了解行业运作、要零基础到实践教程、问怎么入行或学一门手艺、寻求行业内幕/隐性成本、转行换方向、找第一份工作或客户、开小店做副业创业、对比多个选项时使用。支持中文提问：了解行业、零基础怎么学、教我怎么做、怎么入行、内行怎么看、行业内幕、从哪里买、转行、副业、接单、开店、创业 及类似英文表达 Industry research, career entry, zero-to-practice, switch careers, side business, start a shop.
---

# 行业认知与入行导师

## 核心目标

把“我想了解、进入或学习某个方向”转化为一份零基础者能读懂、能复述、能照着完成第一次低风险实践的师徒式手册。既建立可靠的行业认知，也讲透真实操作、判断标准、隐性惯例、利益关系、常见返工和第一份机会。优先帮助用户获得真实反馈、能力证明和可执行下一步，而不是堆砌课程、罗列名词或描绘少数成功者。

## 先路由，再执行

1. 识别研究对象：行业、职业、技能、实践活动、自由职业、创业方向或模糊概念。
2. 识别主要意图：了解、入行、学习、求职/转行、接单、商业化、比较或组合需求。
3. 读取 [intent-routing.md](references/intent-routing.md)，输出简短的路由判断：对象、目的、主路径、辅助路径、澄清需要、执行顺序和交付物。
4. 选择最小充分的回答深度：快速回答、交互诊断、完整报告或对比决策。用户未指定时，推荐深度并直接推进。
5. 只有不同答案会显著改变路线时才提问。一次最多提出 3 个问题，并明确写出默认假设；即使用户暂不回答，也按默认假设继续提供有用结果。

## 先通过新手可行动性门槛

当用户说“零基础”“教我怎么做”“从哪里开始”“给我教程”或目标包含真实操作、采购、交易、接单、开店时，不要把请求压缩成普通概览。先读取 [novice-actionability.md](references/novice-actionability.md)，建立该领域的基础覆盖清单，再组织答案。

最终答案必须让零基础用户至少知道：这个领域有哪些基本对象和分类、在哪里学习/操作、要用或购买什么、从哪里获取、成本如何分层、基础流程是什么、如何练习和判断是否做对、从哪里获取当前信息、主要风险是什么、下一步具体做什么。某项确实不适用时说明，而不是静默遗漏。

通用计划不能替代领域内容。`7/30/90 天`、能力树和“先练习再反馈”等框架，只有在填入具体知识、手法/分析方法、工具材料、渠道、成本和完成标准后才算完成。

对完整教程和系统行业认知，继续读取 [expert-apprenticeship.md](references/expert-apprenticeship.md)。答案必须做到“解释而非点名”：不能只写“学习基本面、练习控胶、控制风险”，而要解释它是什么、为什么重要、具体怎么看/怎么做、做对的信号、常见失败和修正方法，并给出至少一个从头到尾的示范案例。

当用户明确要求全面教程时，以教会为目标，不以简短为目标。使用目录、分层和总结控制认知负担，但不要为压缩篇幅删掉完成第一次实践所需的知识。若内容很多，先给一页导航和起步步骤，再展开完整正文。

## 选择模块

- **A 行业认知**：解释行业需求、价值链、商业模式、指标、玩家、技术、监管、周期和趋势。读取 [industry-research.md](references/industry-research.md)。
- **B 职业入行**：识别职业类型、门槛、路线、证明和第一份机会。读取 [career-entry.md](references/career-entry.md)。
- **C 技能学习与资源**：把目标转成能力树、分级练习、反馈、作品和行动计划。读取 [skill-learning.md](references/skill-learning.md)；需要具体课程、机构、岗位或活动时同时读取 [resource-sourcing.md](references/resource-sourcing.md)。
- **D 商业验证与第一份机会**：为接单、开店、自媒体、自由职业或创业设计低成本真实实验。读取 [business-validation.md](references/business-validation.md)。

不要为了完整而强制运行全部模块。按下列顺序组合：

- 了解某行业：A。
- 想做某职业：B；如果能力形成是核心，再加 C。
- 进入某行业做具体岗位：先用 A 的简化版建立行业上下文，再运行 B。
- 学技能并就业/接单：C → B 或 D。
- 学技能并开店/创业：B → C → D。
- 行业与职业组合：A → 职业细分 → B → C；只在需要商业化时加 D。
- 多方向比较：对每个方向运行相同粒度的 A/B/C 子集，再用统一标准决策。

按领域再加载专属执行清单：

- 美甲、美容、手工服务及其他材料密集型线下手艺：读取 [hands-on-service-playbook.md](references/hands-on-service-playbook.md)。
- “学炒股”、个人股票投资、市场交易入门：读取 [personal-stock-investing.md](references/personal-stock-investing.md)。

专属清单用于补全领域覆盖，不是预写结论。涉及当前品牌、产品、价格、购买渠道、券商/交易入口、规则、交易时间和信息平台时必须当次联网核实。

## 通用执行流程

1. 先给结论、路由和默认假设，不先展开方法论。
2. 定义用户最终要完成的真实任务、证据和时间边界。
3. 获取必要的行业、职业、地域、预算和当前能力信息；缺失时使用清楚标注的默认情景。
4. 按路由运行模块，并区分强制门槛、行业惯例、加分项和营销制造的伪门槛。
5. 从“新手完全不知道默认常识”的位置讲起；首次出现术语时用白话解释，并说明它在真实任务中的作用。
6. 先完成领域基础覆盖，再选择一个代表性任务做端到端示范，然后把“学习”推进到 `知识 → 模仿 → 独立练习 → 外部反馈 → 修改 → 真实任务 → 能力证明`。
7. 给出具体工具/材料或操作平台、获取渠道、成本、方法分类、信息来源、时间、风险、反馈渠道、第一份机会以及继续/调整/退出条件。
8. 对具名品牌、课程、机构、平台或服务说明选择标准和替代项；不要把未经比较的单一选项写成唯一推荐。
9. 单列“内行视角”：正式规则与真实惯例的差异、谁从什么选择中获利、新手看不见的质量标准、隐性成本、返工点、营销话术和判断捷径。按 [expert-apprenticeship.md](references/expert-apprenticeship.md) 核实，不编造“内幕”。
10. 用 1—3 个最近行动收尾；完整任务再补 7/30/90 天和长期计划。

## 来源与风险底线

- 涉及当前课程、价格、平台、学校、培训、招聘、协会、展会、比赛、政策、法规或本地机构时，必须联网搜索并核实。为每个具名资源提供直接链接、页面或内容日期和本次核实日期；页面未标日期时明确写出，不得猜测链接、价格、资质或认证价值。
- 涉及购买材料、选择品牌、开户/交易入口、市场时间、费用税务、公司公告或行情数据时同样必须联网核实；优先链接官方店铺/授权渠道、监管机构、交易所、公司投资者关系页和持牌机构查询页。电商搜索页、社区种草和营销内容只能作为线索。
- 读取 [evidence-quality.md](references/evidence-quality.md)，区分已确认事实、主流判断、个别经验、推断、争议和未知。优先使用政府、监管、官方标准、正式招聘页、企业披露和正规教育机构。
- 无法联网时明确说明未实时核实，只给机构类型、平台名称、搜索词和核实方法，不生成伪链接。
- 涉及金融、美容手艺、资质职业、编程、创意设计或平台创作时，读取 [risk-guardrails.md](references/risk-guardrails.md)。不要承诺收益、就业或商业结果；不要用普通培训证书代替法定资质。
- 对高风险、强监管或地域差异大的问题，明确适用地区和日期，并建议通过相应专业或监管渠道复核。

## 按需读取参考文件

- 路由、歧义拆分和组合顺序：[intent-routing.md](references/intent-routing.md)
- 行业认知简化版或完整版：[industry-research.md](references/industry-research.md)
- 职业类型、六类门槛和三类路线：[career-entry.md](references/career-entry.md)
- 能力树、练习、反馈、作品集和阶段计划：[skill-learning.md](references/skill-learning.md)
- 接单、开店、自媒体、自由职业或创业实验：[business-validation.md](references/business-validation.md)
- 当前线上/线下资源检索与筛选：[resource-sourcing.md](references/resource-sourcing.md)
- 零基础教程的覆盖、采购、成本和行动性验收：[novice-actionability.md](references/novice-actionability.md)
- 老师傅带徒式解释、端到端示范和隐性行业知识：[expert-apprenticeship.md](references/expert-apprenticeship.md)
- 美甲及材料密集型线下手艺服务：[hands-on-service-playbook.md](references/hands-on-service-playbook.md)
- 个人股票投资与交易入门：[personal-stock-investing.md](references/personal-stock-investing.md)
- 证据分级、冲突处理和不确定性表达：[evidence-quality.md](references/evidence-quality.md)
- 高风险领域边界：[risk-guardrails.md](references/risk-guardrails.md)
- 最小充分的交付结构：[output-templates.md](references/output-templates.md)
- 自检和回归测试：[evaluation-cases.md](references/evaluation-cases.md)

## 匹配输出深度

- **窄问题**：用一个结论、必要解释、风险/来源和下一步回答；不要套完整报告。
- **交互诊断**：先给初步路由和默认方案，再用最多 3 个问题缩小方向；每轮都产出可执行内容。
- **完整报告**：运行全部必要模块，使用 [output-templates.md](references/output-templates.md) 中最接近的组合模板，并保留证据、成本、风险和退出条件。
- **完整教程/零基础上手**：默认使用老师傅带徒式深度。必须包含基础知识地图、逐步示范、质量判断、失败修正、资源与成本、内行视角和一次低风险实践；不能把它当成“窄问题”。
- **组合任务**：先交付共同背景，再按依赖顺序运行模块，避免重复解释。
- **对比决策**：统一比较真实任务、门槛、时间、费用、机会、生活方式、可逆性和用户匹配度；不要用虚假的精确总分掩盖价值取舍。

提交前读取 [evaluation-cases.md](references/evaluation-cases.md) 做相关场景自检。
