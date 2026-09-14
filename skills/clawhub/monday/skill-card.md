## Description:

Provides Monday.com API integration with managed OAuth for managing boards, items, columns, groups, workspaces, and account context through GraphQL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and workflow operators use this skill to query and manage Monday.com boards, items, users, columns, groups, and workspaces. It also guides approved Monday.com automations through Maton-managed authentication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connected Monday.com account may allow real changes to boards, items, columns, groups, workspaces, and workflows.

Mitigation: Default to read and list operations, and require explicit user approval for every mutation or automation.

Risk: Over-broad accounts or OAuth scopes can expose more Monday.com data than the task needs.

Mitigation: Use OAuth where possible, connect the narrowest account and scopes available, and revoke unused connections promptly.

Risk: Third-party trigger destinations can disclose business or personal data outside the platform.

Mitigation: Avoid third-party trigger destinations unless the user controls and trusts the host, and prefer platform-hosted destinations for automations.

Risk: Global CLI or SDK installation can introduce package-provenance risk.

Mitigation: Install reviewed, pinned Maton packages and verify Maton package provenance before installing or upgrading.

## Reference(s):

- [Monday.com ClawHub Listing](https://clawhub.ai/byungkyu/skills/monday)
- [Maton Homepage](https://maton.ai)
- [Monday.com API Basics](https://developer.monday.com/api-reference/docs/basics)
- [GraphQL Overview](https://developer.monday.com/api-reference/docs/introduction-to-graphql)
- [Boards Reference](https://developer.monday.com/api-reference/reference/boards)
- [Items Reference](https://developer.monday.com/api-reference/reference/items)
- [Columns Reference](https://developer.monday.com/api-reference/reference/columns)
- [API Changelog](https://developer.monday.com/api-reference/changelog)
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

**Output Type(s):** [guidance, shell commands, code, configuration, API calls]

**Output Format:** [Markdown guidance with bash, JSON, GraphQL, Python, and HTTP examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and valid OAuth or API-key authentication; mutations and automations require explicit user approval.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
