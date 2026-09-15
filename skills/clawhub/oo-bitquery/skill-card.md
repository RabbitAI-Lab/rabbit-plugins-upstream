## Description:

Use this skill for Bitquery requests involving search and data reads, routing actions through the Bitquery connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect the live Bitquery connector schema and run Bitquery V2 GraphQL HTTP queries through an OOMOL-connected account without handling raw API tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path uses a remote shell installer for the oo CLI.

Mitigation: Do not let an agent run the installer automatically; install the CLI manually from a trusted source with version pinning or verification where possible.

Risk: Connector commands run through the user's OOMOL-connected Bitquery account.

Mitigation: Inspect the live action schema before building payloads and only run the intended Bitquery query against the connected account.

## Reference(s):

- [Bitquery homepage](https://bitquery.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-bitquery)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON response envelopes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and meta.executionId fields when actions run with --json.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
