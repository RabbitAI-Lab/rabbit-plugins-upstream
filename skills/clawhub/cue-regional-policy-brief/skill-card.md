## Description:

用 Cue 聚合指定区域的政策发布、招商动态及市场数据，筛选高价值合规线索与潜客名单，并产出结构化周度情报简报。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Law firm BD teams use this skill to request a regional policy and business-opportunity brief for a target area. It helps identify policy changes, investment-promotion activity, compliance leads, prospective client lists, demand hypotheses, and source links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on external Cue runner code that is not pinned by the release evidence.

Mitigation: Review or pin the runner before execution and re-check it during updates.

Risk: Queries, returned reports, and Cue share links may expose confidential client, strategy, or personal data to an external service.

Mitigation: Use only with authorized data and review reports and links before forwarding them.

Risk: The workflow directs agents to deliver Cue report content without filtering and includes payment or referral prompts.

Mitigation: Review generated reports and user-facing prompts before sharing them in professional or client contexts.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/panting09266-ai/skills/cue-regional-policy-brief)
- [Cue platform](https://cuecue.cn)
- [Cue API key management](https://cuecue.cn/api-key)
- [Cue payment page](https://cuecue.cn/pay)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown report with source links and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a Cue share link and a local Markdown report path when the Cue runner returns a conversation id.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter lists 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
