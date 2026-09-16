## Description:

PassSlot operates PassSlot Wallet pass workflows through an OOMOL-connected account, supporting read, create, update, delete, and installation URL actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to manage PassSlot Wallet passes through an OOMOL-connected account, including listing pass assets, creating passes from templates, updating placeholder values, and deleting passes with confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path can ask users to execute a remote installer script directly in a shell.

Mitigation: Install the oo CLI only after independently verifying the installer source, preferring an official signed package, a pinned release, or a manually inspected installer.

Risk: The skill can create, update, and permanently delete PassSlot Wallet pass data.

Mitigation: Confirm the exact target, payload, and expected effect with the user before any write or destructive action.

## Reference(s):

- [PassSlot homepage](https://www.passslot.com)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live connector schema inspection before building action payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: skill frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
