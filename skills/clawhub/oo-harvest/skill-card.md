## Description:

Harvest (getharvest.com). Use this skill for ANY Harvest request: reading, creating, updating, and deleting data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to inspect Harvest action schemas, read Harvest clients, projects, tasks, users, assignments, and time entries, and manage time entries through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of remote installer scripts for the OOMOL CLI.

Mitigation: Review the OOMOL CLI installation path before installing; prefer a verified package or pinned release and inspect downloaded installer content.

Risk: The skill can create, update, start, stop, restart, and delete Harvest time entries.

Mitigation: Confirm the exact target, payload, and effect with the user before write actions, and require explicit approval before destructive delete actions.

## Reference(s):

- [Harvest skill on ClawHub](https://clawhub.ai/oomol/skills/oo-harvest)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Harvest homepage](https://www.getharvest.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute OOMOL oo CLI commands that return JSON responses from Harvest connector actions.]

## Skill Version(s):

1.0.3 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
