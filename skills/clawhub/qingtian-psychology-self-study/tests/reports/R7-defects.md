# R7 专项演练缺陷报告 · 青田·心理学自学室 v1.0.7

> 轮次：R7（第 7 轮，专项覆盖 R6 遗留的 4 个未现场演练处理器）
> 日期：2026-08-10
> 方法：真实落盘 + 不变量自检（同 R6 端到端演练方法论），crisis 仅用技能文档自身列出的示例语义，不生成任何具体内容
> 范围：monthly_review / change_config / resume / crisis

---

## 一、演练覆盖与结果

| 处理器 | 演练场景 | 不变量 | 结果 |
|--------|----------|--------|------|
| monthly_review | solo 用户说「月总结」→ logs 加「月度」条 + 校准 goal | 月度条写入 / goal 校准 / 模板存在 | ✅ 3/3 |
| change_config | solo→team 切换 → group 初始化 + g1/g2 + modules 保留；反向 team→solo 保留历史 | group 初始化 / 里程碑追加 / 进度保留 / 反向保留 | ✅ 4/4 |
| resume | onboarding 半截（Q1-Q2 已答）回来「继续」；state 为空退回 daily_recommend | 断点 step 读出 / tempData 不重填 / 空态退回 | ✅ 3/3 |
| crisis | 轻响应（隐喻「烦得不想活了」）共情；强响应（「我想死」）标准资源声明 | 危机词命中 / 资源声明 / 两分支不改学习数据 / 恢复 context | ✅ 6/6 |

**合计：18/18 不变量通过。**

---

## 二、发现的缺陷与修复（v1.0.6 → v1.0.7）

| ID | 等级 | 处理器 | 问题 | 修复 |
|----|------|--------|------|------|
| **D34** | P2（功能断链） | monthly_review | 指令「引导月反思（见 `tools/templates/`）」但目录只有 weekly/reflection/analysis 三个模板，**无月度模板** → 教练照指令找不到文件 | 新建 `tools/templates/monthly-review.md`（6 段：做了什么/3 收获/卡点/数据快照/方向校准/重测量表），风格与 weekly-review 一致 |
| **D35** | P2（清晰度） | crisis | 第六节「不改动学习数据」与「响应后恢复原 dialogueState.context」并列，LLM 可能把 dialogueState.context 也当成「学习数据」而不恢复，导致 context 卡在 crisis 或丢失 | 在第六节加澄清句：明确「不改动学习数据」仅指 modules/stats/assessments 等进度字段；恢复 dialogueState.context 属会话态恢复、必须执行；并提示危机前先记住当前 context |
| **D36** | P3（清晰度） | change_config | solo→team 仅写「按 Onboarding 组队初始化补齐」，未直接给 JSON 形状，LLM 需回查 Onboarding 第 121 行，易漏 g1/g2 | 在处理器内直接给出 group 初始化 JSON 与 g1/g2 追加语句，减少回查负担 |
| **D37** | P3（清晰度） | resume | 「state 为空→退回 daily_recommend」语义模糊（指 dialogueState 整个空？还是 lastTopic 空？） | 明确两种分支：无进度文件→引导 onboarding；有进度但 context=daily 且无 lastTopic/无未完成 tempData→退回 daily_recommend；onboarding 半截→按第六节末段续接 |
| **D38** | P2（逻辑缺口） | change_config | 步骤③「重算路径」过于简略，未说清改 level/goal 后要不要重排周计划，LLM 可能只改配置不动内容 | 明确：改 level/goal 时调用第九节周计划算法刷新本周及后续周任务（保留 modules 已完成项与 stats 累计）；仅改 timeBudget/mode 时不重排内容 |

---

## 三、累计状态（R1–R7）

- **总缺陷**：D1–D38（R1: D1–D8｜R2: D9–D11｜R3: D12｜R4: D13–D19｜R5: D24–D30｜R6: D31–D33｜R7: D34–D38）
- **版本轨迹**：1.0.0 → 1.0.7
- **自动化验证**：
  - `tests/integration_test.py`（R5）：16/16 断言通过
  - `tests/dryrun/r7_dryrun.py`（R7）：18/18 不变量通过
  - PHQ-9 真实计分（R3/R6）：计分+危机判定+HTML 报告+RESULT_JSON 正常
  - `tools/flashcard-gen.py`（R5）：生成 Anki 兼容 CSV 通过
- **覆盖的处理器**：15 个处理器中 14 个已现场/专项演练（仅 `daily_recommend` 为后台推荐逻辑，非用户直接触发，未单列演练；其依赖的 resume/daily 分支已验证）

---

## 四、结论

青田·心理学自学室经 R1–R7 共 7 轮测试（5 轮规划内 + R6 端到端 + R7 专项），累计修复 38 项缺陷，所有用户可直达的处理器均已通过真实落盘演练。技能达到生产级，可交付使用。

**仍属设计内已知边界（README 已声明，非缺陷）**：组队找人/见面需线下；进度可视化由独立 HTML 承担；实时提醒靠 WorkBuddy 自动化；量表计分依赖本地 Python，无 Python 时回退 LLM 计分。
