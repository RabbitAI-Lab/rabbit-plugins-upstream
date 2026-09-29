## Description:

Guides agents in accessing Jobber through Maton to manage field-service clients, jobs, quotes, invoices, and approved automations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Field-service teams and their agents use this skill to look up and manage Jobber business records and, with approval, connect accounts or configure related automations through Maton.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Writes to Jobber may change business records.

Mitigation: Start with read-only requests and confirm each specific write with the user.

Risk: Functions and triggers can create persistent automations with account access.

Mitigation: Approve only the functions, triggers, and access needed for the intended task.

Risk: Destination URLs may forward business data outside Maton and Jobber.

Mitigation: Review the destination and data sent before approving third-party forwarding; prefer OAuth over raw API keys.

## Reference(s):

- [Jobber skill release](https://clawhub.ai/byungkyu/skills/jobber)
- [Jobber developer documentation](https://developer.getjobber.com/docs/)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Maton homepage](https://maton.ai)
- [Time trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Guidance]

**Output Format:** [Markdown with command and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide approved Jobber API actions and persistent Maton automations.]

## Skill Version(s):

1.2.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
