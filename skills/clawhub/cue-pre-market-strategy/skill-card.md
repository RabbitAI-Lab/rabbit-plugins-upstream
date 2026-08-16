## Description:

Generates a trader-oriented pre-market strategy brief with overnight event scanning, A-share impact mapping, industry-chain transmission analysis, theme ranking, risk notes, and source links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill before market open to request a structured Cue-generated research brief covering overnight catalysts, A-share mappings, industry-chain impacts, ranked themes, and risk signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, research requests, and generated requests are sent to the external Cue service and may involve external data sources.

Mitigation: Do not include secrets, proprietary positions, account details, or internal research unless the user accepts sending that information to Cue.

Risk: The workflow depends on an external runner and local API-key configuration.

Mitigation: Verify the external runner source and configure Cue API credentials deliberately before running the install or execution flow.

Risk: Market research quality and freshness depend on Cue service availability and the external data sources it uses.

Mitigation: Review source links and treat the report as research input rather than a sole basis for trading decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-pre-market-strategy)
- [Publisher profile](https://clawhub.ai/user/panting09266-ai)
- [Cue service](https://cuecue.cn)
- [Cue runner repository referenced by the skill](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror referenced by the skill](https://gitee.com/sensedeal/cue-skills)
- [Example Cue report](https://cuecue.cn/share/jwhaQSVxNzzWYOvHmt-jO)

## Skill Output:

**Output Type(s):** [markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown report with source links, plus shell command and configuration guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports can optionally be converted to DOCX or PDF with pandoc when available.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
