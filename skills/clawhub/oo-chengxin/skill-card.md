## Description:

同程程心 (ly.com) helps agents search and read Tongcheng Chengxin travel data through the OOMOL `chengxin` connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and travel-support agents use this skill to search Tongcheng Chengxin travel data for attractions, hotels, flights, trains, buses, multimodal transport, and vacation products through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Travel search requests may send itinerary, destination, or preference details through the OOMOL connector.

Mitigation: Use the skill only with an OOMOL-connected 同程程心 account you trust, and avoid sending unnecessary sensitive travel details.

Risk: Future connector actions tagged as write or destructive could change or remove account data if approved without review.

Mitigation: Require explicit user confirmation of the exact payload, target, and effect before running any write or destructive action.

Risk: Connector schemas can change over time, which can make stale payload assumptions incorrect.

Mitigation: Inspect the live action schema with `oo connector schema` before constructing each payload.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-chengxin)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [同程程心 homepage](https://www.ly.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs agents to inspect live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: server release and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
