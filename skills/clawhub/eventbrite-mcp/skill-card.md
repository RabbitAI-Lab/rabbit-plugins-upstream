## Description:

Query Eventbrite from a shell for tickets, orders, organization events, attendees, event details, and public discovery using curl with a token or the fpx browser bridge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to compose read-only Eventbrite shell commands for account data, organization event data, attendee/order lookup, public event discovery, and event detail retrieval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent browser-session access can expose private Eventbrite account data with limited scoping.

Mitigation: Use a dedicated browser profile and Eventbrite account session, and unpair or revoke the bridge when finished.

Risk: Tokens, captured cookies, attendee emails, or order details may leak through logs or committed files.

Mitigation: Avoid printing sensitive Eventbrite data into logs and never commit tokens or captured cookies.

Risk: The global fpx CLI install is unpinned and may change behavior over time.

Mitigation: Pin or verify the @fetchproxy/cli package before installing or using it.

Risk: The underlying documented API supports organizer write operations that are outside this skill's scope.

Mitigation: Use only the read-only recipes described by the skill and do not improvise create or update calls from this guidance.

## Reference(s):

- [eventbrite-mcp on ClawHub](https://clawhub.ai/chrischall/skills/eventbrite-mcp)
- [Eventbrite documented API recipes](references/token-api.md)
- [Eventbrite discovery API recipes](references/discovery-api.md)
- [Eventbrite API keys](https://www.eventbrite.com/platform/api-keys)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON/jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only recipes; outputs may include private Eventbrite account, attendee, order, and event data when credentials or a signed-in browser session are used.]

## Skill Version(s):

0.3.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
