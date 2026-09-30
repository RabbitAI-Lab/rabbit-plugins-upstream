## Description:

Helps agents manage ActiveCampaign contacts, deals, campaigns, and automations through a connected Maton account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People managing an ActiveCampaign account use this skill to look up and, with explicit approval, change CRM records, campaigns, and account settings. They can also configure approved functions and triggers to automate related actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Changes to contacts, campaigns, or shared account resources can have unintended effects.

Mitigation: Start with read-only queries; confirm the target and effect with the user before every write or new connection.

Risk: Webhooks, triggers, functions, and destinations can create ongoing data flows or automated changes.

Mitigation: Confirm the event scope, destination, and intended automation separately before enabling them; forward only necessary data.

Risk: CRM records and event payloads may contain personal or sensitive data.

Mitigation: Keep credentials in the supported credential store and avoid exposing full responses or event payloads unnecessarily.

## Reference(s):

- [ClawHub ActiveCampaign skill release](https://clawhub.ai/byungkyu/skills/active-campaign)
- [Maton homepage](https://maton.ai)
- [ActiveCampaign API overview](https://developers.activecampaign.com/reference/overview)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Calendly trigger reference](references/calendly/triggers.md)
- [GitHub trigger reference](references/github/triggers.md)
- [Gmail trigger reference](references/google-mail/triggers.md)
- [HubSpot trigger reference](references/hubspot/triggers.md)
- [Linear trigger reference](references/linear/triggers.md)
- [Notion trigger reference](references/notion/triggers.md)
- [Slack trigger reference](references/slack/triggers.md)
- [Stripe trigger reference](references/stripe/triggers.md)
- [Time trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with command and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions require network access and an authorized Maton connection.]

## Skill Version(s):

1.2.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
