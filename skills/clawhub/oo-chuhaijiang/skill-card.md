## Description:

Chuhaijiang helps agents search and read TikTok Shop product, shop, creator, video, live stream, review, ranking, pricing, sales, category, and market data through an OOMOL-connected Chuhaijiang account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to run read-oriented Chuhaijiang product research and market analysis workflows. It is suited for searching products, reading product and shop details, comparing similar or top-selling products, and listing related creators, videos, live streams, and reviews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an account-connected Chuhaijiang connector, so results and access depend on the configured OOMOL account, Chuhaijiang connection, scopes, and account credits.

Mitigation: Confirm the intended account connection when access errors occur, retry setup only after authentication or connection failures, and resolve billing stops before rerunning requests.

Risk: Future connector actions could be marked write or destructive even though the current release is read-oriented.

Mitigation: Let the agent run read/search actions directly, but review the live connector schema and approve the exact payload before any write or destructive action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-chuhaijiang)
- [Chuhaijiang Homepage](https://www.chuhaijiang.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON when the oo CLI is run with --json.]

## Skill Version(s):

1.0.1 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
