## Description:

Give your agent a phone number. Amber answers calls, places confirmed outbound calls, completes phone tasks, logs transcripts, and exposes MCP tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[batthis](https://clawhub.ai/user/batthis)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Operators use Amber to screen incoming calls and handle confirmed outbound calls, messages, bookings, and follow-up through an AI agent. They can also review call history and use optional contact, calendar, and CRM workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles caller transcripts and can access calendar, CRM, and local contact data; the security review also flags caller data and shared call context.

Mitigation: Enable only the data integrations needed, review caller isolation and privacy behavior, and set clear caller notice, consent, access, retention, and deletion practices.

Risk: The security review reports capabilities beyond the phone-agent description and incomplete analysis of some components.

Mitigation: Review the requested permissions and optional background watcher before installation, and use dedicated, least-privilege provider credentials.

## Reference(s):

- [Amber ClawHub release](https://clawhub.ai/batthis/skills/amber-phone-agent)

## Skill Output:

**Output Type(s):** [Text, Guidance, MCP tool calls]

**Output Format:** [Conversational text and structured MCP tool requests or results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include call summaries or transcript text when available.]

## Skill Version(s):

5.5.52 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
