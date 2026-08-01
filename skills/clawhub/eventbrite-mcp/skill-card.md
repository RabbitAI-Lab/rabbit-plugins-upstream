## Description: <br>
Query eventbrite.com from a shell - your tickets/orders, your organizations' events and attendees via the documented token API (curl), and public event discovery/search via the fpx browser bridge. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to retrieve Eventbrite account, organization, attendee, order, ticket, event-detail, and public discovery data from shell workflows without running an MCP server. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: OAuth tokens, browser cookies, attendee names, emails, order data, ticket data, and command output may expose sensitive Eventbrite account information. <br>
Mitigation: Use the skill only in trusted agent sessions, avoid logging or committing tokens and captured cookies, and treat returned Eventbrite data as sensitive. <br>
Risk: The fpx/Transporter browser pairing persists after approval and can use an authenticated Eventbrite browser session. <br>
Mitigation: Review the pairing before use, limit Chrome site access to eventbrite.com, and revoke or remove the pairing when it is no longer needed. <br>
Risk: The skill is scoped to read-only recipes even though Eventbrite APIs may support organizer write operations. <br>
Mitigation: Do not compose create, update, delete, or modification calls from this skill; restrict usage to the documented read-only examples. <br>


## Reference(s): <br>
- [Eventbrite access recipes](artifact/SKILL.md) <br>
- [Eventbrite documented API recipes](artifact/references/token-api.md) <br>
- [Eventbrite discovery API recipes](artifact/references/discovery-api.md) <br>
- [Eventbrite API keys](https://www.eventbrite.com/platform/api-keys) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, curl examples, fpx examples, and jq recipes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces read-only Eventbrite API and browser-bridge request guidance; command output may include sensitive account, attendee, order, ticket, token, cookie, or browser-session data.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
