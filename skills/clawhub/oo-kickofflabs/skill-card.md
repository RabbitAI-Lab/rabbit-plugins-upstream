## Description:

Reads KickoffLabs campaigns, campaign statistics, and scoring action definitions through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

KickoffLabs users and their agents use this skill to list campaigns, review lead statistics, and inspect configured scoring actions in a connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional setup instructions can execute an unverified remote installer.

Mitigation: Review the installer before use; prefer a verified package or documented signed installation method.

Risk: Broad routing language could lead an agent to attempt actions beyond the three documented reads.

Mitigation: Limit use to the listed read-only actions unless additional connector actions have been reviewed separately.

## Reference(s):

- [KickoffLabs](https://kickofflabs.com/)
- [oo CLI installation guide](https://cli.oomol.com/install-guide.md)
- [KickoffLabs skill on ClawHub](https://clawhub.ai/oomol/skills/oo-kickofflabs)

## Skill Output:

**Output Type(s):** [Text, Shell commands]

**Output Format:** [Markdown summaries and JSON campaign data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only campaign discovery, statistics, and scoring action listings.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
