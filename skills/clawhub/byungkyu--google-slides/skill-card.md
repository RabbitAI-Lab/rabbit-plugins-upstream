## Description:

Helps agents create, edit, and format Google Slides presentations through a user-authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams use this skill to read and update presentations, add slides and content, and set up approved automations through their Google Slides connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Google Slides connection grants access according to the OAuth scopes the user approves.

Mitigation: Review requested scopes, select only what is needed, and prefer read-only access when possible.

Risk: Writes, new connections, and hosted automation can change presentations or account behavior.

Mitigation: Default to reading and listing; get explicit user confirmation before any write, connection, function, or automation.

Risk: Persistent triggers and destinations can keep forwarding event data until removed.

Mitigation: Confirm the destination, data, and duration before enabling forwarding; review and delete destinations when no longer needed.

## Reference(s):

- [Google Slides skill on ClawHub](https://clawhub.ai/byungkyu/skills/google-slides)
- [Maton](https://maton.ai)
- [Google Slides API reference](https://developers.google.com/slides/api/reference/rest)
- [Related API gateway skill](https://clawhub.ai/byungkyu/api-gateway)
- [Time trigger reference](references/time/triggers.md)
- [Google Mail trigger reference](references/google-mail/triggers.md)
- [Calendly trigger reference](references/calendly/triggers.md)
- [GitHub trigger reference](references/github/triggers.md)
- [HubSpot trigger reference](references/hubspot/triggers.md)
- [Linear trigger reference](references/linear/triggers.md)
- [Notion trigger reference](references/notion/triggers.md)
- [Slack trigger reference](references/slack/triggers.md)
- [Stripe trigger reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code]

**Output Format:** [Markdown with commands and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Google Slides actions require a user-authorized connection; confirm writes and automations before execution.]

## Skill Version(s):

1.2.4 (source: ClawHub release metadata; skill frontmatter lists 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
