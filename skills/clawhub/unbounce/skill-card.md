## Description:

Unbounce API integration with managed OAuth for building and managing landing pages, tracking leads, and analyzing conversion data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to connect an authorized Unbounce account through Maton, inspect accounts, pages, leads, domains, page groups, and users, and perform approved landing-page or lead-management operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write operations, new connections, function deployment, triggers, and destinations can change Unbounce data or create continuing automation.

Mitigation: Start with read and list calls, and obtain explicit user approval for writes, connection creation, hosted functions, triggers, destinations, and deletions.

Risk: Unbounce leads and page data can include personal or business-sensitive information.

Mitigation: Use OAuth, select the intended connection, avoid dumping full responses, and extract only the fields needed for the user's task.

Risk: API-key fallback uses a long-lived credential, and MATON_API_KEY overrides the active profile.

Mitigation: Prefer OAuth and OS credential-store login; use raw HTTP or API keys only where the CLI cannot be installed, and avoid exposing keys in commands, logs, or files.

Risk: Hosted functions and triggers can keep running after the original task is complete.

Mitigation: Use private functions, prefer DENY_ALL network policy, review the target account, resource, and payload before approval, and delete automation when it is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/unbounce)
- [Maton homepage](https://maton.ai)
- [Unbounce API Documentation](https://developer.unbounce.com/api_reference/)
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

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, API paths, JSON examples, and small code snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and user-approved OAuth or API-key authentication before live API calls.]

## Skill Version(s):

1.2.5 (source: server release evidence; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
