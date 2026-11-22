## Description:

快手公开数据只读技能：关键词搜视频、博主作品与粉丝数据、视频评论，输出 JSON，不登录不发布。

This skill is ready for commercial/non-commercial use.

## Publisher:

[um-why](https://clawhub.ai/user/um-why)

### License/Terms of Use:

MIT

## Use Case:

Content creators, marketers, and analysts use the skill to research public Kuaishou videos, creator activity, and comments for topic research, competitor monitoring, and audience analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scan is medium confidence and partial; it does not establish that all partially reviewed scripts are safe.

Mitigation: Review the skill source before installing, especially the parts not fully covered by the scan.

Risk: Keywords and links are sent to the named third-party provider when making queries.

Mitigation: Avoid submitting confidential information and consider whether you are comfortable sharing the query data with the provider.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/um-why/skills/kuaishou-data-miner)
- [Guaikei data service](https://www.guaikei.com)
- [Command options](references/options.md)
- [FAQ and configuration](references/faq.md)

## Skill Output:

**Output Type(s):** [JSON data, Analysis]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results include command status and data; result counts depend on the provider plan.]

## Skill Version(s):

1.1.3 (source: frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
