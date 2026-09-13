## Description:

Google Ads API integration with managed OAuth for querying campaigns, ad groups, keywords, and performance metrics with GAQL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and marketing operations teams use this skill to connect a Maton-authenticated Google Ads account, run read-first GAQL/API queries, and perform approved campaign or automation actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Google Ads access and automation can expose sensitive account data or affect campaign state.

Mitigation: Prefer read and list operations, connect only the needed Google Ads account, and require clear confirmation before any campaign, budget, trigger, destination, or hosted function change.

Risk: Long-lived API keys can be exposed through environment variables, logs, committed files, or pasted output.

Mitigation: Prefer OAuth, keep credentials in the operating system credential store, avoid exporting MATON_API_KEY, and rotate any key that was printed, committed, or pasted.

Risk: Hosted functions and triggers can run approved actions unattended or send event data to unintended destinations.

Mitigation: Use user-authored or user-reviewed handlers, keep functions private, deploy with DENY_ALL network policy by default, and route only to Maton/internal destinations unless the user approves a named external host.

## Reference(s):

- [Google Ads API Overview](https://developers.google.com/google-ads/api/docs/start)
- [GAQL Reference](https://developers.google.com/google-ads/api/docs/query/overview)
- [GAQL Grammar](https://developers.google.com/google-ads/api/docs/query/grammar)
- [GAQL Cookbook](https://developers.google.com/google-ads/api/docs/query/cookbook)
- [GAQL Fields Reference](https://developers.google.com/google-ads/api/fields/v24/overview)
- [Metrics Reference](https://developers.google.com/google-ads/api/fields/v24/metrics)
- [GoogleAdsService Search](https://developers.google.com/google-ads/api/reference/rpc/v24/GoogleAdsService/Search)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Maton Homepage](https://maton.ai)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Time Trigger Reference](references/time/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and explicit user approval for writes, connection changes, hosted functions, triggers, or destinations.]

## Skill Version(s):

1.2.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
