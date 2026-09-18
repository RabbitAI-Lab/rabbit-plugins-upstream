## Description:

Bitquery connector skill for running Bitquery search and data queries through an OOMOL-connected account instead of calling the Bitquery API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect the live OOMOL Bitquery connector schema and run Bitquery V2 GraphQL queries through the oo CLI when a task requires Bitquery data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands executed directly in a shell.

Mitigation: Install the oo CLI only through a trusted, verified, version-pinned, signed, or checksum-verified path.

Risk: Bitquery query payloads are routed through OOMOL-connected infrastructure.

Mitigation: Use the skill only when routing those payloads through OOMOL is acceptable for the account, data, and use case.

Risk: Connector action inputs may change over time.

Mitigation: Inspect the live action schema with oo connector schema before constructing or running payloads.

## Reference(s):

- [ClawHub Bitquery skill page](https://clawhub.ai/oomol/skills/oo-bitquery)
- [Bitquery homepage](https://bitquery.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON response envelopes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns Bitquery GraphQL response data with execution metadata when connector actions run successfully.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
