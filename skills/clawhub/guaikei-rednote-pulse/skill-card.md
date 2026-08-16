## Description:

检索小红书公开内容：按关键词搜笔记、查单篇笔记详情、单独拉取评论区、抓取博主主页作品列表，输出结构化 JSON，支撑爆款选题、竞品监控、KOL 筛选与评论舆情分析。

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content operators, marketers, and analysts use this skill to retrieve public Xiaohongshu notes, note details, comments, and creator post lists for topic research, competitor monitoring, KOL screening, and comment analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords, note or profile URLs, request parameters, and the Guaikei API token are sent to the Guaikei service.

Mitigation: Confirm external API use is acceptable before installation, scope the token appropriately, and avoid submitting sensitive research targets.

Risk: Command results may be saved as local logs containing research targets or retrieved public-content data.

Mitigation: Protect or delete generated logs on shared machines and avoid committing them to source control.

Risk: The skill is limited to public Xiaohongshu data and depends on token validity, service availability, and platform response behavior.

Mitigation: Check command status fields, handle empty or error results explicitly, and do not treat failed or empty responses as evidence.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-rednote-pulse)
- [Publisher profile](https://clawhub.ai/user/engheng-art)
- [Guaikei API service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, json, guidance]

**Output Format:** [JSON result envelopes with status, request metadata, and results, plus concise agent-facing text when useful.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and a GUAIKEI_API_TOKEN; commands can save task outputs under local logs.]

## Skill Version(s):

1.0.0 (source: server release evidence; artifact metadata reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
