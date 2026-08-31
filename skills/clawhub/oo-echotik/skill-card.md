## Description:

EchoTik lets an agent search and read EchoTik market, product, creator, video, shop, and live-commerce data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query EchoTik and TikTok Shop commerce intelligence through their OOMOL-connected account, including category trends, rankings, product details, creator details, video details, reviews, shops, and live sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connector calls may use the user's OOMOL-connected EchoTik account permissions or credits.

Mitigation: Install only for intended EchoTik data lookups, review the OOMOL account connection first, and monitor billing or credit status before repeated use.

Risk: The oo CLI installer and account connection are prerequisites for running the skill.

Mitigation: Review the oo CLI installer and EchoTik account connection before setup, and avoid exposing raw credentials to the agent.

Risk: Connector action inputs can change with the live EchoTik contract.

Mitigation: Fetch the action schema with `oo connector schema` before building each payload, then run only schema-matching JSON.

## Reference(s):

- [EchoTik API service](https://echotik.live/zh/api-service)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [EchoTik on ClawHub](https://clawhub.ai/oomol/skills/oo-echotik)

## Skill Output:

**Output Type(s):** [shell commands, guidance, configuration, text]

**Output Format:** [Markdown with inline bash commands and JSON payloads or results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses depend on the live EchoTik connector schema and the user's connected OOMOL account.]

## Skill Version(s):

1.0.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
