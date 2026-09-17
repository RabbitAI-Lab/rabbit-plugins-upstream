# R4 缺陷报告 · 组队系统深度走查

**轮次**：R4（第 4 轮）
**测试焦点**：team-learning 模块 + group 字段读写 + group_meeting/group_review 处理器 + 组队里程碑
**前置版本**：v1.0.3
**修复后版本**：v1.0.4

## 基线核查
- team-learning.md 内容完整（三种模式 / 21 主题库 / 90 分钟模板 / 三明治法 / 复盘模板 / 避坑 / 找伙伴）。
- progress-schema.json 的 group 字段结构完整（memberCount/meetings/streak/lastTopic/nextTopic/members/openIssues/reports），但为 optional（不在 required）。
- milestones.md 定义了 g1/g2 组队专属里程碑，但标注"仅 team 模式初始化"。

## 缺陷清单

### D13（P1，功能性）Onboarding 未初始化 group 字段
- **现象**：第四问收集"单人/组队"后，收尾（SKILL.md:117）只初始化 modules/milestones/dialogueState，**从未写 `group` 对象**。group 在 schema 中是 optional，team 用户 progress.json 可能无 group。
- **影响**：group_review 处理器要更新 group.meetings/streak，对象不存在时 AI 须临时创建，行为不确定；progress_query 聚合 group 易错。
- **修复**：Onboarding 收尾补「组队模式初始化」——mode=team 时初始化完整 group 对象（默认 memberCount=2 对子）；mode=solo 不建 group。

### D16（P1，功能性）g1/g2 里程碑不随 team 初始化（合并于 D13）
- **现象**：roadmap.json 的 milestones 仅含 m1–m10，无 g1/g2；Onboarding 按 roadmap 初始化，team 用户永不获得 g1/g2。
- **影响**：「铁军小组」「完成 10 次组会」里程碑永不点亮，组队激励失效。
- **修复**：Onboarding 收尾 mode=team 时向 milestones[] 追加 g1/g2（reached:false）。

### D14（P2，逻辑矛盾）周计划组会附加限 currentWeek>=13
- **现象**：周计划算法（SKILL.md:329）"mode=team 且 currentWeek>=13 → 加一次组会"，与 team-learning 21 主题库"1–12 周入门启蒙有主题"、group_meeting 处理器"1–12 周选入门主题"直接矛盾。
- **影响**：早期（1–12 周）组队用户周计划不提醒组会，被漏掉组队引导；手动开组会虽可行，但计划层不一致。
- **修复**：改为 mode=team 每周都含可选组会提醒，主题随周次按阶段映射升级。

### D15（P2，健壮性）group_review 缺解析/计算权威规则
- **现象**：处理器（SKILL.md:284-289）仅写"解析复盘→汇总→更新 group"，无：streak 计算规则、reports[] 结构定义、解析失败引用模板。
- **影响**：AI 解析自由文本复盘时易不更新 streak、不追加结构化 report、解析失败时不引导用模板。
- **修复**：补全——提取字段清单、streak 满勤+1/未满清零权威规则、reports[] 对象结构、openIssues 同步、解析失败贴 team-learning.md 第四节模板。

### D17（P3，一致性）里程碑检测时机漏 group_review
- **现象**：milestones.md 检测时机列了 learn_theory/do_practice/analyze_dialogue/self_assess/weekly_review/progress_query，**无 group_review**。
- **影响**：group_review 后 g1/g2 不被检查，铁军里程碑即便达标也不祝贺。
- **修复**：检测时机加 group_review。

### D18（P3，健壮性）progress_query 聚合 group 无容错
- **现象**：progress_query 步骤"聚合 stats/modules/group"，solo 用户无 group 时未说跳过。
- **修复**：明确"仅当 group 存在且 mode=team 纳入，缺失则跳过不报错"。

### D19（P3，一致性）change_config 模式切换未处理 group
- **现象**：change_config 文件规则只说"更新 userConfig；重置 modules"，未提 team↔solo 切换时 group 怎么办（"不想组队了"是已列触发词）。
- **修复**：补 team→solo 保留历史置 mode=solo；solo→team 按 Onboarding 补齐 group 与 g1/g2。

## 修复汇总
| 缺陷 | 严重度 | 状态 |
|------|--------|------|
| D13 组队未初始化 group | P1 | ✅ |
| D16 g1/g2 未初始化 | P1 | ✅（并入 D13） |
| D14 组会附加限 >=13 | P2 | ✅ |
| D15 group_review 规则缺 | P2 | ✅ |
| D17 里程碑检测漏 group_review | P3 | ✅ |
| D18 progress_query 容错 | P3 | ✅ |
| D19 change_config 模式切换 | P3 | ✅ |

## 遗留/下轮
- R5：Phase3 智能增强（对话分析透镜、概念闪卡、案例库）可用性 + 集成回归 + 边界用例（危机中断恢复、跨域拒绝、空输入、进度读写不覆盖）。
