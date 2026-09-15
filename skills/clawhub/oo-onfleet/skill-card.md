## Description:

Use this skill for Onfleet requests to read, create, update, and delete task data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Onfleet through an OOMOL-connected account, including listing, retrieving, cloning, creating, updating, completing, and deleting tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions execute remote installer scripts directly.

Mitigation: Review the oo CLI installation source before installation and prefer a pinned, verifiable installer or package-manager install.

Risk: Create, update, complete, and delete actions can change or remove Onfleet task data.

Mitigation: Confirm the exact payload, target, and expected effect with the user before write actions, and require explicit approval before destructive deletions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-onfleet)
- [Onfleet homepage](https://onfleet.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, JSON, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; responses include data and execution metadata.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
