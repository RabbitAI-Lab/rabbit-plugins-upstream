## Description:

Ghost (ghost.org). Use this skill for ANY Ghost request - reading, creating, and updating data. Whenever a task involves Ghost, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and site operators use this skill to operate connected Ghost sites through the OOMOL oo CLI. It supports reading published posts, pages, authors, tags, and settings, and it requires confirmation before state-changing Ghost actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote shell and PowerShell installer pipelines for the oo CLI.

Mitigation: Use an official signed or packaged installation method when available, verify the installer before execution, and avoid running installer pipelines from an elevated shell.

Risk: Ghost state-changing actions can modify site content or settings when the connector action supports writes.

Mitigation: Inspect the live action schema first and confirm the exact payload and expected effect with the user before running any write or destructive action.

## Reference(s):

- [ClawHub Ghost Skill](https://clawhub.ai/oomol/skills/oo-ghost)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Ghost Homepage](https://ghost.org)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include Ghost connector JSON results with execution metadata from the oo CLI.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
