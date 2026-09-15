## Description:

Shipday (shipday.com). Use this skill for Shipday requests that read, create, update, or delete delivery order data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to manage Shipday delivery orders, carriers, and order progress from an OOMOL-connected account. It supports read, write, and destructive Shipday actions while requiring schema inspection and confirmation before state-changing operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes inline remote installer commands for the oo CLI.

Mitigation: Review the oo CLI installation path and prefer a verified, pinned, or package-manager source before running setup.

Risk: Shipday create, edit, and delete actions can modify or remove delivery records.

Mitigation: Inspect the live action schema, confirm the exact payload and intended effect with the user, and require explicit approval before destructive actions.

## Reference(s):

- [ClawHub Shipday Skill](https://clawhub.ai/oomol/skills/oo-shipday)
- [Shipday Homepage](https://www.shipday.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing Shipday action payloads.]

## Skill Version(s):

1.0.4 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
