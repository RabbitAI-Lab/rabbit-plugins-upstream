## Description:

XYDC MCP helps agents use the XYDC MCP connector through OOMOL's oo CLI for reading, creating, and updating XYDC marketplace data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect XYDC MCP action schemas and run marketplace research workflows for ASINs, keywords, category insights, rankings, traffic, orders, variations, and trends through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands execute downloaded scripts when installing the oo CLI.

Mitigation: Install the oo CLI only from trusted OOMOL sources and review the install guide or installer script before execution.

Risk: Some XYDC actions can write state or consume credits, including category insight resource generation.

Mitigation: Confirm write, destructive, or credit-consuming actions with the user and avoid automatic retries after timeouts or billing errors.

Risk: Connector calls depend on live action schemas that may change.

Mitigation: Inspect the current action schema before constructing a payload and validate data against that schema.

## Reference(s):

- [XYDC MCP homepage](https://platform.xydc.com/mcp)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-xydc-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, Markdown]

**Output Format:** [Markdown guidance with oo CLI commands and JSON connector payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return XYDC connector data and execution metadata; some actions can consume credits or change connector state.]

## Skill Version(s):

1.0.1 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
