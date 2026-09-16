## Description:

Keepa lets agents search and read Keepa data for Amazon products, deals, categories, sellers, token status, and product history through OOMOL's oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to query Keepa through an OOMOL-connected account instead of handling Keepa API credentials directly. It supports product discovery, deal filtering, best-seller lists, product history, snapshots, seller profiles, category search, and token-status checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes curl-to-bash and irm-to-iex installer commands for the oo CLI.

Mitigation: Do not let an agent run those installer commands automatically; install the oo CLI through a trusted, verifiable method and review publisher and installer integrity first.

Risk: Connector use depends on an OOMOL account, a Keepa connection, and possible billing or token consumption.

Mitigation: Confirm the account, connection state, and billing or token impact before broad or repeated Keepa queries.

Risk: Incorrect connector payloads can produce failed or misleading Keepa queries.

Mitigation: Fetch the live action schema with oo connector schema before constructing each action payload, and bound pagination or filters for large searches.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-keepa)
- [Keepa Homepage](https://keepa.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action results are returned as JSON objects with data and meta.executionId when commands are run.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
