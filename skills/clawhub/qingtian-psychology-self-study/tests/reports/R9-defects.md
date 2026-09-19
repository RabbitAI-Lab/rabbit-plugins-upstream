# R9 缺陷报告（2026-09-09 · 交付 v1.3.0）

> 本轮为「深度审查 + 全量完善」轮次：对 v1.2.0 全项目执行静态检查、全量表数据审计、定向计分验证与 GitHub 同类项目调研，并据此完成立即修复、短期增强与中长期进化三档改造。
> 关联：`../审查报告-2026-09-09.md`（逐项证据与借鉴来源）；`tests/run_all.py`（一键全量回归）。

## 1. 本轮发现并修复的问题（D41 起）

| ID | 级别 | 问题 | 修复 |
|---|---|---|---|
| D41 | P2 | ASRS 计分法与官方标准不符：文档称"≥4 项阳性"，实现为求和法，两者不等价 | `scoring_engine.py` 新增 `method:"count"` 计分模式（item 阈值计数）；ASRS.json 改为官方口径（每题 ≥2 计阳性，≥4 项阳性提示）；`scale_authority.md`/`RUNBOOK.md` 同步说明 |
| D42 | P2 | 里程碑 m4 条件两处定义不一致（roadmap.json=analyses，milestones.md=dialogues） | `milestones.md` m4 改为 `stats.analyses>=1`；`progress-tracker.md` 注明 dialogues 与 analyses 语义 |
| D43 | P2 | 组队会议纳入周计划的周次规则三处冲突（onboarding ≥13 周 / SKILL 每周 / week-plans 13-20） | 统一为「team 模式每周含可选组会提醒（早期 🌱入门启蒙，13 周起正式主题）」：`onboarding.md`、5 个 week-plans 模板同步 |
| D44 | P3 | Rosenberg 边界文档冲突（15 分归属）、SWLS 边界冲突（20 分归属） | `scale_authority.md` 与 JSON bands 对齐（Rosenberg 10-15 偏低 / 16-25 正常 / 26-40 较高；SWLS 5-14/15-19/20-24/25-35） |
| D45 | P3 | `modules/assessment.md` 兜底题称 Rosenberg"4 道反向计分"，实际 5 题 | 改为 5 题 |
| D46 | P3 | 版本可追溯性回退：v1.2.0 无对应测试报告 | 本轮交付 v1.3.0 + 本报告；新增 `tests/run_all.py` 一键全量入口 |
| D47 | P3 | `report_generator.py` 标准分注释硬编码"×1.25" | 改为从 `standard_score.slope` 动态生成 |
| D48 | P3 | SKILL.md §8 self_assess 步骤 ⑥⑦ 内容重复 | 合并为一步 |
| D49 | P3 | 状态机 context"analyze"与处理器名"analyze_dialogue"不一致 | §7 状态机统一为 `analyze_dialogue` |
| D50 | P3 | `safety_protocol.md` 残留 C-SSRS/PCL-5 引用（量表库无此二者） | 改述为"如未来接入时" |
| D51 | P3 | `book-list.json` L4 作者 " Baron"（疑拼错/缺中文名） | 改为「阿伦（Aron）」（经典心理统计学教材作者） |
| D52 | P3 | `__pycache__` 与干跑产物混入源码目录 | 新增 `.gitignore` |
| D53 | P3 | 测试缺口：反向/危机/标准分/ASRS count 无自动化用例；无统一测试入口 | 新增 `tests/test_scoring_cases.py`（7 组 40+ 断言）+ `tests/run_all.py` |
| D54 | P3 | advanced 起点文案未提及流派阶段也被跳过 | SKILL.md §9 与 `advanced-standard.md` 补全"跳过启蒙、流派、领域" |
| D55 | P3 | `progress-tracker.md` 把练习与对话分析混写，未列 analyses | 拆为独立行并补 m4 语义备注 |
| D56 | P3 | 快速筛查缺失、认知记录/情绪打卡/备份等能力缺失 | 见下方新增能力清单 |

## 2. 新增能力（v1.3.0）

- **计分引擎**：`sum / average / count` 三模式；`standard_score` 注释动态化。
- **量表库 19 → 21**：新增 PHQ-2、GAD-2 快速筛查（≥3 阳性提示 → 建议上完整量表）。
- **危机单源化**：新增 `resources/crisis-resources.md`（热线唯一数据源 + 情绪急救包：4-7-8 呼吸、5-4-3-2-1 落地、STOP、渐进放松、自我对话脚本）；`report_generator.py` 解析该文件渲染热线（解析失败回退内置常量）；`safety_protocol.md`、`scale_authority.md`、`dialogue-analysis-prompt.md` 统一指向单源。
- **认知记录卡**：`modules/thought-diary.md` + `thought_record` 处理器（五栏模板 + ANTs 清单 + 苏格拉底式引导）；计入 counseling 模块（total 4→5）。
- **情绪打卡**：`mood_check` 处理器 + `moodLog[]`（mood/energy 1-5 + note，同日覆盖）；周回顾聚合趋势。
- **XP/徽章/等级**：10 类活动 XP 表、6 级等级、8 枚徽章；`stats.totalDays` 去重计数规则。
- **learnerProfile 画像层**：学习风格/反复卡点/动力状态/常用流派，周回顾更新、每日推荐个性化。
- **RAG 接地**：learn_theory 输出带 `modules/*.md` 出处标注，超范围内容声明为通用知识并建议核实。
- **认知歪曲标签层**：对话分析提示词新增 ANTs 标注步骤。
- **渐进暴露模板**：`modules/exposure.md` + `exposure` 处理器（SUDS 层级 + 安全边界）。
- **进度备份**：`tools/progress-backup.py` export/import + `export_progress`/`import_progress` 意图。
- **报告 PDF 提示**：HTML 报告 footer 加 Ctrl+P 另存为 PDF 指引。
- **前置知识检查**：`roadmap.json` 各阶段新增 `prerequisites`，周计划生成时自评提示。
- **分发元数据**：`manifest/manifest.json`（与 SKILL.md version 对齐 1.3.0）。

## 3. 验证

- `tests/test_scoring_cases.py`：7 组用例（反向/危机两路径/标准分/ASRS count/快速筛查/21 量表结构+冒烟+位置键/报告渲染与热线单源）——全部通过。
- `tests/integration_test.py`：v1.3.0 新字段不变量（counseling total=5、moodLog 覆盖、xp/totalDays、learnerProfile、合并写不覆盖）——通过。
- `tests/run_all.py`：一键全量 5/5 通过（test_scoring_cases + integration_test + build_dryrun + r7_dryrun + r8_multidim）。
- 全量表数据审计（21 个）：结构/bands/危机引用/位置键冒烟 全部通过。

## 4. 遗留与建议

- 17 流派 therapy/counselor 内容文件的**逐流派内容口径审查**未在本轮覆盖（内容量大），建议作为 R10 主题。
- `学习进度汇总.html` 未随项目提供（README 声明独立），其 localStorage 导入可在 Phase 2 接入 `progress-backup.py` 导出产物。
- 若未来分发到多平台（Claude/Copilot 等），需由 manifest 单源生成各平台格式并在 CI 校验（当前仅提供单源，见 `manifest/README.md`）。
