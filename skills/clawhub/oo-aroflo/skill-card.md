## Description:

AroFlo helps an agent search and read AroFlo data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers with an OOMOL-connected AroFlo account use this skill to inspect action schemas, retrieve individual clients, tasks, and users, list those records with supported filters, and check API health.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Review and independently verify the oo CLI installer source before running setup commands; prefer signed or checksum-verified installation methods.

Risk: The skill depends on connected AroFlo credentials and live connector schemas.

Mitigation: Inspect the live action schema before building payloads and keep execution limited to the documented read actions unless the user explicitly approves a state-changing action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-aroflo)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [AroFlo homepage](https://aroflo.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions return JSON responses with data and meta.executionId when run successfully.]

## Skill Version(s):

1.0.2 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
