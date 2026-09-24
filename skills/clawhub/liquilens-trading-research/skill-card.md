## Description:

Prepare a source-backed trading research brief with dollar-funding context, public bank evidence and position-sized BTC exit estimates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beepboop2025](https://clawhub.ai/user/beepboop2025)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to prepare source-backed financial research briefs for macro preparation, counterparty research, public bank evidence review, and market-depth questions. It preserves source dates, limitations, counterevidence, and missing data rather than converting evidence into trading or safety assurances.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research questions, referenced public entities, and position sizes may be sent to LiquiLens, Seiche, and Undertow MCP services.

Mitigation: Use the skill only with inputs suitable for those listed services, and avoid private or sensitive trading information unless the operator has approved that data sharing.

Risk: Research briefs may be mistaken for trading instructions, portfolio recommendations, credit ratings, deposit-safety assurances, or executable venue quotes.

Mitigation: Treat the output as research evidence only and require independent review before any financial, trading, compliance, or deposit-safety decision.

Risk: Missing, stale, restricted, or unavailable evidence can lead to incomplete analysis.

Mitigation: Keep failed sections visible, preserve source dates and limitations, and do not fill unavailable evidence with zero or invented values.

## Reference(s):

- [OpenClaw LiquiLens Agent Setup](https://liquilens.in/agents/openclaw/)
- [LiquiLens Trading Research on ClawHub](https://clawhub.ai/beepboop2025/skills/liquilens-trading-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Configuration guidance]

**Output Format:** [Source-backed research brief with sections for each requested product, including source dates, URLs, evidence, counterevidence, limitations, and visible failed sections.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require OpenClaw MCP configuration for Seiche, LiquiLens, and Undertow; no credentials are required by the skill.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
