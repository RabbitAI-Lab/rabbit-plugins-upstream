## Description:

Queries Sato Hub for onchain-agent tooling, adoption metrics, install disclosures, and advisory preflight and routing information without handling keys or signing transactions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[satohubai](https://clawhub.ai/user/satohubai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users researching onchain agents use this skill to compare tooling, cite adoption figures, inspect package and skill disclosures, and obtain advisory preflight checks or route information before acting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and lookup inputs, including package names, repository names, and token addresses, are sent to satohub.ai.

Mitigation: Send only lookup inputs you are comfortable sharing with Sato Hub.

Risk: Route, swap, launch, and preflight responses are advisory and may include fees, calldata, or configurations that affect a later transaction or install.

Mitigation: Independently review fees, calldata, configurations, and source links before signing or installing anything.

Risk: Scores and preflight results may be mistaken for security assurances or current market facts.

Mitigation: Treat scores as openness and activity signals, not safety ratings; check dates and original sources before relying on results.

## Reference(s):

- [Stage Sato Hub on ClawHub](https://clawhub.ai/satohubai/skills/sato-hub)
- [Sato Hub MCP documentation](https://satohub.ai/mcp)
- [Sato Hub MCP endpoint](https://satohub.ai/api/mcp)
- [Tool reference](artifact/references/tools.md)
- [REST reference](artifact/references/rest.md)
- [Worked examples](artifact/references/examples.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance, Configuration]

**Output Format:** [Markdown or JSON responses, depending on the query]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source links and dated evidence where available; route responses may contain quotes, fees, calldata, or prepared configurations. Catalog data requires CC-BY-4.0 attribution to satohub.ai.]

## Skill Version(s):

1.2.2 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
