## Description:

Google Ads API integration with managed OAuth for querying campaigns, ad groups, keywords, and performance metrics with GAQL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and marketing operators use this skill to authenticate Google Ads through Maton, query account performance data, and run approved Google Ads actions or automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires authorizing Maton to access a Google Ads account.

Mitigation: Use OAuth where possible, select the least privilege scopes available, and verify the target account and connection before running account-specific commands.

Risk: Google Ads changes, hosted functions, triggers, and destination forwarding can affect budgets, bidding, campaign status, or business data movement.

Mitigation: Default to read and list calls, summarize high-impact actions first, and require explicit approval before writes, new connections, functions, triggers, or forwarding destinations.

Risk: Long-lived API keys and destination headers can expose credentials if copied into environments, logs, or third-party receivers.

Mitigation: Prefer OAuth and the operating system credential store; use raw HTTP only when the CLI cannot be installed, rotate exposed keys, and never place Maton or provider tokens in trigger destination headers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/google-ads-api)
- [Maton homepage](https://maton.ai)
- [Google Ads API Overview](https://developers.google.com/google-ads/api/docs/start)
- [GAQL Reference](https://developers.google.com/google-ads/api/docs/query/overview)
- [GAQL Grammar](https://developers.google.com/google-ads/api/docs/query/grammar)
- [GAQL Cookbook](https://developers.google.com/google-ads/api/docs/query/cookbook)
- [Google Ads Fields Reference](https://developers.google.com/google-ads/api/fields/v24/overview)
- [Google Ads Metrics Reference](https://developers.google.com/google-ads/api/fields/v24/metrics)
- [Google Ads Search API](https://developers.google.com/google-ads/api/reference/rpc/v24/GoogleAdsService/Search)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](references/time/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Code, Configuration, Guidance]

**Output Format:** [Markdown with bash, Python, and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the authenticated user's Maton connection and favors read/list operations unless the user explicitly approves writes, new connections, hosted functions, triggers, or destination forwarding.]

## Skill Version(s):

1.2.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
