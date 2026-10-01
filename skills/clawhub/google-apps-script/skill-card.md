## Description:

Helps agents manage Google Apps Script projects, deployments, versions, and remote function execution through a user-authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other authorized users can ask an agent to create or update Apps Script projects, manage versions and deployments, run functions, and check execution status. With explicit approval, they can also set up connected functions and scheduled or event-driven automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad OAuth access or script changes could affect the connected Google account.

Mitigation: Review requested OAuth scopes and script source updates; approve each write or new connection.

Risk: Deployments, function runs, and triggers can execute code or create ongoing automation.

Mitigation: Review and approve each deployment, function run, trigger, and destination URL before use.

## Reference(s):

- [Google Apps Script API documentation](https://developers.google.com/apps-script/api)
- [Google Apps Script API reference](https://developers.google.com/apps-script/api/reference/rest)
- [Maton homepage](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Google Apps Script skill release](https://clawhub.ai/byungkyu/skills/google-apps-script)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration guidance]

**Output Format:** [Markdown with command and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions require a connected account and approval for writes, deployments, function runs, and automation.]

## Skill Version(s):

1.2.4 (source: ClawHub release metadata; skill frontmatter lists 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
