## Description:

Helps agents manage Dropbox files and folders, search content, and retrieve metadata through a Maton-managed connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other Dropbox users can guide an agent to list, search, and manage files and folders or retrieve metadata using their authorized Dropbox connection. User-approved hosted functions and triggers can automate selected actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A broad Dropbox authorization or unapproved file operation could expose or change data.

Mitigation: Review requested scopes, favor read-only actions, and confirm the target and effect of each write, deletion, or upload.

Risk: Hosted functions, triggers, or destinations can repeatedly act on or forward connected data.

Mitigation: Require separate approval for automation and destinations; review the function, event scope, and recipient before enabling them, and remove them when no longer needed.

Risk: API credentials or Dropbox content could be exposed through commands or logs.

Mitigation: Use managed login where possible, avoid printing credentials, and show only the response fields needed for the task.

## Reference(s):

- [Dropbox skill release](https://clawhub.ai/byungkyu/skills/dropbox-api)
- [Maton homepage](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Dropbox HTTP API overview](https://www.dropbox.com/developers/documentation/http/overview)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with command, API, and function examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include JSON responses and JavaScript function examples.]

## Skill Version(s):

1.2.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
