## Description:

Enables agents to search and retrieve Twelve Data market data through the OOMOL oo CLI connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect Twelve Data connector schemas and run read-oriented market data actions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes unverified remote installer commands for the oo CLI.

Mitigation: Do not run curl | bash or irm | iex installer commands unless the oo CLI source is trusted and the installer is verified through an official, versioned, integrity-checked channel.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-twelve-data)
- [Twelve Data Homepage](https://twelvedata.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action results are JSON responses returned by oo connector run.]

## Skill Version(s):

1.0.3 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
