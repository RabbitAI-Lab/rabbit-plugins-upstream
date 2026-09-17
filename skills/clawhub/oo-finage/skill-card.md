## Description:

Finage lets agents use an OOMOL-connected Finage account to retrieve U.S. stock market data through the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to inspect Finage connector schemas and run Finage market-data actions. It supports retrieving U.S. stock aggregates, latest quotes, latest trades, previous-close data, snapshots, and symbol lists through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include mutable remote installer commands that execute directly in a shell.

Mitigation: Prefer a signed or checksummed oo CLI release, inspect installer contents before execution, and run setup with ordinary user privileges.

Risk: One read-style action is marked as a write action, which may create noisy confirmation prompts.

Mitigation: Confirm the action schema and user intent before running any action tagged as write or destructive.

## Reference(s):

- [Finage ClawHub Skill](https://clawhub.ai/oomol/skills/oo-finage)
- [Finage Homepage](https://finage.co.uk)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Finage command responses are JSON objects containing data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: evidence release and frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
