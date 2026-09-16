## Description:

Pinata (pinata.cloud). Use this skill for Pinata requests involving reading, creating, updating, and deleting data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Pinata files, groups, pin requests, and metadata through the OOMOL `oo` CLI. It supports read operations as well as state-changing and destructive Pinata actions that require confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup documents direct remote installer execution without integrity verification.

Mitigation: Use an official, versioned oo CLI download, verify integrity when available, and review installer contents before execution.

Risk: Write and destructive Pinata actions can change or remove account data.

Mitigation: Inspect the live action schema, confirm the exact payload and target with the user, and require explicit approval before destructive actions.

Risk: The skill depends on OOMOL as the Pinata connector and credential broker.

Mitigation: Install only when that connector model is acceptable, and verify the OOMOL account connection and scopes before running actions.

## Reference(s):

- [ClawHub Pinata Skill](https://clawhub.ai/oomol/skills/oo-pinata)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Pinata](https://pinata.cloud)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before action execution; write and destructive actions require confirmation.]

## Skill Version(s):

1.0.2 (source: release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
