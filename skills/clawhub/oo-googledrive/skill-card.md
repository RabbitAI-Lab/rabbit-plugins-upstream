## Description:

Enables agents to operate Google Drive through the OOMOL `googledrive` connector and `oo` CLI for reading, creating, updating, and deleting Drive data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use this skill when they need an agent to inspect Google Drive metadata, list or retrieve files, manage collaboration objects, or perform confirmed state-changing Drive actions through an already connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change Google Drive state, including files, shared drives, comments, replies, labels, permissions, revisions, and trash.

Mitigation: Confirm the exact payload and effect with the user before running write actions, and inspect the live connector schema before constructing the payload.

Risk: Destructive actions can permanently delete Drive content, comments, replies, revisions, permissions, shared drives, or trash contents.

Mitigation: Get explicit user approval for the target and operation before any destructive action, and use read/list actions first when needed to verify the target.

Risk: The connector acts on the user's connected Google Drive account.

Mitigation: Install and use the skill only when the user accepts this account-level access, and review prompts carefully before approving uploads, deletions, permission changes, or other state-changing actions.

## Reference(s):

- [Google Drive product page](https://workspace.google.com/products/drive/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Google Drive skill on ClawHub](https://clawhub.ai/oomol/skills/oo-googledrive)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses use JSON with `data` and `meta.executionId`; write and destructive actions require user confirmation before execution.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
