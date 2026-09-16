## Description:

用 Cue 实时扫描今日 A 股热点板块与近 24h 催化资讯，拆解盘中催化逻辑与受益方向，助短线交易者紧跟市场热钱流向。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External traders and market researchers use this skill to request Cue-generated A-share hotspot and catalyst reports, including sector momentum, catalyst logic, beneficiary sectors, capital-flow signals, and source links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote Cue report content may be reproduced too directly or treated as authoritative market guidance.

Mitigation: Review generated reports before use, preserve source links, and avoid presenting the output as personalized investment advice.

Risk: Cue share links and external-service responses may be added to final answers.

Mitigation: Only include share links derived from an actual completed run and validate the reported conversation identifier before sharing.

Risk: Referral, payment, scheduling, or diagnostic guidance may appear in user-facing responses.

Mitigation: Review the skill before installation and configure agent policy to suppress unwanted promotional or operational flows.

Risk: The skill depends on a Cue API key and external service availability.

Mitigation: Use a limited Cue API key, avoid untrusted proxies for diagnostics, and treat service outages or empty results as non-fatal conditions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-hotspot-tracker)
- [Cue platform](https://cuecue.cn)
- [Cue API key management](https://cuecue.cn/api-key)
- [Cue subscription page](https://cuecue.cn/pay)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report with source links and optional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The report should include the Cue original report link only when it is derived from an actual completed run.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter reports 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
