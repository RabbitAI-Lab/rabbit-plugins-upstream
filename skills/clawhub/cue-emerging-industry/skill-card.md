## Description:

用 Cue 一键梳理陌生赛道的行业天花板、竞争格局与核心商业模式，帮助用户快速建立新兴产业认知框架并映射 IPO/并购中常见的合规风险与法律争议点。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business, legal, investment, or corporate development teams use this skill to request structured Cue research on unfamiliar emerging industries, including market ceiling, competitive landscape, business models, and IPO or M&A compliance risks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Cue as an external research service and requires a Cue API key to be sent to cuecue.cn.

Mitigation: Install only when use of the external Cue service is acceptable; protect the Cue API key and avoid submitting confidential or regulated topics unless the user's Cue account and data handling terms permit it.

Risk: Generated research reports are third-party content whose quality and timeliness depend on Cue and external data sources.

Mitigation: Review important market, legal, IPO, and M&A claims against primary sources before relying on the report for business or legal decisions.

Risk: The skill directs the agent to follow a rigid delivery workflow, including raw report delivery and account-credit guidance.

Mitigation: Override the workflow when the user requests cancellation, summarization, link omission, or a neutral handling of insufficient-credit errors.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-emerging-industry)
- [Cue platform](https://cuecue.cn)
- [Cue API key management](https://cuecue.cn/api-key)
- [Cue runner repository referenced by the skill](https://github.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report with source links, plus shell command and configuration guidance when setup or troubleshooting is needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are delivered as third-party Cue content and may include a Cue share link when an actual run returns a conversation ID.]

## Skill Version(s):

1.0.8 (source: ClawHub release evidence; artifact frontmatter reports 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
