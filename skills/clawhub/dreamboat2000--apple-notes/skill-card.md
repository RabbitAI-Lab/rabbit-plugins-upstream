## Description:

Manage Apple Notes via the `memo` CLI on macOS, including creating, viewing, editing, deleting, searching, moving, and exporting notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dreamboat2000](https://clawhub.ai/user/dreamboat2000)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Apple Notes from an agent on macOS through the memo CLI. It is suited for note creation, retrieval, editing, folder movement, export, and deletion workflows where Apple Notes access has been granted.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The memo CLI requires access to Apple Notes, which may contain sensitive personal or business content.

Mitigation: Install only after reviewing the upstream project and grant Apple Notes Automation access only when the user accepts that access scope.

Risk: Edit, move, export, or delete operations can change or expose notes if the wrong title or folder is selected.

Mitigation: Confirm note titles, destination folders, and destructive actions before running memo commands.

Risk: The skill depends on a local third-party CLI and cannot manage notes containing images or attachments.

Mitigation: Prefer a known memo release, verify the binary installation path, and fall back to Notes.app for attachment-heavy notes.

## Reference(s):

- [memo CLI project](https://github.com/antoniorodr/memo)
- [Apple Notes skill page](https://clawhub.ai/dreamboat2000/skills/apple-notes)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and concise operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires macOS, Apple Notes.app access, terminal interaction for some actions, and the memo CLI.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
