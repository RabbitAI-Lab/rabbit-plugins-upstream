# JobWatch

把你的 OpenClaw agent 变成求职哨兵：定时盯目标公司 careers 页 → LLM 对照你的个人画像
判级 → 强匹配实时提醒 / 次要的每日摘要 / 全部沉淀知识库，外加投递状态跟踪和随口查询。

## 安装

唯一前提：装好的 OpenClaw（gateway 运行中）。

```bash
openclaw skills install jobwatch
```

## 上手：一句话 + 一场面试

对你的 agent 说：**「帮我做求职监控」**（或 "set up job alerts for me"）。

它会面试你（约 10 分钟，一次一组问题）：

| 面试环节 | 它会问什么 | 你怎么答 |
|---|---|---|
| 1. 目标域 | 盯哪些公司、什么方向 | 报公司名即可，招聘系统它自己探测 |
| 2. 背景 | 年限/领域/技术栈/差异化 | 口述几句，或直接丢简历文件 |
| 3. 红线 | visa？地域？绝不看的岗位类型？ | 想清楚，这是一票否决项 |
| 4. 级别意向 | 目标级别？IC 还是管理线？ | 单独问是因为现任职级≠求职意向 |
| 5. 配置 | 通知渠道 / 知识库 / JD 抓取 | 回答「全部默认」即可零配置 |

然后它自己干活：生成你的求职画像（`<workspace>/jobwatch/profile/JOB_PROFILE.md`，
永远只在你机器上）→ 探测信源写配置 → 抓一轮真实岗位试判 → **拿约 5 个判级结果和你
校准**（判错直接说，它改画像重判）→ 发一条示例 P1 提醒给你看效果 → 征得你同意后注册
定时任务（工作日每 15 分钟 + 周末每小时 + 每日 9:00 摘要）。

## 日常使用

上岗后你什么都不用做。P1 岗位会实时出现在你们的对话里，每天 9:00 一条摘要。想互动时：

- 「Databricks 那个 AI Engineer 我投了」→ 它记账；投递 7 天没动静，摘要里自动提醒跟进
- 「本周有什么好岗位？」「监控跑得怎么样？」→ 直接答
- 「以后 XX 类岗位算 P1」→ 它改画像，下轮生效

## 配置与增强（全部可选）

默认零配置：判级用你 agent 自己的模型，通知发对话渠道，知识库写本地文件。想升级：

| 增强 | 作用 | 怎么开 |
|---|---|---|
| Firecrawl / Jina key | JD 全文抓取更干净；监控 Google 系公司基本必需 | `<workspace>/jobwatch/.env` 填 `FIRECRAWL_API_KEY` 或 `JINA_API_KEY` |
| API 判级 | 更快更稳、省 agent 会话 | config `judge.mode: api` + `.env` 填 `LLM_API_KEY`（任意 OpenAI 兼容端点，非 OpenRouter 加 `LLM_BASE_URL`） |
| Telegram 直连 | 独立低延迟推送 | config `notify.mode: telegram`（自动复用 OpenClaw 的 bot 配置） |
| 2brain 知识库 | 云端 RAG：图谱 + 溯源问答 | config `kb.backend: twobrain` + `.env` 填 `TWOBRAIN_*` |

信源支持：Greenhouse / Ashby / Lever（官方 API）、Google Careers（Firecrawl 渲染）、
任意 RSS。加公司 = 让 agent 跑一次探测，加一行配置。

## 常见问题

- **重来一次 onboarding**：删掉 `<workspace>/jobwatch/` 目录，并给 agent 开个新会话（频道里发 `/new`，否则它的对话记忆还记得上次入职）。skill 本体不用动。
- **判级不准**：直接告诉 agent 哪里判错了，或自己改 `profile/JOB_PROFILE.md`——它是
  判级的唯一依据，写得越具体越准。
- **卸载**：`openclaw cron list` 删掉 3 个 jobwatch-* 任务，删除 skill 目录和
  `<workspace>/jobwatch/`。
- **隐私**：画像/密钥/运行数据全在本地 HOME 目录，skill 不上传任何数据；抓取只读
  公开信源并遵守速率限制。

## 工作原理（一图流）

```
cron 唤醒 agent
  ① 感知  官方 ATS API 抓列表 · Firecrawl 抓 SPA 详情页 JD（脚本，确定性）
  ② 推理  去重/硬过滤/岗位年龄（脚本）→ agent × 你的画像判级（LLM，可校准）
  ③ 行动  入库 + P1 实时 + P2 摘要 + 投递跟进（脚本，格式校验兜底）
```

脚本管确定性，agent 管判断，schema 校验兜底——判级失败降级进摘要，绝不静默丢岗位。
