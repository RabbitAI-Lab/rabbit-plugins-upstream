## Description:

Connects an agent to Jobber through Maton to manage field-service clients, jobs, quotes, invoices, properties, scheduling data, and team members.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Field-service teams and their agents use this skill to retrieve Jobber records and, with approval, create or update clients, jobs, quotes, and invoices. Optional functions and triggers can automate approved actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting Jobber or making changes may grant access to business records or alter them.

Mitigation: Approve each connection and write separately, select only needed access, and remove unused connections.

Risk: Hosted functions, triggers, and event watches can keep acting without a person reviewing each event.

Mitigation: Approve each function, trigger, and destination separately; only run watch --exec with a user-provided, reviewed script.

Risk: External destinations can receive business or event data.

Mitigation: Keep destinations on Maton-controlled hosts unless you explicitly trust the external host.

## Reference(s):

- [Jobber skill release](https://clawhub.ai/byungkyu/skills/jobber)
- [Maton](https://maton.ai)
- [Jobber Developer Documentation](https://developer.getjobber.com/docs/)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, API calls, Code, Shell commands, Guidance]

**Output Format:** [Markdown with commands, API examples, and structured response summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Maton account and network access; Jobber access depends on the authorized connection.]

## Skill Version(s):

1.2.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
