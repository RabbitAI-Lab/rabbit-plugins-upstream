## Description:

Apollo provides managed OAuth access to the Apollo.io API so an agent can search and enrich people and companies and manage contacts, accounts, labels, sequences, and related sales data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, revenue operations, and developer users use this skill to let an agent perform approved Apollo prospecting, enrichment, contact, account, sequence, and label workflows through Maton-managed authentication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorized Apollo operations can access or change real sales data, consume enrichment credits, or send sequence-related activity.

Mitigation: Use read and list calls by default, confirm new connections and writes with the user, and review each requested Apollo authorization before proceeding.

Risk: Hosted functions, triggers, or destinations can continue running against authorized data after setup.

Mitigation: Create, invoke, or connect automation only after approval of the handler, connection, schedule or event source, destination, and network policy; remove automation when it is no longer needed.

## Reference(s):

- [Apollo Skill on ClawHub](https://clawhub.ai/byungkyu/skills/apollo-api)
- [Maton](https://maton.ai)
- [Apollo API Overview](https://docs.apollo.io/reference)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Catalog](references/time/triggers.md)
- [Slack Trigger Catalog](references/slack/triggers.md)
- [GitHub Trigger Catalog](references/github/triggers.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown with bash, HTTP, JSON, and Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes user-approval checkpoints for OAuth connections, writes, hosted functions, triggers, destinations, and raw HTTP API key fallback.]

## Skill Version(s):

1.2.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
