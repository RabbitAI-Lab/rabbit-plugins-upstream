## Description:

Helps field service teams manage Jobber clients, jobs, quotes, invoices, properties, schedules, and team members through a connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Field service staff and their agents use this skill to retrieve scheduling and customer information and, with approval, create or update Jobber business records. Optional hosted functions and triggers support user-approved automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Jobber access may expose sensitive customer and business data.

Mitigation: Use OAuth and a least-privileged Jobber account; keep credentials out of outputs and files.

Risk: Writes or deletions can change or remove business records.

Mitigation: Confirm each write or deletion with the user before execution.

Risk: Functions, triggers, and external destinations can keep running or send data after the initial task.

Mitigation: Create automation only with explicit approval after reviewing its code, destination host, payload fields, and cleanup plan.

## Reference(s):

- [Jobber skill on ClawHub](https://clawhub.ai/byungkyu/skills/jobber)
- [Maton homepage](https://maton.ai)
- [Jobber developer documentation](https://developer.getjobber.com/docs/)
- [Jobber getting started guide](https://developer.getjobber.com/docs/getting_started/)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Guidance]

**Output Format:** [Markdown with command and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Jobber record details returned through the user's authorized connection.]

## Skill Version(s):

1.2.5 (source: ClawHub release evidence; skill frontmatter lists 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
