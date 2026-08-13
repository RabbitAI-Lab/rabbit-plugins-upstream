## Description:

SellerSprite (sellersprite.com). Use this skill for SellerSprite search and data-reading requests through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query SellerSprite for Amazon product, ASIN, competitor, keyword, and API usage data through the oo CLI after their OOMOL account is connected.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SellerSprite product, ASIN, keyword, and usage queries are sent through the OOMOL/SellerSprite integration.

Mitigation: Install only when this data flow is intended, and review the oo CLI installer plus OOMOL account connection flow before first use.

Risk: Payloads may become invalid if SellerSprite connector action schemas change.

Mitigation: Inspect the live action schema with `oo connector schema` before constructing each payload.

Risk: Future write or destructive connector actions could change or remove SellerSprite data.

Mitigation: Confirm the exact payload and effect with the user before write actions, and require explicit approval before destructive actions.

## Reference(s):

- [SellerSprite homepage](https://www.sellersprite.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [SellerSprite skill on ClawHub](https://clawhub.ai/oomol/skills/oo-sellersprite)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs agents to inspect the live connector schema before building each action payload.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
