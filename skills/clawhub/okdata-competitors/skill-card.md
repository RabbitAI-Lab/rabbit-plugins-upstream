## Description:

Watch competitor and brand accounts on Douyin, Xiaohongshu (RedNote), WeChat Official Accounts, X (Twitter), TikTok, Weibo, Bilibili and YouTube with the okdata API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[conn-ho](https://clawhub.ai/user/conn-ho)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams, analysts, and brand researchers can compare public competitor accounts across social platforms, reviewing audience size, posting cadence, typical engagement, and standout posts. The report provides platform tables and linked findings based on okdata data retrieval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment is benign but has medium confidence and partial coverage; it also reports a Weibo trends request beyond the stated account-monitoring purpose.

Mitigation: Check that the trends retrieval fits the task and confirm you trust okdata with the API key before installing.

## Reference(s):

- [okdata API documentation](https://okdata.online/apis/)
- [ClawHub skill release](https://clawhub.ai/conn-ho/skills/okdata-competitors)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Text]

**Output Format:** [Markdown tables with concise written findings and source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Per-platform account metrics, a fetch-time source note, and total API spend when available.]

## Skill Version(s):

0.1.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
