# R1 缺陷报告 · 心理学自学教练 v1.0.0

> 基线：版本 v1.0.0，全新技能，无历史测试轮次 → 从 R1 起做完整五步流程。
> 测试维度覆盖：跨会话生命周期、安全过/漏触发、输入护栏、外部输入保真、文档时效、一致性三处、多语言（负向）。
> 方法：真实读取源文件 + 模拟 fixture 走查，逐项比对规划与 SKILL.md 实际规则。

## 一、状态核验（Step 1）
- 目标目录 md/json/py 文件数：SKILL.md(1) + modules(9) + curriculum(8) + resources(5) + schemas(1) + tools(5) + practice(39) + assessment(25) = 完整落地。
- 版本：v1.0.0；累计缺陷基线：0。
- 判定：全新技能，进入完整 R1 流程（非盲区增量模式）。

## 二、发现清单（D1–D8）

| 编号 | 严重度 | 位置 | 现象 |
|---|---|---|---|
| D1 | P1 | SKILL.md 第10节 / roadmap modules | 7 个模块仅 theory、counseling 有 completed+1 触发；assessment/reading/cases/methods/support 五个模块无触发点，永远为 0 → progress_query 进度条全空，核心进度反馈失效 |
| D2 | P1 | SKILL.md 第140行 危机词表 | 缺「活着没意思」「不如死了」「死了算了」「没盼头」等常见轻生表述 → 真实危机可能漏触发护栏 |
| D3 | P2 | SKILL.md 第59/77/130行 | Onboarding 的 tempData 仅内存未写盘，中途退出下次丢失，跨会话续接无法实现（与第130行承诺矛盾） |
| D4 | P2 | SKILL.md 第六/二节 crisis | 危机一律全套热线，缺「比喻宣泄 vs 真实危机」分层，可能疏远仅情绪宣泄用户 |
| D5 | P2 | SKILL.md 第304行 unknown | 跨领域请求（如「帮我写代码」）未明确拒绝引导，仅模糊回应 |
| D6 | P2 | SKILL.md 第276行 group_meeting | 团队主题库按「月」分段（🌱0-3月等），但处理器「按阶段选主题」未定义「当前周→主题阶段」映射 |
| D7 | P3 | SKILL.md 第304行 unknown | 空/无意义输入无显式处理规则 |
| D8 | P3 | SKILL.md 第235行 analyze_dialogue | 粘贴外部逐字稿缺保真基线声明（未提示「仅对你提供内容做技术反馈、保留原貌」） |

## 三、负向结论（已一致，未改动）
- 维度3 多语言：本技能以中文自学语境为主，无英文成品输出规则需求 → 不适用，记负向。
- 维度5 文档时效：模块加载指南引用的 18 个文件全部真实存在，README 路径一致 → 已一致。
- 维度6 一致性（stats/schema）：SKILL.md 与 progress-schema.json 的 stats、userConfig、dialogueState 字段完全对齐 → 已一致。
- 维度1 基础持久化：progress.json 不存在→onboarding、损坏→.bak 重建、resume 主路径合理 → 已一致（细化见 D3）。
- roadmap levelOffset(0/1/3) 与 SKILL.md 第九节阶段起点、onboarding.md 映射三方一致 → 已一致。

## 四、修复方案（见 SKILL.md 相应 Edit）
- D1：第十节新增「模块完成度触发映射表」，为 5 个缺失模块补齐 completed 触发/派生规则。
- D2：危机词表扩充 + crisis 处理器加语义兜底。
- D3：Onboarding 规则明确「每收集一问答即写盘 tempData+step」。
- D4：crisis 处理器分层（先共情判断计划/意图，分层播资源）。
- D5/D7：unknown 处理器加跨域拒绝引导 + 空输入提示。
- D6：group_meeting 明确「周→主题阶段」映射表。
- D8：analyze_dialogue 加保真声明。

## 五、修复后验证（Step 5 部分）
- 修复后重读各段确认结构未被破坏，触发映射与 roadmap modules total 上限一致。
- 集成回归在 R5 统一执行。
