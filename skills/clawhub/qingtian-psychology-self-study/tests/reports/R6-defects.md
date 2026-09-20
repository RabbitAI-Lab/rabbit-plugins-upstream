# R6 端到端对话演练缺陷报告 · 青田·心理学自学室 v1.0.5→1.0.6

## 背景
应要求做**真·端到端对话演练**（单人主链路）：以教练身份按 SKILL.md 指令真实陪一个虚拟新用户走完 Onboarding→日常循环→周回顾，并**真实落盘** `progress.json`、练习个案报告、PHQ-9 测评产物，验证"指令能否被忠实执行"这一此前五轮测试未覆盖的缺口。

## 演练覆盖的处理器（8 个）
onboarding · daily_recommend · learn_theory · do_practice · analyze_dialogue · self_assess · weekly_review · progress_query
（team 模式 + 状态机已在 R4 集成测试 `integration_test.py` 覆盖；本论聚焦单人主链路真实跑通。）

## 发现并修复的缺陷

### D31（P1）答案 JSON 形状缺失 + 引擎静默失败
- **现象**：SKILL.md `self_assess` 仅写"取选项序号 0 起"，未规定 answers 的 JSON 形状。教练极易生成 `{"answers":[0,1,...]}` 这类错误格式。封装脚本 `score_and_report.py` 对缺题**静默放行**：退出码 0、仍渲染出"无分数"的空白 HTML 报告，用户完全无感知。
- **证据**：演练初版用 `{"answers":[...]}` 跑 PHQ-9，`RESULT_JSON` 显示 `missing_items:["q1".."q9"]`、`complete:false`、无总分。
- **修复**：
  1. SKILL.md `self_assess` 第④⑤步明确形状：`{"q1":<序号>,"q2":<序号>,...}`（键为题号 q1..qn，值与量表 items 顺序一致，0 起）。
  2. `score_and_report.py` 增加完整性校验：缺题即向 stderr 输出"❌ 作答不完整：缺少题目 q1..qn"并 `sys.exit(2)`，**不再生成误导报告**。

### D32（P2）RESULT_JSON 无顶层 total/level
- **现象**：`RESULT_JSON` 不含 `total`/`level` 字段，分数存于 `dimension_scores`（按维度）与 `bands`。教练照"解析末行 RESULT_JSON 写进度"取不到分数。
- **修复**：SKILL.md 第⑦步说明——多数量表为**单维度**，取 `dimension_scores` 唯一维度名下的分值作 total、`bands` 同名键作 level（例：PHQ-9 → `total=dimension_scores['抑郁总分']`，`level=bands['抑郁总分']`）；多维度分别记录。

### D33（P2）RESULT_JSON 不含报告路径
- **现象**：教练需在 `assessments[].report` 记录报告路径，但 `RESULT_JSON` 未回吐路径（仅 stdout 打印"HTML 报告已保存：…"）。
- **修复**：`score_and_report.py` 在 `save()` 后写入 `result["report_path"] = path`，随 RESULT_JSON 一并返回。

## 修复后复测（tests/dryrun/build_dryrun.py）
- ✅ D31b 回归：错误格式 `{"answers":[...]}` 现被拒——退出码 **2**、含"作答不完整"。
- ✅ 正确格式 PHQ-9：总分 **3.0** / 分级 **无·极轻度** / `crisis_flag:false` / `complete:true`。
- ✅ 进度文件 **12 项核心不变量全部符合预期**（theory=1, counseling=2, assessment=1, cases=1, support=1, practiceCount/analyses/dialogues/assessments/reflections 各=1, weekCompleted=true, group 在 solo 模式缺失）。

## 演练产物（落盘于 tests/dryrun/，隔离真实用户数据）
- `progress.json` —— 首轮单人链路最终进度
- `reports/practice/case-report-cbt.md` —— TPR 练习个案报告
- `reports/assessment/PHQ-9_report_20260810_121526.html` —— 真实计分 HTML 报告
- `build_dryrun.py` —— 可复跑的演练构建/自检脚本

## 未现场演练（仅静态核验，建议后续补专项）
- `monthly_review` / `change_config` / `resume` / `crisis`：逻辑经走查无误；`crisis` 分层（情绪宣泄 vs 明确意图）在 R1(D2/D4) 已加固。可另开一轮专项演练覆盖。

## 版本
v1.0.5 → **v1.0.6**（新增 D31/D32/D33 修复，结构未变）。
