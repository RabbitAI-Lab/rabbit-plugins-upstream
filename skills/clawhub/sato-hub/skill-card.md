## Description:

Sato Hub lets agents query a daily rebuilt index of onchain-agent tooling, protocols, payment rails, identity standards, venues, agent skills, adoption numbers, and Agent Passports through a hosted MCP server, REST endpoints, or a bundled curl script.

This skill is ready for commercial/non-commercial use.

## Publisher:

[satohubai](https://clawhub.ai/user/satohubai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and external users use this skill to discover, compare, and cite onchain-agent infrastructure, agent-economy metrics, Sato Score records, Preflight checks, and Sato Route plans before installing, integrating, trading, launching, or routing agent tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and routing inputs are sent to the hosted Sato Hub MCP endpoint.

Mitigation: Install only when sharing those inputs with Sato Hub is acceptable, and avoid sending private wallet, trading, launch, or project data that should not leave the local environment.

Risk: Finance-adjacent route outputs can include swap calldata, launch configuration, x402 routing, build plans, or venue choices that are advisory.

Mitigation: Independently review fees, recipients, source URLs, generated files, and route assumptions before signing, deploying, paying, submitting, or acting on the output.

Risk: The skill is described as mostly read-only, but server evidence flags write-capable remote tools for watch subscriptions, project submissions, and agent passport registration.

Mitigation: Use write tools only when intentionally creating a subscription, submitting a project, or registering an agent passport with Sato Hub.

Risk: Sato Score, Preflight, and Sato Route outputs are informational signals and not security audits, safety guarantees, quality grades, or return forecasts.

Mitigation: Carry the tool caveats into downstream answers and require separate review before relying on the results for security-sensitive or financial decisions.

## Reference(s):

- [Server-resolved GitHub import](https://github.com/satohubai/sato-hub-skill/tree/main/skills/sato-hub)
- [ClawHub skill page](https://clawhub.ai/satohubai/skills/sato-hub)
- [Sato Hub MCP documentation](https://satohub.ai/mcp)
- [Sato Hub MCP endpoint](https://satohub.ai/api/mcp)
- [Sato Hub MCP tools reference](references/tools.md)
- [Sato Hub REST reference](references/rest.md)
- [Sato Hub worked examples](references/examples.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or JSON responses with optional inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses outbound network access to the hosted Sato Hub endpoint; catalog data is CC-BY-4.0 with attribution to data by satohub.ai.]

## Skill Version(s):

0.1.0 (source: release metadata; artifact frontmatter states 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
