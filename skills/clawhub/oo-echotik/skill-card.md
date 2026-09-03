## Description:

EchoTik helps agents search and read EchoTik market, product, creator, live, video, shop, category, ranking, and review data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to query EchoTik and TikTok Shop market intelligence, including category trends, product details, creator profiles, live rooms, videos, shops, rankings, and product reviews. It is intended for agents that already have the oo CLI installed and an OOMOL-connected EchoTik account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on an external CLI and an OOMOL-connected EchoTik account, so missing installation, authentication, connection scope, or billing state can block use.

Mitigation: Install and sign in to the oo CLI only when required by an actual command failure, reconnect EchoTik when scope or credential errors occur, and resolve billing issues before retrying.

Risk: Future EchoTik actions may write, remove, or overwrite data even though the current listed actions are read-oriented.

Mitigation: Inspect the live action schema before execution and get explicit user confirmation for any action tagged write or destructive.

Risk: Market and commerce results are offline or T+1 snapshots and may not reflect real-time EchoTik or TikTok Shop state.

Mitigation: Present returned data as snapshot intelligence and include relevant dates, filters, and regions when summarizing results.

## Reference(s):

- [EchoTik API Service](https://echotik.live/zh/api-service)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-echotik)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are expected as JSON objects when commands are run with --json.]

## Skill Version(s):

1.0.1 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
