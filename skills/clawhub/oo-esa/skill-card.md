## Description:

Provides agent access to esa (esa.io) for reading, creating, updating, and deleting data through OOMOL's oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to let an agent search, read, create, update, and manage esa posts, comments, categories, tags, attachments, team metadata, and related esa content through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The oo CLI operates on esa with the permissions of the connected account.

Mitigation: Install and use the skill only when that account-level access is acceptable for the intended workspace and task.

Risk: Write and destructive actions can change, archive, delete, duplicate, or restore esa content.

Mitigation: Confirm the exact target, payload, and expected effect with the user before approving write or destructive actions.

Risk: Remote installer commands may execute code before the user has inspected it.

Mitigation: Prefer OOMOL's official or manual install guidance, or inspect the installer before running remote install commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-esa)
- [esa homepage](https://esa.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Markdown, JSON, Guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [State-changing and destructive esa actions require user confirmation before execution.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
