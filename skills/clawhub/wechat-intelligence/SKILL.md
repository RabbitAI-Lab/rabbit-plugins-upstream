---
name: wechat-intelligence
description: 使用曼格云 API 构建和运行低成本的公众号情报分析系统。当用户提出公众号情报分析系统、公众号监控、多公众号监测、公众号文章自动采集、AI 分析公众号文章、竞品公众号追踪、行业情报、每日公众号简报、公众号数据导出或公众号分析面板等需求时使用。
---

# 公众号情报分析系统

把多个公众号的分散内容整理为本地、可持续增量更新的情报资料库。使用随附脚本完成接口调用、状态管理、费用核算、分析面板生成和 Excel 导出；文章分析直接使用当前智能体，不要求用户再提供第二个模型接口。

## 触发方式

- 自动触发：用户直接描述公众号监控、文章采集、AI 分析、竞品追踪、每日简报、分析面板或数据导出等相关需求。
- 显式触发：在需求开头输入 `$wechat-intelligence`，例如“`$wechat-intelligence 帮我监控这 10 个公众号并生成每日情报`”。
- `公众号情报分析系统` 是对外显示名称，`wechat-intelligence` 是符合 Skill 格式要求的技术标识，不能翻译为中文命令。

## 运行流程

1. 选择由客户管理的工作目录。用户未指定时，默认使用 `~/MangyunWechatIntelligence`。
2. 首次使用时运行一次 `scripts/mangyun_intelligence.py --workspace <路径> init`。
3. 使用 `account add` 添加公众号。优先使用 `--ghid gh_xxx`；不知道原始标识时再使用 `--url`，不得虚构标识。
4. 首次采集前或大批量调整公众号后运行 `estimate`。用人民币元说明固定的第一页费用、可能产生的翻页费用，以及每篇新增文章的正文费用。
5. 运行 `scan`。程序通过历史文章接口按每页 20 条发现文章，遇到已知文章后停止；发现阶段不获取正文。
6. 运行 `status`。如果存在待获取正文，运行 `fetch-content`；预计费用超过单次预算时，脚本会停止，除非用户明确授权使用 `--allow-over-budget`。
7. 运行 `make-analysis-queue`。只分析队列中的新增文章，遵循 [分析结果规范](references/analysis-schema.md)，把结果 JSON 写入脚本指定的路径，再用 `import-analysis` 导入。队列每篇包含 `crossAccountContext`（同主题/同关键词的跨公众号已分析文章）和 `accountKeywords`，分析时据此填写 `relatedAccounts`。
8. 运行 `make-brief`。跨文章聚合：按主题聚类、生成每日摘要与跨号话题对比（纯本地计算，不调用付费接口）。可选为 AI 生成收尾队列，补充各话题立场对比一句话。用 `analyze-topics` 做主题聚类检索/复盘。
9. 运行 `build-dashboard` 和 `export`。向用户返回 `dashboard.html` 和 Excel 工作簿的绝对路径。

日常更新不得重建基线，也不得重复获取已分析文章的正文。依次完成 `scan`、`fetch-content`、队列分析、`make-brief`，然后重新生成分析面板和 Excel。

## 成本控制

- 日常发现新文章使用 `wechat-native-account-articles`，不使用今日文章接口。当前公开价格见 [曼格云 API 调用规范](references/api-contract.md)。
- 每页固定使用 20 条。页容量变小不会降低单页价格，反而更容易产生额外翻页费用。
- 首次扫描只建立文章元数据基线。除非用户明确要求补齐历史正文并接受费用预估，否则不得获取基线文章正文。
- 只获取纯文本。除非用户的结果确实需要，否则不得请求 HTML、文章报告、指标、评论或公众号资料。
- 重试时复用已经生成的幂等键，不得随机生成新的重试键。
- 遵守工作目录中的预算设置。预计正文费用超出预算时，保留待处理状态，并在继续前征得用户同意。
- 真实费用以接口响应中的 `consumption` 为准，通过 `status` 或分析面板报告，不得根据文章数量猜测。

## 分析规则

- 每篇文章只分析一次，除非用户明确要求重新分析。
- 结论只能依据队列提供的标题、摘要和正文，不得虚构数字、实体或变化。
- 区分文章中的主张与已经核实的事实，不确定内容写入 `risks`。
- 使用简洁中文输出。主题限制为 1 至 5 个稳定标签，重要程度使用 1 至 5 的整数。
- 仅在确有相关证据时与 `previousContext` 对比；上下文为空表示没有纵向比较依据。
- 原样保留文章编号，确保导入结果可以准确对应。
- `stance` 描述本文相对话题的立场（利好/质疑/中立/通报），缺失或非法值自动回退为"通报"，不阻断导入。
- `relatedAccounts` 只能依据队列的 `crossAccountContext` 填写，不得臆造账号，用于跨公众号同话题对比。

## 安全与存储

- 只从 `MANGYUN_API_KEY` 读取接口密钥。不得把密钥写入配置、SQLite、输出文件、日志、提示词或截图。
- 只保存公开文章元数据、规范化公开链接、用户要求获取的纯文本、分析结果和费用汇总。不得保存 Cookie、授权请求头、`key`、`pass_ticket`、`appmsg_token` 或完整接口响应。
- 可选的分析面板服务只能绑定到 `127.0.0.1`。
- 自动分析仅作为辅助。导出结果必须保留原文链接，便于客户回到原文核验关键事实。

## 常用命令

运行 `python scripts/mangyun_intelligence.py --help` 查看全部参数。常用命令如下：

```text
init
account add --name "账号名" --ghid gh_xxxxxxxxxxxx --keyword 行业 --group 竞品
account add --name "账号名" --url https://mp.weixin.qq.com/s/...
account list
estimate
scan
fetch-content
make-analysis-queue
import-analysis --input <analysis.json>
make-brief [--date YYYY-MM-DD] [--rebuild] [--no-daily-queue]
analyze-topics [--topic 主题] [--account 账号] [--json]
build-dashboard
export
status
serve
doctor
```

用户要求定时运行时，优先配置智能体自身的周期任务执行日常更新流程。没有明确授权时，不得创建操作系统计划任务或外部自动化。
