## Description:

按关键词检索微信公开文章和视频，并返回结构化结果。

This skill is ready for commercial/non-commercial use.

## Publisher:

[um-why](https://clawhub.ai/user/um-why)

### License/Terms of Use:

MIT

## Use Case:

内容分析人员和开发者可按关键词、发布时间、热度或视频时长检索微信公开文章和视频，用于选题发现与趋势监测。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search keywords are sent to the third-party Guaikei API service, and searches may incur usage costs.

Mitigation: Use non-sensitive, public topics; keep the default result limit unless more results are needed, and review any returned cost estimate.

Risk: ClawScan reports a benign verdict with medium confidence, but its analysis was partial: 18 of 28 components were fully inspected.

Mitigation: Review the scripts before deployment and account for the remaining inspection uncertainty when deciding whether to install.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/um-why/skills/wechat-search-sou)
- [Search options](references/options.md)
- [FAQ and setup](references/faq.md)
- [Guaikei API service](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [JSON]

**Output Format:** [Structured JSON search-result envelope]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Article or video results; defaults to 10 items. Responses may include an estimated cost.]

## Skill Version(s):

1.1.2 (source: frontmatter, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
