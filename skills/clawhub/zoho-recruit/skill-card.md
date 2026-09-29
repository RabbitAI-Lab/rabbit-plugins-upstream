## Description:

Helps agents read and manage Zoho Recruit candidates, job openings, interviews, applications, and recruiting workflows through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiting teams use this skill to find and manage candidate records, job openings, applications, and interviews in Zoho Recruit. With explicit approval, they can also set up hosted functions and triggers for ongoing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Candidate and recruiting records may contain sensitive personal information.

Mitigation: Access only the records needed for the task and avoid exposing full responses in logs or files.

Risk: Writes and bulk deletions can change or irreversibly remove recruiting records.

Mitigation: Default to reading; obtain explicit approval for every write and approve each record separately before deletion.

Risk: Hosted functions, triggers, and destinations can continue running or forwarding future events.

Mitigation: Create them only with explicit user approval after reviewing their behavior, access, and destination.

## Reference(s):

- [ClawHub Zoho Recruit release](https://clawhub.ai/byungkyu/skills/zoho-recruit)
- [Maton homepage](https://maton.ai)
- [Zoho Recruit API v2 overview](https://www.zoho.com/recruit/developer-guide/apiv2/)
- [Maton CLI manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with command and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Maton account and network access; confirm changes before execution.]

## Skill Version(s):

1.2.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
