## Description:

AppVeyor helps agents search and read AppVeyor build, project, environment, role, and user data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect AppVeyor projects, build artifacts, deployment environments, roles, and users through an OOMOL-connected AppVeyor account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes pipe-to-shell installer commands for the oo CLI.

Mitigation: Review the installer source or install the oo CLI through a verified package-managed method before use.

Risk: The connected AppVeyor API key may expose more AppVeyor account data than intended.

Mitigation: Use the narrowest AppVeyor API key scope available and keep routine use to the documented read actions.

## Reference(s):

- [ClawHub AppVeyor Skill](https://clawhub.ai/oomol/skills/oo-appveyor)
- [AppVeyor Homepage](https://www.appveyor.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include oo CLI connector calls that return JSON-formatted AppVeyor data.]

## Skill Version(s):

1.0.3 (source: SKILL.md frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
