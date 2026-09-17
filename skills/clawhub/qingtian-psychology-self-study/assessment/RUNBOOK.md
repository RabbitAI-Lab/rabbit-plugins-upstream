# 测评引擎运行手册（集成 心理量表测评系统）

> 本文件是「心理学自学 Skill」内部运行测评模块的指挥中心。它是心理量表测评系统的**内嵌版**——21 个量表 JSON（19 个标准量表 + PHQ-2/GAD-2 两个快速筛查量表）、通用计分引擎、报告生成器已随技能复制在 `assessment/` 下，无需外部加载即可原生运行。
>
> **本模块根目录（相对本 Skill）**：`assessment/`
> - 量表数据：`assessment/scales/<id>.json`
> - 计分引擎：`assessment/scripts/scoring_engine.py`
> - 报告生成：`assessment/scripts/report_generator.py`
> - 安全护栏：`assessment/references/safety_protocol.md`（最高优先级）
>
> ⚠️ **可移植性约定**：下方命令中的脚本路径**不要硬编码绝对路径**。请使用本 Skill 的安装根目录变量（如 `<SKILL_ROOT>/assessment/scripts/score_and_report.py`），或直接用相对路径 `assessment/scripts/score_and_report.py`。脚本内部已基于 `__file__` 自动定位 `scales/` 与同目录的计分/报告引擎，**在 Windows / Linux / SkillHub 环境下均可运行**，无需修改源码。

---

## 一、启动引导语（用户输入「自测/测一下/量表名」时首先输出）

> 👋 我们来做个自评筛查。
> 最近有什么让你困扰的状态吗？比如睡不好、情绪低落、压力大、容易焦虑……说说看，我帮你推荐合适的量表。
> 如果目标明确，也可以直接说量表名（如 PHQ-9、GAD-7、MAAS），我们立刻开始。
> ⚠️ 这是**自评筛查，不是诊断**，结果仅供参考，不替代专业评估。

输出引导语后**不要直接出题**，等待用户选择或指明量表。

---

## 二、量表库（21 个，按领域分类）

> **快速筛查优先**：用户状态模糊或时间紧张时，先推 PHQ-2（抑郁）与 GAD-2（焦虑），各 30 秒；总分 ≥3 提示阳性 → 建议继续完成完整 PHQ-9 / GAD-7。

| 领域 | 量表（id） | 题数 | 备注 |
|------|-----------|------|------|
| 抑郁(快速) | PHQ-2 | 2 | 快速初筛，≥3 建议上 PHQ-9 |
| 抑郁 | PHQ-9 | 9 | 含自杀意念筛查题（q9），触发即危机护栏 |
| 抑郁(中国常模) | SDS | 20 | 10 题反向，标准分 ×1.25 |
| 焦虑(快速) | GAD-2 | 2 | 快速初筛，≥3 建议上 GAD-7 |
| 焦虑 | GAD-7 | 7 | — |
| 焦虑(中国常模) | SAS | 20 | 5 题反向，标准分 ×1.25 |
| 压力 | PSS-10 | 10 | 4 题反向 |
| 睡眠 | PSQI | 19→7成分 | 成分分求和，>7 为差（JSON 为 7 成分简化版，见 description） |
| 正念 | MAAS | 15 | 题目负向，计分方向已内置 |
| 正念 | FFMQ | 39 | 5 因子，含反向 |
| 自尊 | Rosenberg | 10 | 5 题反向 |
| 情绪 | PANAS | 20 | 积极/消极两维 |
| 生活满意 | SWLS | 5 | 7 点 |
| 抑郁(社区) | CES-D | 20 | 4 题反向 |
| 心理韧性 | CD-RISC | 10 | 5 点 |
| 职业倦怠 | MBI | 22 | 3 维度 |
| 综合症状 | SCL-90 | 90 | 9 因子+附加 |
| 社会支持 | SSRS | 10 | 3 维度 |
| 注意缺陷 | ASRS | 6 | 官方计数计分：每题≥2 计阳性，≥4 题阳性提示 |
| 依恋 | ECR | 36 | 焦虑/回避两维，反向 |
| 网络成瘾 | IAT | 20 | 5 点，划界分 |

> 按阶段推荐：启蒙期 PHQ-9/GAD-7/PSS-10；基础期加 MAAS/Rosenberg/SWLS；整合期加 ECR/MBI/SCL-90；详见 `modules/assessment.md`。

---

## 三、题目呈现方式

**默认：逐题可点击**（选项 ≤ 4 时）。每轮只出**一道题**，用可点击卡片（在本环境用 AskUserQuestion 渲染）让用户点选；选中即取该选项序号（0 起）。
**批量模式**：用户说「全部列出/批量」，或某题选项 > 4、或题量极大（如 SCL-90 90 题）→ 一次性列出全部，接受 `1-A 2-B 3-C` 或 `q1:2` 紧凑作答。

每题读出 `items[].text`，选项即 `options[].label`。**作答取选项序号（0 起），不是分值**——引擎内部按 `options[].score` 换算。

---

## 四、计分与报告（核心步骤）

收集完作答后，将 `answers` 写成 JSON（形如 `{"q1":2,"q2":0,...}`），然后运行**通用计分引擎 + 报告生成器**：

```bash
# 在用户工作区执行（cwd 为用户工作区）；<SCALE_ID> 如 PHQ-9
# <SKILL_ROOT> 为本 Skill 的安装根目录（不要写死绝对路径，跨平台/跨机器应使用该变量）
python3 "<SKILL_ROOT>/assessment/scripts/score_and_report.py" <SCALE_ID> <ANSWERS_JSON_PATH> <OUT_DIR>
```

> 上述 `score_and_report.py` 为集成封装脚本（见下方第五节），它 import 同一目录的 `scoring_engine` 与 `report_generator`，完成「读量表→计分→生成 HTML→保存到 OUT_DIR」。`<OUT_DIR>` 建议为工作区的 `reports/assessment/`。

**输出**：
- 对话中先给要点摘要（各维度原始分/标准分/分级）；
- 若 `crisis_flag == true` → **先于分数**插入求助资源（见 `assessment/references/safety_protocol.md`）；
- HTML 报告保存到 `<OUT_DIR>/<id>_report_<时间戳>.html`，并用预览/浏览器打开；
- 询问是否保存到本地（默认已存本地 `reports/assessment/`）。

---

## 五、集成封装脚本 score_and_report.py

在 `assessment/scripts/` 新建 `score_and_report.py`（与本手册配套），内容：

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""集成封装：读量表 → 计分 → 渲染 HTML 报告 → 保存到指定目录。
用法：python3 score_and_report.py <SCALE_ID> <ANSWERS_JSON> <OUT_DIR>
"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from scoring_engine import load_scale, score
from report_generator import render, save

def main():
    if len(sys.argv) < 4:
        print("Usage: python3 score_and_report.py <SCALE_ID> <ANSWERS_JSON> <OUT_DIR>"); sys.exit(1)
    sid, ans_path, out_dir = sys.argv[1], sys.argv[2], sys.argv[3]
    scale = load_scale(sid)                       # 大小写/连字符容错
    with open(ans_path, "r", encoding="utf-8") as f:
        answers = json.load(f)
    result = score(scale, answers)
    # 先打印要点摘要
    print("=== 计分结果 ===")
    for dim, val in result.get("dimension_scores", {}).items():
        std = result.get("standard_scores", {}).get(dim, "—")
        print(f"  {dim}: 原始分 {val} | 标准分 {std} | 分级 {result.get('bands', {}).get(dim, '—')}")
    if result.get("crisis_flag"):
        print("⚠️ 危机标志触发，请先于分数展示求助资源（见 safety_protocol.md）")
    os.makedirs(out_dir, exist_ok=True)
    path = save(scale, result, out_dir=out_dir)   # save() 已渲染 HTML
    print(f"HTML 报告已保存：{path}")
    # 同时回吐 result JSON 供本 Skill 记录进度
    print("RESULT_JSON>>>" + json.dumps(result, ensure_ascii=False))

if __name__ == "__main__":
    main()
```

> 调用方（自学 Skill 的 `self_assess` 处理器）读取 `RESULT_JSON>>>` 后的 JSON 写入 `progress.json` 的 `assessments[]` 与 `stats.assessments++`。

---

## 六、安全护栏（最高优先级，不可关闭）

详见 `assessment/references/safety_protocol.md`（与 `references/scale_authority.md` 版权声明）。要点：
1. **危机优先**：含自杀意念筛查题（如 PHQ-9 第 9 题）一旦触发 `crisis_flag=true`，**先于分数**显示求助资源。
2. **热线与情绪急救包单源**：求助资源一律取自 `resources/crisis-resources.md`（本技能唯一数据源），HTML 报告由 `report_generator.py` 解析该文件；修改热线只改单源。
3. **不诊断**：自评筛查 ≠ 诊断，引导至专业评估。
4. **不推荐药物**：涉及用药一律引导处方医生。
5. **年龄门槛**：成人量表对未成年人提示需监护人在场。
6. **隐私**：报告仅存本地；涉及敏感数据提示脱敏。
7. **版权**：每份量表 JSON 已标注来源与授权范围（见 `scale_authority.md`）。

---

## 七、与自学 Skill 的衔接

- `self_assess` 处理器：读本 RUNBOOK → 输出引导语 → 选量表 → 出题收集 → 调封装脚本计分+出报告 → 将 `RESULT_JSON` 写入 `progress.json`（`assessments[]` 追加：id、日期、各维度分、分级、报告路径；`stats.assessments++`）。
- 测评后建议用户写一句「这次分数让我注意到 ______」，纳入 `weeklySummary` 素材（见 `modules/assessment.md`）。
- 月度反思时重测同一量表可对比趋势（progress.json 的 `assessments[]` 已按时间保存）。
