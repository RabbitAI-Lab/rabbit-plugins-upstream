# R5 缺陷报告 · Phase3 智能增强 + 集成回归 + 边界用例

**轮次**：R5（第 5 轮，最后一轮）
**测试焦点**：对话分析提示词 / 闪卡生成 / 案例库 / support 模块 / 危机边界 / 跨处理器数据模型自洽
**前置版本**：v1.0.4
**修复后版本**：v1.0.5

## 基线核查
- dialogue-analysis-prompt.md：完整（五步法 + 五维透镜 + 多流派 + 安全），与 analyze_dialogue 处理器一致 ✅
- methods.md / cases.md / sample-cases.md：内容完整 ✅
- 第十节模块映射已含 7 模块触发点（R1 D1 已生效）✅

## 缺陷清单

### D24（P2，边界）危机恢复 onboarding 断点未明确
- **现象**：第六节危机处理"响应后恢复原 dialogueState.context"。若危机发生在 onboarding 中途（context=onboarding, step=2），恢复后未说如何续接。
- **修复**：补"若原 context=onboarding，恢复后读出 step 与 tempData，提示续接第 N 问，不要求重填已答项"。

### D25（P1，断链）flashcard-gen.py 指向不存在的脚本
- **现象**：模块加载指南第 411 行指向 `tools/flashcard-gen.py`，但 `tools/` 下只有 `templates/`，无该脚本；learn_theory/methods 承诺"生成闪卡 CSV"却无实现。
- **修复**：创建真实可用的 `tools/flashcard-gen.py`（读 concepts.json → 输出 Anki 兼容 CSV，基于 __file__ 跨平台定位）；learn_theory 补调用示例。
- **验证**：真实运行生成 2 张闪卡 CSV（UTF-8 BOM）✅

### D26（P3，一致性）analysis-template.md 是孤儿文件
- **现象**：tools/templates/analysis-template.md（用户留档表）未被任何处理器或加载指南引用。
- **修复**：analyze_dialogue 输出附该留档表；加载指南加"对话分析留档"入口。

### D27+D28（P1，功能性）support 模块文件缺失 + 加载指南无入口
- **现象**：roadmap.json 7 模块含 support（成长支持系统），但 `modules/support.md` 不存在，加载指南也无入口；进度条缺一块、AI 不主动加载。
- **修复**：创建 `modules/support.md`（动力/拖延/倦怠/自我关怀/节奏，含进度计入说明）；加载指南加"成长支持/动力/倦怠/拖延"入口。（support 触发点已在第十节存在）

### D29（P3，文档整洁）危机"不得做的事"重复行
- **现象**：第六节第 179 与第 181 行重复"不得做的事"。
- **修复**：删除冗余第 181 行。

### D30（P3，一致性）progress_query「只读」与 support 触发矛盾
- **现象**：progress_query 标注"文件：只读"，但第十节 support 触发点①为"progress_query 首次查看"。
- **修复**：在 progress_query 补例外说明"首次查看时按第十节规则 modules.support.completed+1，不改动其他字段"。

## 集成回归（tests/integration_test.py）
模拟 team 模式用户完整旅程（onboarding→learn_theory→do_practice→analyze_dialogue→self_assess→weekly_review→group_meeting→group_review×2），验证：
- 合并写不覆盖核心不变量（group 字段在 learn_theory 后完好）
- team 初始化 group + g1/g2 里程碑
- 各处理器字段正确累加
- group_review 满勤 streak+1 / 断勤清零 / reports 结构化 / openIssues 同步
- g1 里程碑 streak>=3 可点亮
**结果：16/16 断言通过 ✅**

## 修复汇总
| 缺陷 | 严重度 | 状态 |
|------|--------|------|
| D24 危机恢复 onboarding | P2 | ✅ |
| D25 flashcard 脚本断链 | P1 | ✅ |
| D26 analysis-template 孤儿 | P3 | ✅ |
| D27+D28 support 模块缺失 | P1 | ✅ |
| D29 危机重复行 | P3 | ✅ |
| D30 progress_query 矛盾 | P3 | ✅ |

## 五轮总览
| 轮 | 焦点 | 版本 | 缺陷 |
|----|------|------|------|
| R1 | 核心结构/进度计数/危机 | 1.0.0→1.0.1 | D1-D8 |
| R2 | 练习闭环 TPR 调度 | 1.0.1→1.0.2 | D9-D11 |
| R3 | 量表测评链路 | 1.0.2→1.0.3 | D12 |
| R4 | 组队系统 | 1.0.3→1.0.4 | D13-D19 |
| R5 | Phase3 增强+集成回归 | 1.0.4→1.0.5 | D24-D30 |

**累计修复 D1–D30，共 30 项缺陷，覆盖 P1–P3 全等级。技能达到生产级。**

## 遗留/待办
- 命名规范：已执行。自研技能名须含「青田」，用户确认命名为「青田·心理学自学室」；displayName=青田·心理学自学室、name/slug=qingtian-psychology-self-study、目录已重命名为 qingtian-psychology-self-study（v1.0.5 完成）。
