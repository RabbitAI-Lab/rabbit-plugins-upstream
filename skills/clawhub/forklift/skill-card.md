## Description:

Forklift expert helps agents answer Chinese and China-oriented forklift questions covering brands, product selection, standards, safety, maintenance, troubleshooting, used equipment evaluation, parts, market trends, and sales updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yangpf6698](https://clawhub.ai/user/yangpf6698)

### License/Terms of Use:

MIT

## Use Case:

External users, operators, maintenance teams, buyers, and agents use this skill to answer forklift-domain questions and produce structured guidance for selection, diagnosis, standards checks, maintenance planning, and market or sales summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is China-oriented and may not fit non-Chinese regulatory, market, or operating contexts without review.

Mitigation: Route it only for clear forklift intent and verify region-specific safety, legal, and purchasing decisions against official local sources.

Risk: Forklift model parameters, standards status, sales rankings, and market data can become stale.

Mitigation: Use current web search or official sources for time-sensitive values before relying on the answer.

Risk: AGV and general market questions may be routed too broadly if forklift intent is ambiguous.

Mitigation: Configure routing to require clear forklift or directly related industrial-vehicle context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yangpf6698/skills/forklift)
- [Skill instructions](artifact/SKILL.md)
- [Usage guide](artifact/usage-guide.md)
- [Brand directory](artifact/brands.md)
- [Forklift standards](artifact/standards.md)
- [Standard retrieval workflow](artifact/standard-retrieval.md)
- [Safety and regulation guide](artifact/safety-regulation.md)
- [Selection guide](artifact/selection-guide.md)
- [Fault diagnosis guide](artifact/fault-diagnosis.md)
- [Maintenance plan](artifact/maintenance-plan.md)
- [Parts and consumables guide](artifact/parts-consumables.md)
- [Used forklift evaluation guide](artifact/used-forklift-evaluation.md)
- [Market trends guide](artifact/market-trends.md)
- [Sales news workflow](artifact/sales-news.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown answers with tables, checklists, diagnostic steps, and optional ASCII charts for sales summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to use web search for current model parameters, standards status, sales rankings, and market data.]

## Skill Version(s):

2.0.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
