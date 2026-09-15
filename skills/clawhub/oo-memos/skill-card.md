## Description:

This skill helps agents manage Memos through the OOMOL oo CLI connector, including reading, creating, updating, deleting, and managing attachments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Memos through an OOMOL-connected account, including reading, creating, updating, deleting, and attaching content while relying on live connector schemas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructions include direct execution of remote installer scripts for the oo CLI.

Mitigation: Review setup commands before installing and prefer a verified or package-manager installation path when available.

Risk: Write and destructive actions can modify or delete Memos data.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [Memos homepage](https://usememos.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-memos)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May issue oo CLI connector schema and run commands that return JSON responses.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
