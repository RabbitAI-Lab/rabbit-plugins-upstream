## Description:

获取小红书博主公开作品及单篇笔记的真实点赞、评论、收藏数据，帮助评估公开互动质量；不用于粉丝数估算、私密内容或后台数据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content teams, marketers, and analysts use this skill to search Xiaohongshu public posts, inspect note details and comments, and review a creator's public works for KOL screening, competitor monitoring, topic research, and engagement-quality analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords and note or profile URLs, including xsec_token query values, are sent to guaikei.com with GUAIKEI_API_TOKEN.

Mitigation: Use the skill only for authorized public-data collection, avoid submitting sensitive URLs or tokens, and confirm that third-party API use is acceptable for the task.

Risk: Retrieved data and request context can be saved locally under logs/.

Mitigation: Review generated logs and delete them when they are no longer needed.

Risk: High --limit values can collect large comment or public-post datasets and increase exposure of submitted task details.

Mitigation: Use the lowest --limit value that supports the analysis and collect only the data needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-blogger-insights)
- [Guaikei API service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, text]

**Output Format:** [Markdown guidance with inline shell commands; command execution returns structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js and GUAIKEI_API_TOKEN. Commands may save retrieved results under logs/.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
