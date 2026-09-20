## Description:

Eraser (eraser.io). Use this skill for ANY Eraser request: reading, creating, updating, and deleting data through OOMOL's Eraser connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent manage Eraser files and diagrams through an OOMOL-connected account. It supports listing and reading Eraser content, creating and updating files or diagrams, rendering diagrams from DSL, and generating diagrams from prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup fallback includes remote shell installer commands for the oo CLI.

Mitigation: Install the oo CLI through verified official steps yourself, and do not let an agent run curl-to-bash or PowerShell iex installers automatically.

Risk: The skill can create, update, archive, or delete Eraser files and diagrams.

Mitigation: Review and explicitly approve the target, payload, and expected effect before any write or destructive Eraser action runs.

Risk: The skill operates through OOMOL as an intermediary for an Eraser account.

Mitigation: Install and use the skill only when that account and credential-handling model is acceptable for the workspace.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-eraser)
- [Eraser homepage](https://www.eraser.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent output may include proposed oo CLI commands, Eraser action payloads, and summaries of connector responses.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
