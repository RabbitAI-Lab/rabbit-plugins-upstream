## Description:

Salesloft lets agents search and read Salesloft accounts, cadences, people, and current-user data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, developers, and sales operations teams use this skill to search and read Salesloft accounts, cadences, people, and authenticated user information through an OOMOL-connected Salesloft account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup directs users to execute a remote installer directly in the shell.

Mitigation: Review the installer path before installing, and prefer a pinned, signed, or manually inspected installer.

Risk: Future versions could add Salesloft write actions beyond the currently listed read actions.

Mitigation: Use this release only for the listed read actions unless a later version clearly documents write capabilities and confirmation rules.

## Reference(s):

- [ClawHub Salesloft Skill](https://clawhub.ai/oomol/skills/oo-salesloft)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Salesloft Homepage](https://www.salesloft.com/)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [OOMOL Salesloft connection](https://console.oomol.com/app-connections?provider=salesloft)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Salesloft connector schemas before running read actions.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
