## Description:

LinkedIn API integration with managed OAuth for sharing posts, managing profiles and organizations, accessing ad features, and creating approved LinkedIn automations through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to work with LinkedIn through a managed OAuth connection: read profile, organization, ad, and library data; create approved posts or campaign changes; and wire scheduled or event-driven actions when the user has explicitly requested automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: LinkedIn write, delete, publishing, and advertising operations can affect public content, account data, ad delivery, or budgets.

Mitigation: Default to read and list operations; before any write or destructive call, confirm the exact operation, target account or resource, payload, scopes, budget, and irreversible effects with the user.

Risk: Hosted functions, triggers, and destinations can create persistent automation or ongoing data forwarding.

Mitigation: Create them only after separate approval, disclose what runs and where data flows, prefer Maton-controlled destinations, and remove functions, triggers, or destinations when no longer needed.

Risk: Long-lived credentials and broad OAuth scopes increase exposure if reused or leaked.

Mitigation: Prefer OAuth, approve only the LinkedIn scopes and accounts needed, avoid exporting API keys, and revoke unused connections promptly.

## Reference(s):

- [ClawHub LinkedIn skill page](https://clawhub.ai/byungkyu/skills/linkedin-api)
- [Maton homepage](https://maton.ai)
- [Maton docs](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [LinkedIn Ad Accounts documentation](https://learn.microsoft.com/en-us/linkedin/marketing/integrations/ads/account-structure/create-and-manage-accounts)
- [LinkedIn Campaign Management documentation](https://learn.microsoft.com/en-us/linkedin/marketing/integrations/ads/account-structure/create-and-manage-campaigns)
- [Time trigger reference](artifact/references/time/triggers.md)
- [Gmail trigger reference](artifact/references/google-mail/triggers.md)
- [GitHub trigger reference](artifact/references/github/triggers.md)
- [Slack trigger reference](artifact/references/slack/triggers.md)
- [Stripe trigger reference](artifact/references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized LinkedIn connection; write operations and automations require explicit user approval.]

## Skill Version(s):

1.2.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
