## Description:

Provides read-only shell recipes for retrieving Eventbrite account and organizer data and discovering public events.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Eventbrite users can retrieve their tickets, orders, organization events, and attendee information, or find public events using read-only shell commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account orders, attendee details, tokens, or cookies could be exposed when running examples.

Mitigation: Treat account data and credentials as private; do not save them in logs, scripts, screenshots, or shared terminals.

Risk: Pairing the browser bridge gives it access to eventbrite.com in the browser.

Mitigation: Install and pair the bridge only if comfortable granting it site access to eventbrite.com.

## Reference(s):

- [Eventbrite token API recipes](references/token-api.md)
- [Eventbrite discovery recipes](references/discovery-api.md)
- [Eventbrite API keys](https://www.eventbrite.com/platform/api-keys)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/eventbrite-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and API query examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only recipes; retrieved results may contain private account and attendee data.]

## Skill Version(s):

1.1.9 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
