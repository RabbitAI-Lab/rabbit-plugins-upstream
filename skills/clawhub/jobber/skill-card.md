## Description:

Guides agents in managing Jobber clients, jobs, quotes, invoices, properties, and team members through an authenticated Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Field service teams and their agents use this skill to retrieve Jobber scheduling and business records or, with approval, create and update clients, jobs, quotes, and invoices. It also describes optional hosted functions and event-triggered automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated access may expose or change sensitive customer, job, and billing records.

Mitigation: Use only the necessary Jobber connection and permissions; confirm each write and its target before execution.

Risk: Hosted functions, triggers, or event watches can perform recurring actions without further prompts.

Mitigation: Review the handler and event scope and obtain separate explicit approval before enabling automation.

Risk: Trigger destinations may forward event payloads or expose credentials to external hosts.

Mitigation: Approve destinations separately, prefer Maton-controlled hosts, and never include API keys or raw sensitive payloads in external destinations.

## Reference(s):

- [Jobber skill release](https://clawhub.ai/byungkyu/skills/jobber)
- [Jobber developer documentation](https://developer.getjobber.com/docs/)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Maton homepage](https://maton.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Guidance]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance covers authenticated Jobber queries, approved record changes, and optional automation.]

## Skill Version(s):

1.2.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
