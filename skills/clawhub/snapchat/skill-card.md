## Description:

Snapchat Marketing API integration with managed OAuth for managing ad accounts, campaigns, ad squads, ads, creatives, audiences, and performance reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect a Snapchat advertising account, manage advertising resources, review performance stats, and create approved automations when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OAuth or API-key access can allow actions against Snapchat advertising data and accounts.

Mitigation: Use OAuth where possible, avoid unneeded API-key use, and confirm the exact Snapchat account and resource before acting.

Risk: Ad-changing operations can create, update, or delete Snapchat campaigns, ad squads, ads, creatives, or related resources.

Mitigation: Default to read and list operations, and require explicit user confirmation before write or delete calls.

Risk: Functions, triggers, destinations, or event watching can create ongoing automation or data forwarding.

Mitigation: Create automation only when requested, confirm the function, trigger, destination, and network policy, and prefer narrow access for the approved task.

## Reference(s):

- [Snapchat Skill Page](https://clawhub.ai/byungkyu/skills/snapchat)
- [Maton Homepage](https://maton.ai)
- [Snapchat Ads API Introduction](https://developers.snap.com/api/marketing-api/Ads-API/introduction)
- [Snapchat Ads API Patterns](https://developers.snap.com/api/marketing-api/Ads-API/api-patterns)
- [Snapchat Campaign Management](https://developers.snap.com/api/marketing-api/Ads-API/campaigns)
- [Snapchat Creative Management](https://developers.snap.com/api/marketing-api/Ads-API/creatives)
- [Snapchat Targeting](https://developers.snap.com/api/marketing-api/Ads-API/targeting)
- [Snapchat Ads Gallery API](https://developers.snap.com/api/marketing-api/Ads-Gallery-Api/using-the-api)
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

**Output Type(s):** [Guidance, Markdown, Shell commands, Code, Configuration, API calls]

**Output Format:** [Markdown with shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose authenticated Snapchat API operations and hosted automation steps that require user confirmation before write actions.]

## Skill Version(s):

1.2.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
