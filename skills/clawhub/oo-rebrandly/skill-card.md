## Description:

Use this skill for Rebrandly requests involving reading, creating, updating, and deleting branded short-link data instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Rebrandly branded short links through an OOMOL-connected Rebrandly account, including creating, inspecting, listing, updating, and soft-deleting links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute downloaded scripts.

Mitigation: Review setup instructions before installation and prefer installing the oo CLI from a verified official package or downloaded installer with integrity checks.

Risk: Some Rebrandly actions create, update, or soft-delete branded links.

Mitigation: Require explicit user approval before running write or destructive Rebrandly actions, and confirm the target and payload before execution.

Risk: Incorrect payloads may produce unintended Rebrandly changes.

Mitigation: Inspect the live connector schema before building each action payload.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-rebrandly)
- [Rebrandly homepage](https://www.rebrandly.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Rebrandly connection page](https://console.oomol.com/app-connections?provider=rebrandly)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, text]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
