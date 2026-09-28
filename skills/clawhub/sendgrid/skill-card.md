## Description:

SendGrid API integration with managed OAuth for sending email and managing contacts, templates, suppressions, statistics, sender identities, unsubscribe groups, and API keys.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to perform SendGrid account tasks through Maton, including sending transactional or marketing email, managing lists and suppressions, handling bounces and unsubscribes, and analyzing email performance. It is suited for user-approved SendGrid work where the agent should default to read or list operations and confirm writes, sends, connection changes, API key actions, and automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Email sends and SendGrid data changes can affect real recipients, sender reputation, and account records.

Mitigation: Default to read and list operations; require explicit user approval for every write, send, connection change, and destructive action after confirming the target resource, payload, sender, audience, and intended effect.

Risk: SendGrid API key management can create long-lived credentials that persist beyond the session.

Mitigation: Only perform API key actions when explicitly requested, use the narrowest scopes required, and do not expose created key values in logs, files, or agent output.

Risk: Persistent trigger destinations can continue forwarding event data until deleted.

Mitigation: Create or update destinations only after separate user approval of the exact destination URL, owner, transmitted fields, persistence, and any credentials; minimize forwarded fields and remove destinations that are no longer needed.

Risk: Raw API responses and trigger payloads can contain personal or confidential data.

Mitigation: Return only the fields needed for the user task and avoid dumping full responses into logs, files, shared surfaces, or third-party destinations.

## Reference(s):

- [ClawHub SendGrid Skill](https://clawhub.ai/byungkyu/skills/sendgrid)
- [Maton](https://maton.ai)
- [Related API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)
- [SendGrid API Documentation](https://www.twilio.com/docs/sendgrid/api-reference)
- [SendGrid Marketing Contacts API](https://www.twilio.com/docs/sendgrid/api-reference/contacts)
- [SendGrid Suppressions Overview](https://www.twilio.com/docs/sendgrid/api-reference/suppressions-suppressions)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands, HTTP examples, JSON payloads, and guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and user-authorized SendGrid connection credentials.]

## Skill Version(s):

1.2.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
