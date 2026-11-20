## Description:

Gives an agent phone calling and call screening through MCP, with transcripts, calendar booking, optional CRM, and opt-in Apple Contacts lookup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[batthis](https://clawhub.ai/user/batthis)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use Amber to let an agent screen incoming calls, prepare confirmed outbound calls, check call history, and support call workflows with calendar, contact, and optional CRM tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags undisclosed capabilities, optional background persistence, and incomplete inspection.

Mitigation: Review required permissions and provider accounts, disable the optional watcher and extended contact export unless needed, and wait for dependencies and referenced scripts to receive a complete review.

Risk: Calls, transcripts, contact details, and calendar data can include sensitive information about the operator and other people.

Mitigation: Review retention and access permissions, disclose caller notice and consent practices, collect only needed details, and require explicit approval for outbound calls and calendar writes.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/batthis/skills/amber-phone-agent)
- [OpenAI Privacy Policy](https://openai.com/policies/privacy-policy)

## Skill Output:

**Output Type(s):** [Guidance, MCP tool calls, Call summaries, Calendar entries]

**Output Format:** [Natural language guidance and structured MCP tool interactions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outbound calls and calendar writes require explicit confirmation; call records and personal data should be treated as private.]

## Skill Version(s):

5.5.60 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
