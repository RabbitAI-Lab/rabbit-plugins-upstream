## Description:

DaData.ru helps agents query DaData.ru suggestion actions for Russian addresses, banks, email addresses, names, organizations, and individual entrepreneurs through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to search DaData.ru suggestion data through an OOMOL-connected account without directly handling DaData.ru API credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes streamed remote installer commands for the oo CLI.

Mitigation: Review official installation instructions, use a trusted package source, or verify installer contents before execution; do not let an agent run the installer automatically.

Risk: The skill operates DaData.ru through an OOMOL-connected account.

Mitigation: Install and use it only when the user is comfortable using OOMOL's oo CLI and connected DaData.ru credentials.

## Reference(s):

- [DaData.ru homepage](https://dadata.ru)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-dadata-ru)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, text]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command responses are JSON when the oo CLI is run with --json.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
