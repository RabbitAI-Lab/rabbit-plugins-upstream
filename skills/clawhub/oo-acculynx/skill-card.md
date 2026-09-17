## Description:

AccuLynx (acculynx.com). Use this skill for AccuLynx requests that read, create, or update data through the OOMOL connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate AccuLynx through an OOMOL-connected account, including listing company settings and calendars, creating contacts and Lead-milestone jobs, and adding or updating initial appointments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes direct execution of internet installer scripts for the oo CLI.

Mitigation: Review setup instructions before installation, prefer a verified oo CLI release or package source, and avoid running downloaded installer scripts directly in a shell unless OOMOL's distribution path is trusted.

Risk: Write actions can create contacts and jobs or add and update initial appointments in AccuLynx.

Mitigation: Use the least privileged AccuLynx API key practical and confirm the exact payload and expected effect with the user before create or update actions run.

## Reference(s):

- [AccuLynx homepage](https://acculynx.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-acculynx)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before actions and returns connector responses with data and execution metadata.]

## Skill Version(s):

1.0.3 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
