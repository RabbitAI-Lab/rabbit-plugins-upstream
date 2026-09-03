---
name: mock-interview
description: 基于用户真实经历的模拟面试。引导录入经历后生成 5 道深挖题,在本地网页答题(支持语音),答完按 5 个维度打分并生成评分报告。当用户想练面试、模拟面试、准备面试、练习行为面试题时使用。
---

# 模拟面试

一条链路:**引导录入 → 出题 → 网页答题 → 打分 → 报告**。

核心区别于普通题库:**题目从用户自己的经历里长出来**,不是"讲讲你的优缺点"。

## 流程

### 1. 录入经历

按 `references/intake.md` 走四轮对话。要点:

- 开场先预告"大概三四轮、两三分钟",用户才配合
- 相近的合并问,别一轮一个问题
- 用户说"没有"立刻跳过,不追
- 拿到的原话尽量保留 —— 出题时 `source_quote` 要从这里摘

完成后判定经历密度(`rich` / `moderate` / `sparse`),规则在同一份文档里。**课程项目、比赛、开源、社团负责人都算实质经历**,不能只认实习。

### 2. 出题

按 `references/question-gen.md` 生成 5 道题,写入 `data/session.json`。

硬要求:
- 默认全部深挖用户经历,通用题只在 `sparse` 档兜底
- `source_quote` 必须是用户原话,题干里要带上引用
- 每题 2-3 条 `probes`,指向 rubric 的加分点
- 不问用户没提过的东西

写文件时 `status` 置 `awaiting_answers`,`answers` 置空数组,`scores` 置 `null`。完整结构见 `data/session.example.json`。

### 3. 起服务

```bash
python server.py
```

后台跑。它会打印 URL(默认 `http://127.0.0.1:8787`,端口占用会自动往上找,实际 URL 在输出里)。

**把 URL 给用户,并说明:**
> 打开这个链接答题,5 道题,可以打字也可以语音。答完最后一题页面会自己结束,然后回来找我看分。

### 4. 等

```bash
python wait.py
```

每次最多阻塞约 90 秒。退出码:

| 码 | 含义 | 你该做什么 |
|---|---|---|
| 0 | 收集完成 | 进入打分 |
| 2 | 还没答完(带进度) | **再调一次 `wait.py`** |
| 3 | 出错 | 看输出信息 |

退出码 2 就继续调,别停下来问用户"答完了吗"。一轮面试十分钟左右,调七八次是正常的。

用户中途放弃的话,不足 5 题也能打分 —— 报告会自动标为低置信度。

### 5. 打分

读 `data/session.json` 里的 `questions` 和 `answers`,按 `references/rubrics.md` 打分,写 `data/scores.json`。

**分数只是索引,点评才是用户要看的东西。** rubrics.md 里「写点评」那一节是重点,别只看评分表。

每题必须给:

- `strengths` — 至少 1 条,每条 `quote` + `why`(这句为什么值钱)
- `weaknesses` — 1-3 条,每条 `quote` + `problem` + `dimension`(会导致什么后果)
- `rewrite` — `before` / `after` / `what_changed`,**改写示范不能省,这是最有用的一块**
- `fix` — 2-3 句可执行动作

顶层还要给 `summary`(3-5 句跨题观察)和 `bottleneck`(含 `evidence_across_questions` 至少两条、`improvement_plan` 恰好 3 步)。

**四条硬约束:**

1. **所有 `quote` 必须是用户原话**,能在 `answers[].text` 里搜到。校验脚本会检查,编造会报警告。
2. **`rewrite.after` 不许编事实。** 用户没给的数字写成 `___(填你实际的数字)`。
3. **给分要有区分度。** 五题全 3 分的报告没有信息量。
4. **别写"多练习""注意结构"这类空话。** 太短会被校验拦下来。

有 `input_mode` / `duration_sec` 时,在 `summary` 里对比语音和打字的差异 —— 这是本系统独有的观察。

字段结构见 `data/scores.example.json`(那份是深度标杆,照那个量级写)。写完先自检:

```bash
python build_report.py --check
```

校验不通过会把所有问题一次列出来,改完再跑。除结构完整性外它还会检查:

- **点评长度** —— `fix` / `why` / `problem` / `what_changed` 太短会被拦(防空话)
- **引用落地** —— 所有 `quote` 能否在用户回答里搜到(防编造),不匹配报警告
- `overall` 是否等于逐题均值、`bottleneck` 是否真指向最低分维度 —— 警告,不阻断,但通常说明算错了

### 6. 生成报告

```bash
python build_report.py
```

产出 `data/score-report.html`,自包含,双击就能开。告诉用户路径,并把**瓶颈维度和 next_drill 在对话里也说一遍** —— 有人不会去点那个文件。

## 收尾

报告给完后,如果用户想改进重练:重新出题(可以只换瓶颈维度相关的题),`data/` 下的旧文件直接覆盖。不做跨轮历史追踪。

## 文件

| 路径 | 作用 |
|---|---|
| `references/intake.md` | 四轮录入话术、密度判定 |
| `references/question-gen.md` | 出题策略、五个考察点 |
| `references/rubrics.md` | 5 维评分标准、根因归因 |
| `api-contract.md` | 前端接口契约(给前端同事看) |
| `server.py` | 答题页 server |
| `wait.py` | 等待答题完成 |
| `build_report.py` | 校验评分 + 生成报告 |
| `data/session.json` | 单一数据源 |

`data/` 里是用户简历和面试回答,已在 `.gitignore` 里。

## 注意

**别自己在对话里出题然后让用户口头答。** 那绕过了整条链路,也拿不到 `input_mode` 和 `duration_sec`。

**server 收满 5 题会自动退出**,这是设计好的,不是崩了。

**端口冲突时它会自己避让**,用它打印的 URL,不要假定是 8787。

**打分前确认 `wait.py` 返回 0。** 提前打分会漏掉后面的回答。
