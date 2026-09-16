## Description:

EchoTik helps agents handle EchoTik requests involving search and read access to market, product, creator, live, video, shop, and review data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query EchoTik TikTok Shop market intelligence through an OOMOL-connected account. It supports read-oriented category, product, creator, live, video, shop, and review lookups while relying on the live connector schema before each action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include one-line remote installer commands that execute downloaded scripts directly in a shell.

Mitigation: Use official, versioned oo CLI installation instructions and verify checksums or signatures before installing.

Risk: The skill uses an OOMOL-connected account to access EchoTik data.

Mitigation: Keep authentication and connector setup under direct user control, and do not run login or connection steps unless an action fails with an auth or connection error.

Risk: Connector payloads can be malformed or stale if action inputs are assumed.

Mitigation: Inspect the live connector schema with oo connector schema before building each request payload.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-echotik)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [EchoTik API service](https://echotik.live/zh/api-service)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI to inspect action schemas and run EchoTik connector actions; responses include data and an execution id.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
