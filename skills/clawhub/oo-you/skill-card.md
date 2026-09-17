## Description:

Enables agents to use You.com through the OOMOL oo CLI for search, webpage content fetching, cited research, finance research, and account balance lookup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to perform You.com web and news search, fetch webpage content, and request cited research or finance answers through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that can execute changing code on a user's machine.

Mitigation: Review or verify the installer before use, and prefer a pinned package or verified release artifact.

Risk: Queries and URLs submitted through the connector may be sent to You.com and OOMOL-connected services.

Mitigation: Avoid sending sensitive data unless that disclosure is acceptable for the user's account and environment.

## Reference(s):

- [You.com homepage](https://you.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL app connections](https://console.oomol.com/app-connections?provider=you)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may return JSON responses from the oo CLI with data and execution metadata.]

## Skill Version(s):

1.0.4 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
