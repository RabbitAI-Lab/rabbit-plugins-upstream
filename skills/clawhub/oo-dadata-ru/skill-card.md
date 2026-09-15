## Description:

DaData.ru helps agents search and read DaData.ru suggestion data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to retrieve DaData.ru suggestions for Russian addresses, banks, email addresses, full names, organizations, and individual entrepreneurs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands for the oo CLI.

Mitigation: Review the oo CLI installation path before installing and prefer an official package manager, pinned release, or installer verified with checksum or signature checks.

Risk: DaData.ru connector calls depend on OOMOL authentication, connection state, and billing state.

Mitigation: Run sign-in, connection, or billing recovery steps only after the matching command failure is observed.

## Reference(s):

- [DaData.ru homepage](https://dadata.ru)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub release page](https://clawhub.ai/oomol/skills/oo-dadata-ru)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before connector execution; available actions are read-style DaData.ru suggestion calls.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
