## Description:

Helps agents manage Mailchimp audiences, subscribers, campaigns, templates, automations, and reports through a connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams and developers use this skill to inspect and manage Mailchimp audiences, subscribers, campaigns, and reports, with approval before account changes or campaign sends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connected account access can expose or change marketing data.

Mitigation: Review requested OAuth scopes, use read-only access when possible, and confirm each write with the user.

Risk: Campaign sends can reach real recipients.

Mitigation: Confirm the audience, content, and intended send before executing.

Risk: Persistent triggers or third-party destinations can repeatedly forward data.

Mitigation: Avoid enabling them unless needed and explicitly approved by the user.

## Reference(s):

- [Mailchimp Marketing API documentation](https://mailchimp.com/developer/marketing/api/)
- [Maton homepage](https://maton.ai)
- [Maton API documentation](https://docs.maton.ai/api-reference/overview)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code]

**Output Format:** [Markdown with command and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Account connection and network access required; changes and sends require user approval.]

## Skill Version(s):

1.2.4 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
