## Description:

Helps agents read, create, and format Google Docs through a user-authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams use this skill to retrieve Google Docs content and, with approval, create documents or update text and formatting. Optional automations can run approved document actions on a schedule or in response to supported external events.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting an account gives Maton access to Google Docs within the authorized scope.

Mitigation: Get consent before connecting, choose the least-privilege scopes available, and remove unused connections.

Risk: Document writes can change or expose user content.

Mitigation: Start with read-only checks and confirm the target document, changes, and intended effect before each write.

Risk: Trigger destinations can continuously forward matching event data to another service.

Mitigation: Require separate explicit approval for each destination and avoid external destinations unless the user requests them.

Risk: A raw API key can leak through logs, files, or subprocesses.

Mitigation: Prefer managed OAuth and the CLI; if a key is necessary, keep it out of commands, logs, and persistent files.

## Reference(s):

- [Google Docs skill release](https://clawhub.ai/byungkyu/skills/google-docs)
- [Maton](https://maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Google Docs API overview](https://developers.google.com/docs/api/how-tos/overview)
- [Google Docs batch update reference](https://developers.google.com/docs/api/reference/rest/v1/documents/batchUpdate)
- [Scheduled trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with API examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Document content may contain personal information; return only what the user needs.]

## Skill Version(s):

1.2.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
