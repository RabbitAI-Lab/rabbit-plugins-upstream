## Description:

Dida365 (dida365.com). Use this skill for ANY Dida365 request — reading, creating, updating, and deleting data. Whenever a task involves Dida365, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Dida365 tasks, projects, and habits through an OOMOL-connected account. It supports read actions as well as confirmed create, update, move, complete, and delete actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes direct remote shell installer commands for the OOMOL CLI.

Mitigation: Review the CLI installation method before installing, and prefer official signed package-manager or documented manual installation steps when available.

Risk: The skill can create, update, move, complete, or delete Dida365 data.

Mitigation: Require explicit user approval and confirm the exact target, payload, and expected effect before any write or destructive action.

## Reference(s):

- [Dida365 homepage](https://dida365.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL Dida365 connection](https://console.oomol.com/app-connections?provider=dida365)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-dida365)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May trigger Dida365 API operations through the oo CLI when executed by an agent with user approval.]

## Skill Version(s):

1.0.6 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
