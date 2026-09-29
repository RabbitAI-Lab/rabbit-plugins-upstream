## Description:

Helps agents manage Zoho Projects projects, tasks, milestones, time tracking, and collaboration through a user-authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Project teams and developers use this skill to review and manage Zoho Projects work, including tasks, milestones, and time records. They can also configure approved workflows through Maton.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting an account or changing project data may grant access or cause unintended writes.

Mitigation: Obtain explicit approval for connections and each write; confirm the account, target, and intended effect.

Risk: Hosted functions, triggers, and destinations may run repeatedly or forward data to an external host.

Mitigation: Approve the data flow, schedule, destination host, and deletion or rollback plan before enabling automation.

## Reference(s):

- [Zoho Projects API V3 documentation](https://projects.zoho.com/api-docs)
- [Zoho Projects developer portal](https://www.zoho.com/projects/help/rest-api/zohoprojectsapi.html)
- [Maton documentation](https://docs.maton.ai)
- [Maton homepage](https://maton.ai)
- [ClawHub Zoho Projects release](https://clawhub.ai/byungkyu/skills/zoho-projects)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with command and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses depend on the authorized Zoho Projects account and requested operation.]

## Skill Version(s):

1.2.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
