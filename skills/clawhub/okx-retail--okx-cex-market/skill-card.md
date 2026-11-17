## Description:

Provides read-only access to OKX public market data and technical indicators through the OKX CLI, without API credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[okx-retail](https://clawhub.ai/user/okx-retail)

### License/Terms of Use:

MIT-0

## Use Case:

External users can query public OKX prices, instruments, derivatives data, screeners, and technical indicators. The skill returns market data and leaves interpretation and trading decisions to the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review had medium confidence because some reference checks were incomplete, and it noted a low-probability confirmation concern around market commands.

Mitigation: Review the relevant command references and inspect market-command behavior before installing or running the skill.

## Reference(s):

- [OKX](https://www.okx.com)
- [ClawHub skill release](https://clawhub.ai/okx-retail/skills/okx-cex-market)
- [Price & Market Data Commands](artifact/references/price-data-commands.md)
- [Derivatives Commands](artifact/references/derivatives-commands.md)
- [Instrument Commands](artifact/references/instrument-commands.md)
- [Indicator Commands](artifact/references/indicator-commands.md)
- [Cross-Skill Workflows](artifact/references/workflows.md)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Text tables or raw JSON market-data responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only public market data; no API credentials required. Indicator results are numerical values, not recommendations.]

## Skill Version(s):

1.5.1 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
