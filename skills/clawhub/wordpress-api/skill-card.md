## Description:

WordPress.com API integration with managed OAuth for creating, reading, updating, and deleting WordPress.com posts, pages, sites, and content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage WordPress.com site content through Maton-managed OAuth, including posts, pages, site metadata, and approved automation around hosted functions and triggers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, or delete WordPress.com content through an authenticated user connection.

Mitigation: Default to read and list operations, and confirm the exact WordPress.com target, payload, and intended effect before any write or deletion.

Risk: Long-lived Maton API keys or MATON_API_KEY values can expose account access if copied into logs, files, or child processes.

Mitigation: Prefer OAuth, do not persist or expose MATON_API_KEY, and use the raw HTTP path only when the CLI cannot be installed.

Risk: Hosted functions and triggers run with the deploying Maton account's connected identity and may continue after the immediate task.

Mitigation: Use a dedicated or minimal-connection Maton account, deploy functions with DENY_ALL network policy where possible, and delete unused functions, triggers, and destinations when finished.

## Reference(s):

- [WordPress.com REST API Overview](https://developer.wordpress.com/docs/api/)
- [WordPress.com Getting Started Guide](https://developer.wordpress.com/docs/api/getting-started/)
- [WordPress.com REST API Reference](https://developer.wordpress.com/docs/api/rest-api-reference/)
- [WordPress.com OAuth Authentication](https://developer.wordpress.com/docs/oauth2/)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Time Trigger Reference](references/time/triggers.md)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/wordpress-api)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, code, configuration]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides authenticated WordPress.com API calls, connection setup, hosted functions, triggers, and least-privilege approval steps.]

## Skill Version(s):

1.2.2 (source: server release metadata; artifact frontmatter metadata.version is 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
