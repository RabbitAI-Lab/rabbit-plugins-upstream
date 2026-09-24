## Description:

输入关键词、快手账号主页链接，自动拉取垂类作品、账号作品并解析无水印下载链接，支持一键批量下载到本地。

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

External operators, marketers, content teams, and analysts use this skill to retrieve public Kuaishou search results, creator post lists, and video comments for content research, trend monitoring, competitor analysis, creator screening, and local batch download workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries, Kuaishou URLs or IDs, request limits, and the GUAIKEI_API_TOKEN are sent to guaikei.com.

Mitigation: Use the skill only when that data sharing is acceptable, keep the token in an environment variable, and avoid submitting sensitive or unauthorized targets.

Risk: Saved logs may contain collected public content data, including comments, author metadata, source links, and download links.

Mitigation: Restrict access to logs and retain or delete them according to privacy, platform-compliance, and internal data-handling obligations.

Risk: The skill is intended for public Kuaishou data and does not support private, hidden, or login-gated content.

Mitigation: Reject requests for private or non-public data and use the skill only for publicly accessible Kuaishou content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/why20261/skills/kuaishou-batch-downloader)
- [GUAIKEI API token and support](https://www.guaikei.com)
- [Complete options guide](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Structured JSON from command-line scripts, with local log files when commands run.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results can include public Kuaishou video, author, comment, interaction, source link, and download-link data.]

## Skill Version(s):

1.0.0 (source: release evidence, frontmatter, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
