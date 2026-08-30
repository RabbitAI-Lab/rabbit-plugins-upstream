# API 契约 — 模拟面试答题页

给前端同事看这一份就够了。后端是 Python 标准库写的本地 server,零依赖。

## 一句话流程

Claude 在对话里引导用户录入经历 → 生成 5 道深挖题 → 起 server → **你的页面接手,收 5 个回答** → 第 5 题落地后 server 自动退出 → Claude 打分 → 生成一个独立的评分报告 HTML。

你负责两个页面:

1. **答题页** `web/index.html` — server 托管,用户在这答题
2. **评分报告模板** `web/score-report.template.html` — 静态文件,后端把 JSON 注进去生成最终报告

## 跑起来

```bash
python server.py          # http://127.0.0.1:8787
```

只绑 `127.0.0.1`,同网段其他人访问不到(里面是用户的简历和面试回答)。

端口被占时自动往上找 8788、8789…… 实际端口会打印在终端,也写在 `data/server-info.json` 里。

### 用 Vite / CRA 等 dev server

已经开了 CORS,放行 `http://localhost:*` 和 `http://127.0.0.1:*` 任意端口,预检也处理了。你在 5173 起 dev server 直接 fetch `http://127.0.0.1:8787/api/session` 就行,不用配代理。

要是你就写个静态 HTML,丢进 `web/` 让 server 托管更省事,`/` 默认返回 `web/index.html`。

## 接口

### `GET /api/session`

进页面先调这个。**不返回用户录入的原始经历**,只给答题需要的东西。

```json
{
  "session_id": "20260827-143022",
  "status": "awaiting_answers",
  "context": {
    "target_role": "后端开发实习",
    "seniority": "本科应届",
    "experience_density": "rich",
    "density_note": null
  },
  "questions": [
    {
      "id": "q1",
      "text": "你简历里写独立负责了订单服务的缓存层重构。说说当时为什么要重构?",
      "competency": "决策点",
      "source_quote": "独立负责订单服务的缓存层重构",
      "probes": [
        "重构前具体是什么问题,怎么发现的",
        "考虑过哪些方案,最后为什么选这个",
        "效果怎么衡量的,有数据吗"
      ],
      "is_generic": false
    }
  ],
  "answered": ["q1"],
  "total": 5
}
```

字段说明:

| 字段 | 用途 |
|---|---|
| `questions[].probes` | 2-3 条追问方向。**建议显示成"可以覆盖这几点"**,用户照着说容易得高分。不是必答项 |
| `questions[].source_quote` | 从用户经历里摘的原话。题干上方显示"关于你提到的:…",用户会明显感到题是针对他的 |
| `questions[].competency` | 考察点,如 `决策点` / `量化口径` / `贡献边界` / `返工点` / `技术细节` |
| `questions[].is_generic` | `true` 表示这题是宽泛通用题(用户经历太少时的兜底)。可以不做区分,也可以淡化处理 |
| `context.density_note` | 经历稀薄时的提示语,**非 null 就显示出来**。内容类似"你的材料里可追问细节不多,所以有 3 道是通用题" |
| `answered` | 已答 qid。刷新/断线后用它跳回第一道未答的题 |

`status` 只会是 `awaiting_answers`。如果拿到别的值,说明这轮已经答完了,提示用户回 Claude Code 重新开一轮。

### `POST /api/answer`

用户答完一题就提一次,不要攒到最后。

```json
{
  "qid": "q1",
  "text": "当时线上订单查询 p99 到了 800ms……",
  "input_mode": "voice",
  "duration_sec": 96
}
```

| 字段 | 必填 | 说明 |
|---|---|---|
| `qid` | 是 | 必须是 `/api/session` 给过的 id |
| `text` | 是 | 回答正文。语音的话就是识别后的文本 |
| `input_mode` | 否 | `voice` / `text`。缺省当 `text` |
| `duration_sec` | 否 | 语音时长。有就传,用来分析"说得久但结构差" |

同一个 `qid` 重复提交是**覆盖**,允许用户改答案。

响应:

```json
{ "ok": true, "answered": 2, "total": 5, "all_done": false }
```

### ⚠️ 第 5 题:server 会自己退出

第 5 个回答落地后,响应变成:

```json
{ "ok": true, "answered": 5, "total": 5, "all_done": true,
  "message": "回答已全部收集,请回到 Claude Code 查看评分" }
```

**这个响应返回约 1 秒后,server 进程就退出了。**

所以:

- 收到 `all_done: true` 后**不要再发任何请求** —— 包括再调一次 `/api/session` 刷新状态,那会连接失败
- 结束屏用你手里已有的数据渲染,别指望再拉一次
- 结束屏上请写明:**回到 Claude Code 查看评分**。用户不知道下一步去哪就断链了

这是刻意设计的:你说的"问题收集完 web 应用结束",就是这个。

### `GET /api/health`

`{"ok": true, "status": "awaiting_answers", "answered": 2, "total": 5}`

调试用,不影响主流程。

## 错误

统一 `{"error": {"code": "...", "message": "..."}}`,HTTP 状态码对应:

| code | HTTP | 含义 |
|---|---|---|
| `unknown_qid` | 400 | `qid` 不在题目列表里 |
| `empty_answer` | 400 | `text` 去空白后为空 |
| `session_closed` | 409 | 已经收集完了,不再接受提交 |
| `bad_json` | 400 | 请求体不是合法 JSON |

## 评分报告模板

第二个页面。**不走 HTTP**,是纯静态模板 —— 后端把评分 JSON 注进去,生成一个能直接双击打开的独立 HTML。

在 `web/score-report.template.html` 里放一个占位符:

```html
<script id="score-data" type="application/json">__SCORE_DATA__</script>
```

后端把 `__SCORE_DATA__` 整段替换成 JSON。你这样读:

```js
const data = JSON.parse(document.getElementById('score-data').textContent);
```

生成的报告是 `data/score-report.html`,自包含。所以 **CSS 和 JS 请内联**,或者用 CDN —— 引本地相对路径的文件,报告单独发给别人看就裂了。

注入的数据:

```json
{
  "session_id": "20260827-143022",
  "generated_at": "2026-08-27 15:04",
  "context": { "target_role": "后端开发实习", "seniority": "本科应届" },
  "partial": false,
  "answered_count": 5,

  "summary": "你五道题里有三道掉在同一个地方:讲得清「做了什么」,讲不清「为什么这么选」……(3-5 句,含跨题观察)",

  "overall": {
    "substance": 3.4, "structure": 3.8, "relevance": 3.6,
    "credibility": 4.0, "differentiation": 2.4
  },

  "per_question": [
    {
      "qid": "q1",
      "question": "你简历里写独立负责了订单服务的缓存层重构……",
      "competency": "决策点",
      "answer_excerpt": "当时线上订单查询 p99 到了 800ms……",
      "input_mode": "voice",
      "duration_sec": 96,
      "scores": { "substance": 4, "structure": 4, "relevance": 4,
                  "credibility": 4, "differentiation": 3 },

      "strengths": [
        { "quote": "测了本地缓存、Redis、多级缓存三种方案",
          "why": "这句直接把 Substance 从 3 分拉到 4 分……" }
      ],
      "weaknesses": [
        { "quote": "最后选 Redis",
          "problem": "你列了三个方案却只说结论……",
          "dimension": "substance" }
      ],
      "rewrite": {
        "before": "最后选 Redis",
        "after": "最后选 Redis,因为服务有 4 个实例,本地缓存的一致性我搞不定……",
        "what_changed": "补上了两个排除理由(一致性、时间成本)……"
      },
      "fix": "答技术选型题时,固定用「三个方案 → 各自的致命缺点 → 我的取舍标准」这个顺序……",

      "evidence": "(后端自动合成的纯文本版,见下)"
    }
  ],

  "bottleneck": {
    "dimension": "differentiation",
    "label": "差异化",
    "score": 2.4,
    "root_cause": "你五道题都停在「我做了什么」,没有一道走到「我因此认为什么」……",
    "evidence_across_questions": [
      { "qid": "q2", "quote": "5000 QPS 打了十分钟,用 wrk",
        "note": "口径清楚,但换任何做过压测的候选人都会这么答" },
      { "qid": "q5", "quote": "已支付又变回待支付",
        "note": "全场最强的差异化素材,却只用了半句话" }
    ],
    "improvement_plan": [
      "先把 q5 那个时序问题补成完整三句话……",
      "回去翻这两段实习,找出三个「文档上不会写、只有做过才知道」的点……",
      "下次答题结尾刻意加一句「我从这件事上得出的判断是……」"
    ],
    "next_drill": "(后端自动合成:improvement_plan 的编号列表)"
  }
}
```

### 兼容说明(重要)

`evidence` 和 `next_drill` 原来是纯字符串,现在细节都拆到了结构化字段里。
**后端会从结构化字段自动合成这两个字符串**,所以你现有的渲染代码不改也能跑,
只是内容变长了(每题 500-800 字,原来 60 字左右)。

想要更好的呈现,建议改读结构化字段:

| 字段 | 建议呈现 |
|---|---|
| `summary` | 报告最上方,独立一段。这是唯一有跨题观察的部分 |
| `strengths[]` | 绿色/正向色块。`quote` 用引号样式突出,`why` 跟在后面 |
| `weaknesses[]` | 警示色块。`dimension` 可以做成小标签,指明扣的是哪一维 |
| `rewrite` | **建议做成 before / after 左右对照**,这是全报告最有用的一块 |
| `fix` | 每题末尾,行动项样式 |
| `bottleneck.evidence_across_questions[]` | 跨题证据列表,每条带 `qid` 跳转到对应题目 |
| `bottleneck.improvement_plan[]` | 固定 3 步,做成有序列表 |

`rewrite.after` 里可能出现 `___(填你实际的数字)` 这种占位 —— 用户没提供的数字
不会替他编造,请**原样显示**,这是刻意的。

### 其他要点

- `overall` 是 5 维均值(1-5,一位小数),喂雷达图
- **`bottleneck` 只有一个**。五维全标红没人看得下去,聚焦最短板才有行动价值 —— 请让它最显眼
- 所有 `quote` 都是用户原话,后端已校验能在回答里搜到。**别折叠隐藏**,这是报告最有说服力的部分
- `partial: true` 表示中途退出、不足 5 题。**请显示一条低置信度提示**,`answered_count` 告诉你实际几题
- `duration_sec` 可能为 `null`(打字输入)
- `strengths` 每题至少 1 条,`weaknesses` 1-3 条,`rewrite` 每题必有 —— 可以按固定结构布局

5 个维度固定这五个 key,顺序建议:`substance` 实质 → `structure` 结构 → `relevance` 相关性 → `credibility` 可信度 → `differentiation` 差异化。

## 答题页几点建议

不是硬要求,踩过的坑同步给你:

**语音输入归你。** Web Speech API(`webkitSpeechRecognition`)三个坑:①`continuous = true`,面试回答一两分钟;② 它会在停顿两秒时自己 `onend`,用户没点停止就得自动 `start()` 接上,这是最容易翻车的地方;③ 只有 Chrome/Edge 有,Firefox 没有。**文本框一定留着**,麦克风演示掉链子的概率不低。

**建议单题一屏、只能往前。** 像真面试,代码也简单。答完 5 题给个汇总确认屏再逐条提交也行 —— 但注意最后一条提交后 server 就没了。

**无障碍顺手做掉:** 输入框挂 `<label>`,语音实时转写区加 `aria-live="polite"`,确保全键盘可达。

**别把 `probes` 做成必填。** 它是提示,不是表单项。

## 联调

`data/session.json` 是单一数据源。想脱离 Claude 单独测,手写一份塞进去再起 server 就行,格式照 `GET /api/session` 的响应。仓库里带了 `data/session.example.json` 可以直接复制。


