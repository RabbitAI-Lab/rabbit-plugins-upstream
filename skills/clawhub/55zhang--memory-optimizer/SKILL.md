---
name: memory-optimizer
description: "基于遗忘曲线与间隔复习科学的高效学习与记忆优化计划生成器（Node.js 实现，含可视化图表，与 sleep-optimizer 同系列）。用户输入 memory-optimizer（或 /memory-optimizer）主动调用，或询问任何学习/记忆相关问题（复习计划、背书、遗忘、备考、学习计划、记忆力、考前冲刺等）时自动触发：先按问题框架收集备考阶段与任务目标，再生成含遗忘曲线图、复习调度甘特图和每日学习计划的可执行记忆优化方案"
metadata:
  version: "1.0.0"
  author: "user"
  tags: ["learning", "memory", "study", "spaced-repetition", "forgetting-curve", "exam-prep", "psychology"]
license: "MIT"
user-invocable: true
allowed-tools: ["read", "write", "edit", "exec"]
---

# 记忆与学习优化器 (Memory Optimizer) - 备考阶段增强版

基于遗忘曲线、间隔效应与检索练习等认知科学证据，结合备考阶段特征，生成个性化学习与复习计划，帮助用户实现有效记忆。与同系列 **sleep-optimizer**（睡眠优化器）互补：一个优化夜晚的记忆巩固，一个优化白天的学习安排。

## 核心科学依据

### 记忆与遗忘科学
- **遗忘曲线** (Ebbinghaus, 1885)：记忆随时间指数衰减，R(t) = e^(-t/S)
- **间隔效应** (Cepeda et al., 2006, *Psychological Bulletin*)：分散复习优于集中突击；最佳间隔约为保持期的10-20% (Cepeda et al., 2008, *PNAS*)
- **测试效应/检索练习** (Roediger & Karpicke, 2006, *Psychological Science*)：主动回忆比重复阅读更有效；检索练习优于概念图 (Karpicke & Blunt, 2011, *Science*)
- **学习技术评估** (Dunlosky et al., 2013, *Psychological Science in the Public Interest*)：练习测试与分散练习为高实用性技术；划线/重读为低实用性
- **期望困难** (Bjork, 1994)：适当的难度提升长期记忆效果

### 睡眠与记忆交叉（与 sleep-optimizer 共享）
- **睡眠记忆巩固** (Rasch & Born, 2013, *Physiological Reviews*, IF 37.3)：睡前复习+睡眠巩固是最优组合
- **大学生学习与睡眠** (Lund et al., 2010, *J Adolescent Health*)：睡眠不足直接损害学业表现

## 触发条件

以下任一情况自动触发本技能（无需用户手动指定）：
- 用户输入 `memory-optimizer` 或 `/memory-optimizer`
- 用户询问学习/记忆相关问题：复习计划、怎么背书、总是遗忘、记忆效率低、备考安排、考前冲刺、学习计划制定、四六级/考研/期末复习等
- 用户需要以下帮助时：
  - 制定个性化学习与复习计划
  - 按遗忘曲线安排复习时间点
  - 评估备考任务量是否超载
  - 结合睡眠优化记忆巩固（可联动 sleep-optimizer）

触发后立即执行【工作流程】：先按「数据收集」问题框架逐项询问用户，收集完整后再运行脚本生成报告。

## 输入数据

### 必填
1. **备考阶段**（选择最符合的）：
   - `daily_study` - 日常学习（上课期间保持节奏）
   - `midterm` - 期中备考
   - `final_review` - 期末复习周
   - `exam_week` - 考试周
   - `postgraduate_prep` - 考研备考
   - `civil_service_prep` - 考公备考
   - `certificate_prep` - 证书备考（四六级/教资/计算机等）
   - `skill_study` - 技能学习（编程/语言/乐器等）
   - `thesis_research` - 论文/科研
   - `vacation_study` - 假期自学
2. **距目标/考试天数**（正整数，1-365）
3. **每天可用学习时间**（小时，0-16）

### 必填（任务目标列表，可多项）
每个任务包含：
- **name**：科目/任务名称
- **units**：内容量（数字）
- **unit_type**：单位（章/节/页/词/套题/讲）
- **mastery**：目标掌握度（了解/熟悉/掌握/精通）
- **exam_days**（可选）：该任务距考试的天数，默认=总体天数
- **known**（可选）：初始熟悉度 0-1，默认 0

### 选填
4. **输出文件路径**（可选，`--output 报告.md` 会附带生成 `.chart.svg`）

## 工作流程

### 1. 数据收集
```
询问用户（问题框架，全部问完等用户一次回复）：
- 你目前处于什么备考阶段？（10 项选 1：日常学习/期中备考/期末复习周/考试周/考研备考/考公备考/证书备考/技能学习/论文科研/假期自学）
- 距目标或考试还有多少天？
- 每天能投入多少小时学习？
- 有哪些科目或任务？每个请提供：名称、内容量（几章/几页/多少词…）、目标掌握度（了解/熟悉/掌握/精通）、该科目距考试天数（可选）、目前熟悉程度 0-100%（可选）
```

### 2. 备考阶段适配分析

| 备考阶段 | 推荐每日时长 | 复习占比 | 特殊策略 |
|----------|--------------|----------|----------|
| 日常学习 | 2-4h | 30% | 每周日周回顾 |
| 期中备考 | 3-5h | 40% | 考前2天回归框架 |
| 期末复习周 | 4-8h | 45% | 考前3天快速回顾，睡眠优先 |
| 考试周 | 3-6h | 50% | 考试间隙只过错题要点 |
| 考研备考 | 6-10h | 40% | 每月末全科自测 |
| 考公备考 | 5-8h | 35% | 每周模考+错题本 |
| 证书备考 | 2-5h | 40% | 碎片时间轻量回顾 |
| 技能学习 | 1-3h | 25% | 每周综合串联练习 |
| 论文/科研 | 3-6h | 20% | 每周末文献交叉回顾 |
| 假期自学 | 2-4h | 30% | 开学前1周复盘 |

### 3. 记忆模型与复习调度
- **遗忘曲线**：R(t) = e^(-t/S)，S 由掌握度决定（了解3/熟悉5/掌握7/精通10天）
- **扩张间隔复习**：新学后第 1、3、7、15、31 天复习（Cepeda et al., 2006）；每次复习后记忆强度翻倍，复习时机=保留率约87%时
- **考前3天集中回顾**：考试日临近的任务自动追加一次快速回顾
- **计划容量检查**：总学习量 vs 天数×每日新学容量（55%），超载自动预警

### 4. 生成报告（含可视化）
1. 学习概况评估（任务量、容量检查、风险提示）
2. **记忆可视化**：① 遗忘曲线与间隔复习效果对比 ② 复习调度甘特图（学/复标记）
3. 任务排程明细（每任务新学日+复习日）
4. 备考阶段分析（特征、挑战、推荐投入、定制建议）
5. 每日学习计划（前14天：学什么/复习什么/时长/超时预警）
6. 高效学习策略清单（6 项，附文献出处）
7. 记忆巩固与睡眠联动提示

### 5. 执行脚本生成报告

```bash
node scripts/study_planner.js \
  --stage <备考阶段代码> \
  --days <距考试天数> \
  --hours <每日可用小时> \
  --tasks @任务列表.json \
  [--output 报告.md]
```

> 提示：Windows 命令行传 JSON 引号容易转义出错，`--tasks` 支持 `@文件路径` 写法（如 `--tasks @tasks.json`），推荐在 Windows 下使用。注意 JSON 文件需为 UTF-8 **无 BOM**。
> 使用 `--output 报告.md` 时，会同时生成同名 `报告.chart.svg`（遗忘曲线+复习甘特+每日时长三合一）。

任务列表 JSON 示例：
```json
[
  {"name": "普通心理学", "units": 6, "unit_type": "章", "mastery": "掌握", "known": 0.2},
  {"name": "认知心理学", "units": 5, "unit_type": "章", "mastery": "掌握", "exam_days": 12}
]
```

## 文件结构

```
memory-optimizer/
  SKILL.md              # 技能主文件
  scripts/
    study_planner.js    # 记忆优化核心脚本（Node.js，含遗忘曲线模型与可视化图表）
  references/
    memory-science-references.md  # 记忆与学习科学参考文献
  assets/
    study-diary-template.md       # 学习/复习日记模板
```

## 使用示例

### 示例1：期末复习周
```
用户："马上期末了，好几科要背，总是背了就忘，帮我做个复习计划"

助手：
"我来帮你制定记忆优化方案。请告诉我：

1. 你目前处于什么备考阶段？（日常学习/期中/期末复习周/考试周/考研…）
2. 距考试还有多少天？
3. 每天能投入多少小时学习？
4. 有哪些科目？每个的：内容量（几章/几页）、目标掌握度（了解/熟悉/掌握/精通）、距考试天数？"

[收集数据后，写入 tasks JSON，运行：
node scripts/study_planner.js --stage final_review --days 10 --hours 6 --tasks @tasks.json --output 报告.md]
```

### 示例2：考研备考
```
用户："考研复习内容太多，老是记不住，帮我规划一下"

助手："我来帮你制定考研记忆方案。请告诉我：
1. 备考阶段是考研备考，对吗？
2. 距考试还有多少天？
3. 每天能投入多少小时？
4. 各科目：内容量、掌握目标、当前熟悉度？"

[设置 stage=postgraduate_prep，运行脚本，生成含遗忘曲线图与复习甘特图的报告]
```

## 参考文献

详见 `references/memory-science-references.md`
- *Science*（Karpicke & Blunt 2011）、*PNAS*（Cepeda et al. 2008）
- *Psychological Science*、*Psychological Bulletin*
- *Psychological Science in the Public Interest*（Dunlosky et al. 2013）
- *Physiological Reviews*（Rasch & Born 2013, IF 37.3）

---

*版本: 1.0.0 | 与 sleep-optimizer 同系列：遗忘曲线对抗"背了就忘"，睡眠技能巩固"记了就牢"*
