## Description:

Motion API integration with managed OAuth for managing tasks, projects, workspaces, comments, recurring tasks, schedules, and related Motion resources through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operators use this skill to query and manage scheduled work in Motion through a managed OAuth gateway. It supports read/list workflows by default and guided write operations after user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and modify data in the connected Motion account after authorization.

Mitigation: Use OAuth where possible and approve connection creation only after checking the intended account and connection.

Risk: Write or delete requests can change or remove Motion tasks, projects, comments, custom fields, and related resources.

Mitigation: Before POST, PUT, PATCH, or DELETE requests, confirm the exact account, connection ID, resource ID, payload, and intended effect.

Risk: The raw API-key fallback exposes a long-lived Maton credential to the process environment.

Mitigation: Use the fallback only when the Maton CLI is unavailable; never print, log, persist, or pass the key on a command line, and send it only to api.maton.ai.

Risk: Multiple Maton accounts or Motion connections can cause requests to target the wrong workspace or account.

Mitigation: Specify the Maton profile and Motion connection when more than one exists, and verify context with read/list calls before proposing changes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/motion)
- [Maton Homepage](https://maton.ai)
- [Motion API Documentation](https://docs.usemotion.com/)
- [Motion API Reference](https://docs.usemotion.com/api-reference)
- [Motion Cookbooks](https://docs.usemotion.com/cookbooks/getting-started)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Related API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON request/response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read/list calls are the default; write and delete operations require explicit user confirmation.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
