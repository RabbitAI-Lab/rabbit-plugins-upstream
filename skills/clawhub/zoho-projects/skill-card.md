## Description:

Zoho Projects API V3 integration with managed OAuth for managing projects, tasks, milestones, tasklists, and team collaboration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Teams and agents use this skill to read and manage Zoho Projects work items through Maton-managed OAuth, including projects, tasks, comments, tasklists, milestones, users, and related collaboration data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify or delete Zoho Projects data after the user authorizes access through Maton.

Mitigation: Use OAuth where possible, approve only the needed Zoho account and scopes, and require explicit review before write or delete operations.

Risk: Requests may target the wrong account when multiple Maton or Zoho Projects connections exist.

Mitigation: Specify the intended Maton profile and Zoho Projects connection before taking action, especially for writes.

Risk: Long-lived Maton API keys can be exposed through logs, shell history, or child processes when used outside the CLI flow.

Mitigation: Prefer Maton OAuth through the CLI; if raw HTTP is required, provide the key only through protected input and never print, persist, or pass it on the command line.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/zoho-projects)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Zoho Projects API V3 Documentation](https://projects.zoho.com/api-docs)
- [Zoho Projects Developer Portal](https://www.zoho.com/projects/help/rest-api/zohoprojectsapi.html)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May result in authenticated Zoho Projects API calls through the Maton CLI or SDK when the user authorizes access.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
