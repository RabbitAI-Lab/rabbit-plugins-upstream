## Description:

Analyzes publicly disclosed A-share equity mutual funds across manager history, performance attribution, investment style, risk, holdings, fees, and scale to support due-diligence decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External fund investors, advisors, and researchers use this skill to assess publicly disclosed China A-share equity funds and compare fund managers using historical performance, style, risk, holdings, fees, and scale. It supports research and due diligence, not future-performance predictions or buy/sell timing advice.

### Deployment Geography for Use:

Global; analysis scope is publicly disclosed China A-share equity mutual funds.

## Known Risks and Mitigations:

Risk: The security review flags automatic updates to executable code.

Mitigation: Use a reviewed runner revision and make upgrades an explicit choice.

Risk: The security review flags conflicting API-key protection instructions.

Mitigation: Configure the Cue key locally and do not paste it into chat.

Risk: Fund queries are sent to Cue, and research uses service credits.

Mitigation: Tell users before running that their fund query is sent to Cue and may use service credits.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/panting09266-ai/skills/cue-fund-due-diligence)
- [Cue service](https://cuecue.cn)
- [Cue API key setup](https://cuecue.cn/api-key?src=clawhub-fund-due-diligence)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Structured Markdown fund due-diligence report with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Covers historical and publicly disclosed information; includes a data cutoff and source links when available.]

## Skill Version(s):

1.0.11 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
