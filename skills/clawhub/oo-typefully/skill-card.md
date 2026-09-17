## Description:

Typefully (typefully.com). Use this skill for ANY Typefully request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Typefully drafts and social sets through an OOMOL-connected account. It supports reading account data, listing content, creating or updating drafts, and deleting drafts with explicit confirmation for state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path may execute a remote installer script directly.

Mitigation: Review the installer source and prefer a verified package, signed release, or checksum-checked installer before installing the oo CLI.

Risk: The skill can create, update, or delete Typefully drafts.

Mitigation: Confirm the exact payload, target draft, and intended effect with the user before running write or destructive actions.

Risk: Actions run against the connected Typefully account.

Mitigation: Use the skill only with the intended OOMOL and Typefully account connection, and resolve authentication or scope errors through the documented first-time setup path.

## Reference(s):

- [Typefully homepage](https://typefully.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-typefully)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before execution; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.4 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
