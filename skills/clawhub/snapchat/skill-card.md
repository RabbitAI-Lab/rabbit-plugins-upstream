## Description:

Snapchat Marketing API integration with managed OAuth for managing ad accounts, campaigns, ad squads, ads, creatives, audiences, and performance stats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketing operators, and developers use this skill to access Snapchat Marketing API workflows through Maton, including campaign management, ad performance review, targeting, creatives, and audience operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated write operations can modify Snapchat advertising resources or trigger downstream side effects.

Mitigation: Default to read and list calls, verify identifiers and current state first, and require explicit user approval before every POST, PUT, PATCH, DELETE, workflow trigger, or deletion.

Risk: Connections, hosted functions, triggers, and destinations can create persistent access or automation after the initial task.

Mitigation: Confirm each connection, deployment, trigger, destination, and invocation separately; show the target account, connection, destination host, payload fields, and persistence before approval.

Risk: Persistent event forwarding can continue sending future business or personal data until removed.

Mitigation: Prefer Maton-controlled destinations, forward only the minimum fields needed, avoid public inspection endpoints, review existing destinations, and remove forwarding that is no longer needed.

Risk: OAuth tokens or API keys can expose account access if printed, logged, embedded in destinations, or stored insecurely.

Mitigation: Use OAuth where possible, rely on the operating system credential store, avoid exposing MATON_API_KEY to child processes, never place Maton or provider credentials in destination headers or templates, and rotate any exposed key.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/snapchat)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Snapchat Ads API Introduction](https://developers.snap.com/api/marketing-api/Ads-API/introduction)
- [Snapchat API Patterns](https://developers.snap.com/api/marketing-api/Ads-API/api-patterns)
- [Snapchat Campaign Management](https://developers.snap.com/api/marketing-api/Ads-API/campaigns)
- [Snapchat Creative Management](https://developers.snap.com/api/marketing-api/Ads-API/creatives)
- [Snapchat Targeting](https://developers.snap.com/api/marketing-api/Ads-API/targeting)
- [Snapchat Ads Gallery API](https://developers.snap.com/api/marketing-api/Ads-Gallery-Api/using-the-api)
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

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and user-approved OAuth or API-key authentication.]

## Skill Version(s):

1.2.3 (source: server release metadata; artifact frontmatter lists 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
