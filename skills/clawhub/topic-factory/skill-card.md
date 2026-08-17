## Description:

跨平台自媒体选题日报系统每天从头条、微博、B站、抖音、知乎和36氪等公开热榜抓取热点，按关键词库筛选选题，用 LLM 生成短视频钩子、公众号标题和数据点，并输出 Markdown 日报供飞书推送。

This skill is ready for commercial/non-commercial use.

## Publisher:

[seairteng](https://clawhub.ai/user/seairteng)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, content operators, and automation-focused developers use this skill to generate a daily shortlist of Chinese social media and news topics, with hooks, article title candidates, supporting data points, and source links for review before publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected topic metadata and prompts may be sent to the configured LLM provider.

Mitigation: Use an approved API token and endpoint, avoid adding private source material to topic files, and review generated hooks, titles, and data points before publication.

Risk: Feishu delivery can post generated report text to the configured webhook or expose fallback text in logs.

Mitigation: Keep webhook tokens out of committed files, verify the target chat or fallback recipient, and rotate the webhook if it has been exposed.

Risk: Scheduled jobs fetch public trend data and write Markdown reports, logs, and history files under the configured workspace.

Mitigation: Run the cron jobs with a least-privilege user, review output paths, and monitor logs for unexpected network or file-write failures.

Risk: Archive behavior depends on the adoption marker and may delete history files older than the retention window.

Mitigation: Confirm the adoption marker workflow before relying on archives, and back up reports that must be retained longer than the built-in history cleanup period.

Risk: The daily wrapper calls an external send_alert.py helper when repeated generation attempts fail.

Mitigation: Verify the helper script, alert destination, and permissions before enabling production scheduling.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/seairteng/skills/topic-factory)
- [Publisher profile: seairteng](https://clawhub.ai/user/seairteng)
- [Anthropic API endpoint](https://api.anthropic.com)
- [Toutiao hot board API](https://www.toutiao.com/hot-event/hot-board/?origin=toutiao_pc)
- [Weibo hot search API](https://api.weibo.cn/2/guest/search/hot/word)
- [Bilibili search trend API](https://api.bilibili.com/x/web-interface/search/square?limit=50)
- [Douyin hot search API](https://www.douyin.com/aweme/v1/web/hot/search/list/?aid=6383&count=50)
- [Zhihu hot list API](https://api.zhihu.com/topstory/hot-lists/total?limit=50)
- [36kr RSS feed](https://www.36kr.com/feed)

## Skill Output:

**Output Type(s):** [Markdown, Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports, plain-text Feishu messages or fallback text, and shell/cron setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces daily topic reports under the configured workspace topics directory and optional history archives for unused topics.]

## Skill Version(s):

1.0.1 (source: server release metadata and CHANGELOG, released 2026-08-17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
