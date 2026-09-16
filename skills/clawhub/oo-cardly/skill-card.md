## Description:

Cardly (card.ly). Use this skill for Cardly requests that search, read, or inspect account data through the OOMOL-connected Cardly connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Cardly balances, credit histories, fonts, media options, and writing styles through an authenticated OOMOL connection without handling raw credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of internet installer scripts for the oo CLI.

Mitigation: Install the oo CLI through a trusted and verifiable method, preferably with version pinning or checksum/signature verification.

Risk: The skill reads data from the Cardly account connected through OOMOL.

Mitigation: Connect only the Cardly account the agent is intended to access and review requested actions before execution.

## Reference(s):

- [Cardly homepage](https://www.card.ly)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-cardly)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with oo CLI commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before actions; OOMOL injects credentials server-side.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
