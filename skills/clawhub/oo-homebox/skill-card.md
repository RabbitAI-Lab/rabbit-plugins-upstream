## Description:

HomeBox (homebox.software). Use this skill for ANY HomeBox request -- reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate HomeBox through an OOMOL-connected account, including reading inventory data and creating, updating, or deleting entities, tags, entity types, attachments, and maintenance entries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions may run remote installer scripts directly through a shell.

Mitigation: Review the oo CLI installation path before running it and prefer a pinned or verified installer when available.

Risk: HomeBox write and destructive actions can change or delete user inventory data.

Mitigation: Confirm the exact action, target, payload, and expected effect before allowing write or destructive commands to proceed.

## Reference(s):

- [HomeBox homepage](https://homebox.software)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub HomeBox skill page](https://clawhub.ai/oomol/skills/oo-homebox)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before action payload construction.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
