## Description:

China News gathers current Chinese news from Sina, Sohu, NetEase, Tencent, and RSS sources, then generates categorized news reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tobewin](https://clawhub.ai/user/tobewin)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to fetch recent Chinese news, group items by topic, and produce a readable daily news report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill makes outbound requests to public Chinese news and RSS sites.

Mitigation: Use it only in environments where those network requests are acceptable.

Risk: The skill may create or overwrite a dated Markdown report in the workspace.

Mitigation: Ask the agent to confirm the output path before saving or overwriting reports.

Risk: The skill depends on the Python requests package.

Mitigation: Pin the dependency version in stricter environments.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/tobewin/skills/china-news)
- [Sina News](https://news.sina.com.cn)
- [Sohu News](https://news.sohu.com)
- [NetEase News](https://news.163.com)
- [Sina Domestic News RSS](https://rss.sina.com.cn/news/china/roll.xml)
- [Sina World News RSS](https://rss.sina.com.cn/news/world/roll.xml)
- [Sohu News RSS](https://news.sohu.com/rss/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline Python and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create a dated Markdown news report in the workspace.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
