## Description:

FinChina helps agents search and read FinChina financial, enterprise, and risk-analysis data through an OOMOL-connected account and the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to discover FinChina tool schemas, run FinChina data queries, and retrieve company profiles, financial indicators, metadata, enumerations, and enterprise-risk information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may ask an agent to execute remote installer scripts without integrity checks.

Mitigation: Review the oo CLI installation path first; prefer an official manual installer with verification, or inspect downloaded scripts before execution.

Risk: Connector queries use the user's OOMOL-connected FinChina account and may consume credits.

Mitigation: Inspect the live action schema before each request, send only the intended payload, and confirm cost-sensitive queries with the user when appropriate.

Risk: If FinChina exposes write or destructive actions, incorrect payloads could change or remove data.

Mitigation: Confirm the exact payload and expected effect before write actions, and require explicit approval before destructive actions.

## Reference(s):

- [ClawHub FinChina Skill](https://clawhub.ai/oomol/skills/oo-finchina)
- [FinChina Homepage](https://mcp.finchina.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance, Configuration instructions]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses from connector runs include data and a meta.executionId value; FinChina queries may consume account credits.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
