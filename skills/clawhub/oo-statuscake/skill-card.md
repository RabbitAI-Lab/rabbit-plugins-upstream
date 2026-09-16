## Description:

StatusCake helps agents read and manage StatusCake uptime monitoring data and tests through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to manage StatusCake uptime tests through OOMOL, including reading monitoring data and creating, updating, or deleting tests after user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup can run unverified remote installer scripts directly in a shell.

Mitigation: Prefer manually downloading and verifying the installer or using a trusted package manager before installing the oo CLI.

Risk: Create, update, and delete actions can change or remove StatusCake uptime tests.

Mitigation: Confirm the exact target, payload, and expected effect with the user before allowing write or destructive actions.

## Reference(s):

- [ClawHub StatusCake Skill](https://clawhub.ai/oomol/skills/oo-statuscake)
- [StatusCake Homepage](https://www.statuscake.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return JSON responses from oo connector actions, including data and execution metadata.]

## Skill Version(s):

1.0.3 (source: evidence release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
