## Description:

Analyzes automotive service, tire, and lubricant brand store networks, regional coverage, and location profiles from Baidu Maps address text using published 店店通 store snapshots.

This skill is ready for commercial/non-commercial use.

## Publisher:

[horacetu](https://clawhub.ai/user/horacetu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business analysts use this skill to evaluate automotive aftermarket brand footprints, compare regional coverage, and inspect limited nearby-store or single-store details when the user provides an address, coordinate, or public store ID.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends brand, address, coordinate, or store-ID queries to a third-party publisher service.

Mitigation: Use it only when that data sharing is acceptable, and avoid submitting sensitive or confidential locations.

Risk: The skill requires a 店店通 API key.

Mitigation: Store the key only in a controlled environment variable and do not paste it into chats, logs, skill files, or version control.

Risk: Results depend on the publisher's available data snapshots and the skill is not an official Baidu Maps product.

Mitigation: Treat unavailable coverage as unavailable, verify important business decisions against authoritative sources, and do not infer a Baidu Maps partnership or data source relationship.

## Reference(s):

- [店店通 ClawHub API homepage](https://gotoshop-ai.com/ddtclaw/)
- [ClawHub skill page](https://clawhub.ai/horacetu/skills/ddt-baidu-map-auto-network)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown analysis with concise conclusions, key metrics, coverage notes, and limited store details when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses scoped API queries and should avoid exposing API keys, storage IDs, suppliers, internal fields, or unsupported metrics.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
