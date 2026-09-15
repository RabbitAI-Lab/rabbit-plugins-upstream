## Description:

Operate Sender through the OOMOL oo CLI to inspect action schemas and read, create, update, or remove Sender resources with confirmation for changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Sender subscribers, groups, custom fields, campaigns, and automation workflows through an authenticated OOMOL connector without handling raw Sender API tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that could execute mutable code on the user's machine.

Mitigation: Review the install steps first and prefer a pinned, verifiable oo CLI package or official instructions that allow inspection before execution.

Risk: Sender write or destructive actions can change subscriber, group, field, campaign, or workflow data.

Mitigation: Inspect the live action schema, confirm the exact payload and expected effect with the user, and require explicit approval for destructive removals.

## Reference(s):

- [ClawHub Sender skill page](https://clawhub.ai/oomol/skills/oo-sender)
- [Sender homepage](https://www.sender.net)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live schema inspection before constructing payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
