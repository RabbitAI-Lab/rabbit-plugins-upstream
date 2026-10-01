## Description:

Helps agents read and manage Zoho Recruit candidates, job openings, interviews, and applications through a managed connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiters and hiring teams use this skill to look up and manage Zoho Recruit records, and to set up approved recruitment workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Candidate records may contain sensitive personal information.

Mitigation: Request only necessary records, limit details in responses, and get explicit approval before sharing data with another service.

Risk: Writes and bulk deletions can change or permanently remove recruitment records.

Mitigation: Default to reads; confirm the target and intended changes before writes, and approve each record before deletion.

Risk: Connections and automated triggers can grant ongoing access or forward event data.

Mitigation: Use the narrowest available permissions and require explicit approval for new connections, automation, and third-party destinations.

## Reference(s):

- [Zoho Recruit skill on ClawHub](https://clawhub.ai/byungkyu/skills/zoho-recruit)
- [Maton homepage](https://maton.ai)
- [Zoho Recruit API v2 documentation](https://www.zoho.com/recruit/developer-guide/apiv2/)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Maton documentation](https://docs.maton.ai)
- [API gateway skill for other applications](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with commands and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include selected Zoho Recruit record details and workflow setup guidance.]

## Skill Version(s):

1.2.4 (source: ClawHub release metadata; skill frontmatter says 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
