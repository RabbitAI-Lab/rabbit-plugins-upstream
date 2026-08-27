## Description:

Compresses and manages agent context through Neural-Compressed Markdown state files so long sessions can preserve objectives, status, decisions, critical knowledge, and next steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tutankamun23](https://clawhub.ai/user/tutankamun23)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to compress project or session state into compact NCM files and reload that state for continuity across large or long-running sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may rewrite or prune project state files automatically without clear confirmation, backup behavior, or path limits.

Mitigation: Use it only on a dedicated state file, keep version control or backups enabled, explicitly scope writable paths, and avoid auto mode unless file modification boundaries are clear.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tutankamun23/skills/context-compressor)
- [Publisher profile](https://clawhub.ai/user/tutankamun23)
- [NCM structure template](artifact/assets/templates/ncm_structure.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and compact NCM-tagged text with command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May rewrite and prune target state files when compress or auto modes are used.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
