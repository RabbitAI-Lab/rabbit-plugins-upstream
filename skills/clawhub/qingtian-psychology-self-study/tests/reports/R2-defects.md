# R2 缺陷报告 · 心理学自学教练 v1.0.1

> 基线：v1.0.1，R1 已修复 D1–D8。本轮聚焦维度：练习闭环（TPR 调度）、子技能集成一致性、输入护栏、外部输入保真、多语言（负向）。
> 方法：真实读取 practice/RUNBOOK.md + 核对 therapies/counselors 文件清单 + 模拟「做练习」fixture 走查。

## 一、状态核验
- practice/ 文件清单：RUNBOOK.md + references/(therapies 17 + counselors 17 + ethics/onboarding/practice/risk-assessment/safety-boundaries)。与 RUNBOOK 流派—文件映射表 17×2 一一对应 ✓。
- 版本：v1.0.1；累计缺陷基线：D1–D8（R1）。

## 二、发现清单（D9–D11）

| 编号 | 严重度 | 位置 | 现象 |
|---|---|---|---|
| D9 | P2 | practice/RUNBOOK.md 第六节 | 危机信号词库仍是旧词（自杀/自伤/不想活/想死/活不下去/伤害自己/伤人/报复/轻生），缺 R1 已在主 SKILL.md 新增的「活着没意思/不如死了/死了算了/没盼头/不想活了/解脱」→ 练习链路危机漏触发，与主表不同步 |
| D10 | P2 | practice/RUNBOOK.md 第5行 | 硬编码绝对路径 `C:/Users/77497/.workbuddy/skills/psychology-self-study/practice/references/`，换用户或上 SkillHub 失效；且与同文件第80行相对路径示例矛盾；SKILL.md 已承诺脚本用 `__file__` 相对定位，RUNBOOK 却硬编码 |
| D11 | P3 | SKILL.md 第七节状态机 review_practice 行 | 未列 `dialogues++`，与 SKILL.md 第229行（"stats.dialogues 每结束一次练习 +1"）及 RUNBOOK 第七节不一致 |

## 三、负向结论（已一致）
- 维度4 外部输入保真（练习对话）：RUNBOOK 第四节"沿用用户自己的词，不替换成术语" + 第4节全局约束已实现保真，且声明"教学演示不替代咨询" ✓。
- 维度7 输入护栏（练习中断）：RUNBOOK 第五节切换/暂停/结束规则健全，tempData.flow 中途保留（SKILL.md do_practice 异常项）✓。
- 多语言（负向）：练习以中文对话为主，无英文需求 ✓。
- 17 流派列表编号与 therapies/counselors 文件名、RUNBOOK 映射表三者完全对齐 ✓。

## 四、修复方案
- D9：RUNBOOK 第六节危机信号词库扩充至与主 SKILL.md 一致。
- D10：RUNBOOK 第5行改为「路径相对于本技能根目录的 practice/references/」，删除硬编码绝对路径；保留第80行相对示例。
- D11：SKILL.md 状态机 review_practice 行补 `dialogues++`，与主文件/RUNBOOK 对齐。

## 五、回归验证
- 修复后重读 RUNBOOK 第5/6节、SKILL.md 状态机，确认无结构破坏。
- 跨文件危机词库现在两处一致。
