## Description:

Helps agents access LinkedIn through Maton-managed OAuth to read profiles and organization information, publish posts, and manage supported advertising features.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams use this skill to read LinkedIn account and organization information, share content, and manage supported advertising workflows through an authorized connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorizing more LinkedIn access than the task needs exposes account data and actions.

Mitigation: Obtain approval before connecting an account and select only the required OAuth scopes.

Risk: Posts, ads, deletions, functions, triggers, or destinations could act on the wrong account or send information unexpectedly.

Mitigation: Confirm the account, target, content, and effect with the user before each sensitive action; approve automation and destinations separately.

Risk: Raw API keys and LinkedIn responses may expose credentials or personal information.

Mitigation: Prefer CLI-managed credentials; use raw keys only if the CLI is unavailable and return only task-relevant response fields.

## Reference(s):

- [ClawHub LinkedIn skill](https://clawhub.ai/byungkyu/skills/linkedin-api)
- [Maton homepage](https://maton.ai)
- [Maton API documentation](https://docs.maton.ai/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [LinkedIn API overview](https://learn.microsoft.com/en-us/linkedin/)
- [LinkedIn Marketing API](https://learn.microsoft.com/en-us/linkedin/marketing/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and task-relevant API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized LinkedIn connection.]

## Skill Version(s):

1.2.6 (source: ClawHub release metadata; skill frontmatter says 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
