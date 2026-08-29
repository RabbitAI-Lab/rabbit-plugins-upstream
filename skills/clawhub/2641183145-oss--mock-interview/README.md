# mock-interview — 基于真实经历的模拟面试 skill

一个 Claude Code skill。**不是题库** —— 它先引导你把经历讲清楚,然后从你的原话里
生成 5 道深挖题,在本地网页答题(支持语音),答完按 5 个维度打分并生成评分报告。

## 装

```bash
# Windows
xcopy /E /I mock-interview "%USERPROFILE%\.claude\skills\mock-interview"

# macOS / Linux
cp -r mock-interview ~/.claude/skills/
```

只需要 **Python 3.9+**,零第三方依赖(全用标准库)。

装完**新开一个会话**(skill 在会话启动时加载),然后说:

```
我想练面试
```

## 跑起来是什么样

1. **引导录入**(对话,3-4 轮)—— 岗位、院校、实习、项目/比赛/社团。
   答得越具体,题目越针对你
2. **出题**(对话)—— 5 道题,每道都引用你的原话,配 2-3 条追问提示
3. **答题**(网页)—— 它给你一个 `http://127.0.0.1:8787`,**用 Chrome 或 Edge 打开**。
   打字或语音都行。答完最后一题页面自动结束
4. **打分**(对话)—— 回到 Claude Code,它读你的回答并评分
5. **报告**(HTML)—— `data/score-report.html`,双击打开

## 评分

5 个维度,每维 1-5 分:

| 维度 | 看什么 |
|---|---|
| 实质 Substance | 有没有量化、有没有权衡过备选方案 |
| 结构 Structure | 铺垫 → 冲突 → 解决 → 影响 |
| 相关性 Relevance | 有没有答在问题真正问的点上 |
| 可信度 Credibility | 经不经得起追问、贡献边界清不清楚 |
| 差异化 Differentiation | 换个候选人是不是也能说出一样的话 |

**分数只是索引,点评才是重点。** 每题给四块:

- **好在哪** — 引用原话 + 说清这句为什么值钱
- **差在哪** — 引用原话 + 说清会导致什么后果(面试官下一句会怎么追)
- **改写示范** — before / after 对照,把你原来那句改成能得高分的版本
- **下次怎么做** — 可执行动作,不是"多练习"

外加全局总结(含跨题观察,比如"语音回答平均比打字长 40% 但结构分低 0.7")
和一个最短板 + 3 步改进计划。

一份完整报告约 3800 字,平均每题引用你的原话 4 处。

## 两条设计约束

**引用必须落地。** 所有引用都会被校验能否在你的实际回答里搜到 —— 防止模型
替你编话。

**不替你编数字。** 你没提过的数据会写成 `___(填你实际的数字)` 原样显示,
而不是凭空造一个。

## 隐私

`data/` 里是你的简历和面试回答,**明文存在本地**,已在 `.gitignore` 里。
server 只绑 `127.0.0.1`,同网段其他人访问不到。

`GET /api/session` 刻意不返回原始简历 —— 答题页不需要。

语音用浏览器的 Web Speech API。**Chrome 的实现会把音频传给 Google 服务器转写**,
介意的话用打字。

## 文件

| 路径 | 作用 |
|---|---|
| `SKILL.md` | 入口,六步流程编排 |
| `references/intake.md` | 录入话术、经历密度判定 |
| `references/question-gen.md` | 出题策略、五个考察点 |
| `references/rubrics.md` | 评分标准、根因归因、点评要求 |
| `server.py` | 答题页 server |
| `wait.py` | 等答题完成 |
| `build_report.py` | 校验评分 + 生成报告 |
| `web/index.html` | 答题页 |
| `web/score-report.template.html` | 评分报告模板 |
| `api-contract.md` | 前后端接口契约 |

## 单独联调前端

不用走 Claude,手动准备数据即可:

```bash
cp data/session.example.json data/session.json
python server.py
```

## 已知限制

- **语音只有 Chrome / Edge 支持**,Firefox 没有 Web Speech API
- 追问是预生成的,不会根据你的上一个回答动态调整(页面运行期间模型不在场)
- 不做跨轮历史追踪,每轮独立
- 端口默认 8787,被占用会自动往上找 —— **用它打印的实际 URL**

## 致谢

评分维度和根因归因的思路借鉴了
[noamseg/interview-coach-skill](https://github.com/noamseg/interview-coach-skill)(MIT)。

本项目的不同之处:

- 原版是纯 prompt engineering(48 个 markdown,无脚本),状态存在
  `coaching_state.md` 的 markdown 表格里 —— 本项目换成 JSON 状态层
- 原版无 web 界面,只能在 agent 对话里交互 —— 本项目加了网页答题页(含语音输入)
  和 HTML 评分报告
- 原版有 23 个命令覆盖求职全流程 —— 本项目只做「出题 → 答题 → 打分」一条链路
- 出题策略从评分标准反推(五个考察点各对应一个评分维度)
