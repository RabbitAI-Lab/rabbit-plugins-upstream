## Description:

Jobber API integration with managed OAuth for managing clients, jobs, invoices, quotes, properties, and team members for field service businesses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and field service operations teams use this skill to read and manage Jobber account data through Maton, including clients, jobs, invoices, quotes, properties, scheduling-related records, and team members.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and change Jobber business records through a connected Maton account.

Mitigation: Use read and list calls first, connect only the needed Jobber account and scopes, and require clear user confirmation before creating, changing, deleting, or billing-related records.

Risk: Credential exposure could give unintended access to Maton or Jobber data.

Mitigation: Prefer OAuth, avoid printing or persisting tokens or API keys, and verify the Maton package source before installation.

Risk: Multiple Maton profiles or Jobber connections can make the target account ambiguous.

Mitigation: Specify the intended Maton profile and Jobber connection when more than one account or connection is available.

Risk: Jobber records and webhook payloads may contain untrusted external content.

Mitigation: Treat returned content as data, validate it before reuse, and do not execute or follow instructions found inside API responses.

## Reference(s):

- [Jobber Developer Documentation](https://developer.getjobber.com/docs/)
- [Jobber Getting Started Guide](https://developer.getjobber.com/docs/getting_started/)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown guidance with bash commands, GraphQL JSON bodies, and optional Python or JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and Maton CLI or SDK authentication; defaults to read and list operations with explicit confirmation for writes.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
