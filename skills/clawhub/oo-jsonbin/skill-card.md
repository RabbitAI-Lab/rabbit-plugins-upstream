## Description:

JSONBin.io helps agents read, create, update, and delete JSONBin bins through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage JSONBin.io records from an agent, including reading existing bins and confirming create, update, or delete payloads before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes remote installer commands for the oo CLI.

Mitigation: Install the oo CLI through a trusted, reviewed method instead of allowing an agent to run remote installer scripts automatically.

Risk: Create, update, and delete actions can change or remove JSONBin.io data.

Mitigation: Confirm the exact action, target bin, and JSON payload with the user before execution, and require explicit approval for destructive deletion.

Risk: Connector action schemas may change over time.

Mitigation: Inspect the live connector schema before constructing payloads so requests match the current action contract.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-jsonbin)
- [JSONBin.io homepage](https://jsonbin.io/)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
