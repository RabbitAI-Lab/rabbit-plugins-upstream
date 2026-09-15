## Description:

Figma API integration with managed OAuth for reading design files, nodes, and version history, rendering nodes as images, managing comments and reactions, and reading published components and styles from a file or team library.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maton](https://clawhub.ai/user/maton)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and automation builders use this skill to inspect Figma files, export node images, review comments and reactions, and audit design-system assets through an authenticated Maton connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A connected Figma account exposes the files and teams the authorized user can already access.

Mitigation: Prefer OAuth, choose the least privilege scopes available, verify the active connection, and limit calls to the files or teams needed for the task.

Risk: Write operations and automation setup can modify shared Figma resources or create ongoing data forwarding.

Mitigation: Get explicit user confirmation for each write, connection change, hosted function, trigger, and trigger destination; review destinations and use restrictive network policy where applicable.

Risk: Raw API keys or environment variables can expose long-lived credentials.

Mitigation: Use OAuth and the OS credential store when possible; use raw HTTP or MATON_API_KEY only when the CLI cannot be installed and avoid logging or persisting credentials.

## Reference(s):

- [ClawHub Figma Skill](https://clawhub.ai/maton/skills/figma)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Figma REST API Introduction](https://developers.figma.com/docs/rest-api/)
- [Figma File Endpoints](https://developers.figma.com/docs/rest-api/file-endpoints/)
- [Figma Comment Endpoints](https://developers.figma.com/docs/rest-api/comments-endpoints/)
- [Figma Component and Style Endpoints](https://developers.figma.com/docs/rest-api/component-endpoints/)
- [Figma Dev Resource Endpoints](https://developers.figma.com/docs/rest-api/dev-resources-endpoints/)
- [Figma Rate Limits](https://developers.figma.com/docs/rest-api/rate-limits/)
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

**Output Format:** [Markdown guidance with shell commands, code snippets, JSON examples, and API request paths.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a Figma connection authorized for the target files or teams.]

## Skill Version(s):

1.2.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
