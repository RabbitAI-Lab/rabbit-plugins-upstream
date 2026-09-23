## Description:

Query Sato Hub's daily rebuilt index of onchain-agent tooling, agent-economy measurements, skill disclosures, and Agent Passports through a hosted MCP endpoint or bundled curl script.

This skill is ready for commercial/non-commercial use.

## Publisher:

[satohubai](https://clawhub.ai/user/satohubai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to discover onchain-agent frameworks, wallets, payment rails, MCP servers, skills, and Agent Passports; compare listings; retrieve citable adoption numbers; run Preflight checks; and build route or stack plans. Its outputs should be treated as indexed evidence and operational guidance, not investment, safety, or audit conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP endpoint includes write-capable tools that can change Sato Hub state or prepare unsigned crypto actions despite read-only framing.

Mitigation: Require explicit confirmation before invoking write tools, route generation, swap build-tx, subscriptions, submissions, or agent registration; inspect any unsigned transaction or generated config before signing.

Risk: Sato Score, route output, Preflight verdicts, and observed-success values can be mistaken for safety, quality, uptime, investment, or returns recommendations.

Mitigation: Carry the documented caveats into user-facing answers and do not present scores, verdicts, quotes, or observed checks as audits, guarantees, fills, or financial advice.

Risk: The skill depends on changing external data from satohub.ai.

Mitigation: Cite the relevant Sato Hub record or page, preserve dates and source fields when present, and re-query before time-sensitive decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/satohubai/skills/sato-hub)
- [Sato Hub MCP documentation](https://satohub.ai/mcp)
- [Sato Hub MCP endpoint](https://satohub.ai/api/mcp)
- [MCP tool reference](artifact/references/tools.md)
- [REST fallback reference](artifact/references/rest.md)
- [Worked examples](artifact/references/examples.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or JSON tool results with optional shell commands and REST or MCP request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires outbound network access to satohub.ai; the bundled script uses bash and curl, with jq optional.]

## Skill Version(s):

1.1.1 (source: server release evidence; artifact metadata reports 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
