## Description:

Precoro (precoro.com). Use this skill for ANY Precoro request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and operators who manage purchasing workflows use this skill to inspect live Precoro connector schemas and read or update Precoro data such as catalog items, purchase orders, suppliers, users, and warehouses through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes direct execution of remote installer scripts.

Mitigation: Review OOMOL's official install documentation, prefer a non-pipe-to-shell installation path when possible, and install only from trusted OOMOL distribution channels.

Risk: Precoro actions may operate with the connected account's scopes and can include state-changing operations.

Mitigation: Confirm the exact action, target record, payload, and expected effect with the user before running any write-capable or destructive action.

Risk: The skill depends on a correctly scoped and trusted OOMOL-connected Precoro account.

Mitigation: Use the minimum Precoro connection scope needed for the task and re-check authorization or connection errors before retrying commands.

## Reference(s):

- [ClawHub Precoro skill](https://clawhub.ai/oomol/skills/oo-precoro)
- [Precoro homepage](https://precoro.com/)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are expected as JSON from the oo CLI; action schemas should be inspected before payload construction.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
