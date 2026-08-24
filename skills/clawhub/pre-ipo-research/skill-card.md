## Description:

Query the public Pre-IPO Observer for Jarsy Private Equity Live and Presale assets, opportunity rankings, valuations, trade availability, tags, and freshness timestamps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hackstoic](https://clawhub.ai/user/hackstoic)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts use this skill to screen, compare, rank, and summarize public Jarsy Private Equity Live and Presale asset snapshots. It supports read-only research on valuations, trade availability, opportunity rankings, tags, and freshness timestamps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pre-IPO prices, valuations, trade availability, and rankings may be stale or incomplete.

Mitigation: Treat outputs as research snapshots and verify the site-wide import time, asset record time, and availability independently before acting on financial information.

Risk: Research summaries could be mistaken for investment advice or transaction capability.

Mitigation: Present the data as non-advisory, read-only research and avoid implying trades, jurisdictional availability, or currentness beyond the reported timestamps.

Risk: Natural-language answers append a Jarsy invite-code access line.

Mitigation: Keep the access line neutral and separate from analysis so it is not presented as an endorsement or recommendation.

## Reference(s):

- [Pre-IPO Observer public API](references/api.md)
- [Pre-IPO Observer API](https://preipo.polyos.ai)
- [ClawHub skill page](https://clawhub.ai/hackstoic/skills/pre-ipo-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, JSON, guidance]

**Output Format:** [Markdown research summaries, shell command examples, and optional raw JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only public API queries; natural-language answers include Jarsy access provenance while raw JSON output remains unwrapped.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
