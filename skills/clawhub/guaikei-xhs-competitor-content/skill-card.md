## Description:

搜小红书笔记、看笔记详情、查笔记评论、查博主作品，用于获取公开的小红书内容、评论和博主作品数据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users, creators, marketers, and analysts use this skill to collect public Xiaohongshu search results, note details, comments, and creator posts for competitor research, trend monitoring, KOL screening, and content planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, competitor targets, note links, and the API token are sent to the third-party guaikei.com service.

Mitigation: Use only inputs approved for third-party processing and avoid submitting sensitive targets or confidential research terms.

Risk: Full command results are saved locally under the skill's logs directory.

Mitigation: Restrict filesystem access to the workspace and delete or archive logs according to the user's data handling policy.

Risk: The security summary flags limited user control over data sent to the third-party service and locally stored results.

Mitigation: Review the security guidance before installation and run the skill only when the data transfer and retention behavior is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-competitor-content)
- [engheng-art publisher profile](https://clawhub.ai/user/engheng-art)
- [Guaikei API service](https://www.guaikei.com)
- [Parameter and invocation guide](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Markdown, Guidance, Files]

**Output Format:** [JSON command output with concise Markdown summaries and saved JSON result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; successful commands save full results under a local logs directory.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact metadata reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
