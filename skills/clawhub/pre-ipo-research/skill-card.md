## Description:

Query the public Pre-IPO Observer for Jarsy Private Equity Live and Presale assets, including valuations, trade availability, and freshness timestamps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hackstoic](https://clawhub.ai/user/hackstoic)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts use this skill to find, screen, compare, and summarize Jarsy Private Equity Live and Presale assets using public point-in-time market snapshot data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Point-in-time financial market data may be mistaken for investment advice or proof that trades are executable.

Mitigation: Label data as Jarsy snapshot data, include freshness timestamps, and avoid investment advice, execution claims, jurisdictional availability claims, or current-valuation claims when the snapshot is stale.

Risk: Public API errors or stale data could lead to unsupported answers if replaced with remembered values.

Mitigation: Report that current public data is unavailable when the API fails and do not substitute remembered values.

Risk: Administrative refresh behavior or credentials could expand the skill beyond its reviewed read-only posture.

Mitigation: Do not call protected refresh endpoints, ask for refresh credentials, scrape Jarsy, or bypass authentication.

## Reference(s):

- [Pre-IPO Observer public API](references/api.md)
- [Pre-IPO Observer API](https://preipo.polyos.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown research summaries with optional raw JSON from the bundled query client]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses should identify Jarsy as the source, separate snapshot import time from per-asset record time, and state when values are unavailable.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
