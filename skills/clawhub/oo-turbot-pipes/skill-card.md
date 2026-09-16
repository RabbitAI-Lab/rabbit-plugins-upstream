## Description:

Turbot Pipes (turbot.com). Use this skill for ANY Turbot Pipes request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to query Turbot Pipes through an OOMOL-connected account, inspect connector schemas, and run supported connector actions with JSON payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that could execute unreviewed code if run automatically.

Mitigation: Require a human to install or verify the official installer or a pinned package-manager path before allowing agent use.

Risk: The execute_query action sends SQL through the connected Turbot Pipes account, and read-only enforcement is not proven by the evidence.

Mitigation: Review the SQL payload and account scopes before execution; treat queries as requiring user review unless the connector is known to enforce read-only behavior.

## Reference(s):

- [ClawHub Turbot Pipes Skill](https://clawhub.ai/oomol/skills/oo-turbot-pipes)
- [Turbot Pipes](https://turbot.com/pipes)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are expected as JSON containing data and execution metadata.]

## Skill Version(s):

1.0.2 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
