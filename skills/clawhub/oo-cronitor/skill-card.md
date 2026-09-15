## Description:

Cronitor lets agents inspect action schemas and manage Cronitor monitors through OOMOL's oo CLI instead of calling the Cronitor API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to list, retrieve, create, update, and delete Cronitor monitors in an OOMOL-connected Cronitor account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes commands that execute remote installer scripts.

Mitigation: Use an official package manager or verified installer path where possible, inspect downloaded scripts before running them, and avoid approving automated execution of remote installers.

Risk: The skill can create, update, and delete Cronitor monitors.

Mitigation: Confirm the exact payload, monitor key, and expected effect before approving write or destructive actions.

## Reference(s):

- [Cronitor homepage](https://cronitor.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Cronitor Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-cronitor)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include JSON payloads for oo connector actions and approval prompts for write or destructive operations.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
