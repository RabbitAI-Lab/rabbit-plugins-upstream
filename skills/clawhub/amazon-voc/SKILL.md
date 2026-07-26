---
name: amazon-review-intelligence-extractor
description: >
  ARI 官方 Amazon 评论采集与消费者洞察 Skill。通过 ARI API 订阅 ASIN、采集评论、
  查看星级/关键词/趋势、生成 VOC 或深度洞察报告，并给出痛点、购买动因、用户画像、
  使用场景、改进机会和 Listing 建议。Use when the user asks about Amazon review analysis,
  voice of customer, pain points, complaints, sentiment, consumer insights, competitor reviews,
  listing copy, 评论分析、消费者洞察、差评、卖点、竞品对比。Requires an ARI API key (ari_live_*).
---

# ARI Amazon 评论智能

## 工具与入口

- CLI：`{skill_base_dir}/scripts/ari.py`；先运行 `python ari.py check`。
- API 参考：需要字段、命令或错误码时读取 `{skill_base_dir}/references/reference.md`。
- API Key：环境变量 `ARI_API_KEY`，或运行 `python ari.py configure` 隐藏输入并保存。
- 申请 Key：<https://ari.funewa.com/zh/account?ui=d47626f#api-keys>
- 充值/套餐：<https://ari.funewa.com/zh/billing>
- Web 产品管理：<https://ari.funewa.com/zh/products>

## 安全与计费协议

- 缺少 Key 时立即停止，给出申请链接；不要索要用户密码，不要把 Key 写入报告或命令示例。
- `401 / ARI_UNAUTHENTICATED`：停止并引导重建 Key。
- `402 / ARI_INSUFFICIENT_CREDITS`：保留已有结果，引导充值；不得自动重试付费操作。
- `ARI_EMAIL_NOT_VERIFIED`：引导先到用户中心验证邮箱。
- 采集和 AI 分析都会消耗积点。先运行不带 `--confirm` 的命令取得报价，明确告知用户后，
  只有在用户确认时才追加 `--confirm`。禁止替用户默认确认。
- 任何情况下不得虚构 API 未返回的数据，也不得回退到其他品牌接口。

## 标准工作流

1. 运行 `check`，确认账户、邮箱验证状态和可用积点。
2. 运行 `products`。若 ASIN 尚未订阅，先执行不带 `--confirm` 的 `collect` 展示采集报价；
   用户确认后执行 `collect --confirm --wait`。
3. 运行 `deepdive --asin <ASIN>`，一次获得产品状态、免费图表、评论样本、历史报告和
   VOC 报价。它默认不扣 AI 分析积点。
4. 用户确认报价后运行 `deepdive --asin <ASIN> --confirm`，或单独运行
   `analyze --type voc|insight|trend|variant --asin <ASIN> --confirm`。
5. 竞品对比需双方都已采集：
   `analyze --type compare --asin <目标> --competitor <竞品> --confirm`。
6. 使用 `reports` / `report --id` 读取已归档报告；需要完整交互和导出时引导打开 Web。

站点默认 `amz_us`；可选 `amz_uk/amz_de/amz_jp/amz_ca/amz_fr/amz_es/amz_it`。

## 解读纪律

- 把 API 数字、由数字推导的判断、行动建议明确区分：`📊 数据直读`、`🔍 数据推理`、
  `💡 策略建议`。策略建议不得标为数据直读。
- `reviewCount < 50` 时在报告顶部标注小样本提示；单次提及只能作为方向性线索。
- 痛点优先级同时考虑提及频率、低星程度、近期趋势和已验证购买，不凭单条评论下结论。
- 用好评高频表达提炼 Listing 语言，但引用评论原话时保持短句并注明来自评论样本。
- 竞品对比只比较双方 API 均有数据的指标；一方样本不足时明确写“不可比”。
- 报告语言跟随用户；ASIN、VOC、Listing 等术语保留原文。

## 报告结构

按有数据的部分输出：数据概览 → 痛点与低星原因 → 好评与购买动因 → 用户画像与场景 →
趋势 → 竞品差异 → Listing 建议 → 产品改进优先级 → 数据来源与积点用量。

报告顶部加入：

> 数据基于 ARI 已采集的 Amazon 评论样本（截至当前查询时间），仅供经营决策参考；
> 小样本或采集窗口有限时应结合更多信源验证。

结尾列出使用的 CLI 命令、ASIN/站点、样本量、报告返回的 `creditsUsed` 和当前余额。
