## Description:

Prepare a source-backed trading research brief with dollar-funding context, public bank evidence and position-sized BTC exit estimates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beepboop2025](https://clawhub.ai/user/beepboop2025)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts and developers use this skill to prepare financial research briefs that combine dollar-funding context, public bank evidence and position-sized BTC exit-cost estimates while preserving source dates, missing data and limitations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research queries are sent to external LiquiLens, Seiche and Undertow MCP services.

Mitigation: Install and use the skill only when those service disclosures are acceptable for the specific research questions being asked.

Risk: Financial research output could be mistaken for trading instructions, credit ratings or deposit-safety assurance.

Mitigation: Treat the brief as source-backed research evidence; do not use it as order execution, portfolio recommendation, credit rating or compliance approval.

Risk: Missing, stale, restricted or unavailable evidence can distort conclusions if treated as current or as zero.

Mitigation: Preserve source dates, coverage states and limitations, and keep failed or unavailable sections visible.

Risk: Repeated use can exceed public endpoint fair-use limits.

Mitigation: Avoid background polling and retry loops, schedule only at the owner's requested cadence and stop or reduce calls when rate-limited.

## Reference(s):

- [LiquiLens OpenClaw setup](https://liquilens.in/agents/openclaw/)
- [ClawHub skill page](https://clawhub.ai/beepboop2025/skills/liquilens-trading-research)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, configuration, guidance]

**Output Format:** [Markdown research brief, optional JSON brief and OpenClaw MCP configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Briefs should preserve source dates, URLs, evidence states, counterevidence, limitations and failed sections.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
