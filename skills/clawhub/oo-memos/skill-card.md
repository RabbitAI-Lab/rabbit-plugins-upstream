## Description:

Memos helps agents read, create, update, and delete Memos data through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and end users with an OOMOL-connected Memos account use this skill to manage Markdown memos, attachments, and visible users. It supports read, write, and destructive Memos actions while requiring confirmation before state-changing operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote pipe-to-shell installers for the oo CLI.

Mitigation: Prefer a verified package or manual download with checksum or signature review before installing the CLI.

Risk: The skill can create, update, overwrite, or delete Memos data and attachments.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write or destructive actions.

Risk: The skill depends on OOMOL as a connector for the user's Memos account.

Mitigation: Install only when the user is comfortable using OOMOL for the connected Memos account and review connection state before retrying failed actions.

## Reference(s):

- [Memos homepage](https://usememos.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Markdown, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before requests and requires user confirmation for write or destructive actions.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
