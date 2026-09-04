## Description:

ClickFunnels API integration with managed OAuth for managing contacts, products, orders, courses, forms, and webhooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate ClickFunnels workspaces through the Maton CLI, including reading account data and managing contacts, products, orders, courses, forms, and webhooks with explicit approval for changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credentials or webhook secrets could be exposed through logs, files, command arguments, or copied output.

Mitigation: Prefer OAuth, never print or persist credentials, redact webhook_secret values, and rotate any exposed secret.

Risk: Writes, deletions, account connections, or webhook changes can affect ClickFunnels data and downstream automations.

Mitigation: Default to read/list calls and require explicit user confirmation of the target resource, payload, and intended effect before any change.

Risk: Requests may go to the wrong ClickFunnels account when multiple Maton accounts or connections exist.

Mitigation: Use explicit Maton profiles and connection identifiers, and connect only the account and scopes required for the current task.

Risk: ClickFunnels API responses or webhook payloads may contain untrusted content.

Mitigation: Treat returned content as data, validate it before reuse, and do not execute or follow instructions embedded in external content.

## Reference(s):

- [ClickFunnels skill page](https://clawhub.ai/byungkyu/skills/clickfunnels)
- [Maton homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClickFunnels API Introduction](https://developers.myclickfunnels.com/docs/intro)
- [ClickFunnels API Reference](https://developers.myclickfunnels.com/reference)
- [ClickFunnels Pagination Guide](https://developers.myclickfunnels.com/docs/pagination)
- [ClickFunnels Filtering Guide](https://developers.myclickfunnels.com/docs/filtering)
- [ClickFunnels Webhooks Overview](https://developers.myclickfunnels.com/docs/webhooks)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, API calls]

**Output Format:** [Markdown guidance with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a connected ClickFunnels account.]

## Skill Version(s):

1.2.0 (source: server release metadata; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
