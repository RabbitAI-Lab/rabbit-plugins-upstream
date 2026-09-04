## Description:

CallRail API integration with managed OAuth for tracking and analyzing phone calls, managing tracking numbers, companies, and tags.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to access CallRail account, company, call, tracker, tag, user, integration, notification, and analytics data through the Maton CLI or SDKs. It is suited for call reporting, call organization, and cautious CallRail resource management with approval before connection creation or write operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill grants API access to a connected CallRail account through Maton.

Mitigation: Confirm trust in Maton, use OAuth where possible, and authorize only the needed CallRail account and scopes before connecting.

Risk: Write, delete, or connection-creation operations can change CallRail resources or authorize new access.

Mitigation: Review the target, payload, and intended effect, then require explicit user approval before connection creation or any POST, PUT, PATCH, or DELETE request.

## Reference(s):

- [ClawHub CallRail Skill](https://clawhub.ai/byungkyu/skills/callrail)
- [Maton Homepage](https://maton.ai)
- [CallRail API Documentation](https://apidocs.callrail.com/)
- [CallRail Help Center - API](https://support.callrail.com/hc/en-us/sections/4426797289229-API)
- [CallRail API Rate Limits](https://apidocs.callrail.com/#rate-limiting)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and API path guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a connected CallRail account.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
