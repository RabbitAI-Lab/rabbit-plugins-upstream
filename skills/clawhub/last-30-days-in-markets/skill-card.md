## Description:

Creates an auditable 30-day US equities research brief from SentiSense market mood, story cluster, signal, market summary, and earnings API data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and market analysts use this skill to generate an auditable market catch-up brief for US equities or a single ticker, using fetched SentiSense data with coverage and freshness noted.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends a user-provided SentiSense API key to SentiSense over HTTPS and may make multiple API calls per brief.

Mitigation: Use only a SentiSense API key intended for this service, review quota use, and avoid exposing the key in prompts, logs, or outputs.

Risk: Market summaries may be mistaken for trading advice or automated trading signals.

Mitigation: Present outputs as research and education only, preserve coverage and freshness notes, and do not use the skill for trading, purchases, wallet access, or automated orders.

Risk: Generated briefs can overstate unsupported market claims if data coverage is incomplete or stale.

Mitigation: Include actual coverage windows, generation ages, and omit claims not supported by fetched SentiSense responses.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/last-30-days-in-markets)
- [SentiSense API Reference](https://sentisense.ai/skill.md)
- [SentiSense Website](https://sentisense.ai)
- [SentiSense API Key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown research brief with dated claims, coverage notes, and source traceability]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY and fetches read-only SentiSense API data over HTTPS; not investment advice.]

## Skill Version(s):

1.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
