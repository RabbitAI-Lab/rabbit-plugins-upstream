## Description:

Directory Organizer helps an agent classify files in a local directory by extension into category folders, previewing moves by default and applying them only when requested.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, operators, and agent users can use this skill to preview and execute local directory cleanup by grouping common file types into named folders. It is intended for everyday file organization workflows where the user can review the proposed moves before applying them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Global installation and local file-moving behavior can affect user files if the script is trusted or applied without review.

Mitigation: Review the script before global installation, prefer a pinned commit or local manual install, run dry-run first, and back up important folders before using --apply.

Risk: Applying the organizer in a directory that already has category folders may move files into locations with existing names.

Mitigation: Avoid --apply in directories where category subfolders may already contain files with the same names, or inspect and resolve those folders before applying moves.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhaoxinghua09-cell/skills/dir-organizer)
- [Publisher Homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Plain text or JSON command output, with Markdown guidance in the skill instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The script is dry-run by default and returns deterministic directory organization plans; --apply performs file moves.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
