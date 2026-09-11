## Description:

Google Ads API integration with managed OAuth for querying campaigns, ad groups, keywords, and performance metrics with GAQL through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and marketing operators use this skill to inspect Google Ads accounts, run GAQL reports, and perform account operations through the Maton CLI or API gateway. It is suited for campaign, ad group, keyword, and performance workflows where write actions are reviewed before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Maton connection can access the authorized Google Ads account, and write actions can affect campaigns, budgets, ads, audiences, or deleted resources.

Mitigation: Default to read and list operations, then require explicit review of the exact target, payload, and intended effect before any write, deletion, budget, bid, audience, or campaign-state change.

Risk: Long-lived API keys and exposed tokens can leak through logs, shell history, child processes, or persisted files.

Mitigation: Prefer OAuth through the Maton CLI, keep credentials in the operating system credential store, never print or persist secrets, and rotate any key that was exposed.

Risk: Unpinned or unofficial Maton tooling could increase supply-chain risk.

Mitigation: Install Maton only from official Maton sources and verify the installed command before using it for Google Ads operations.

Risk: Google Ads response data can include sensitive business or customer information.

Mitigation: Extract only fields needed for the task and avoid dumping raw responses into logs, files, or user-visible output unless specifically requested.

## Reference(s):

- [Google Ads API Overview](https://developers.google.com/google-ads/api/docs/start)
- [GAQL Reference](https://developers.google.com/google-ads/api/docs/query/overview)
- [GAQL Grammar](https://developers.google.com/google-ads/api/docs/query/grammar)
- [GAQL Cookbook](https://developers.google.com/google-ads/api/docs/query/cookbook)
- [GAQL Fields Reference](https://developers.google.com/google-ads/api/fields/v24/overview)
- [Metrics Reference](https://developers.google.com/google-ads/api/fields/v24/metrics)
- [GoogleAdsService Search](https://developers.google.com/google-ads/api/reference/rpc/v24/GoogleAdsService/Search)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON request and response examples, and Python or JavaScript snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Google Ads API response data; users should extract only the fields needed for the task.]

## Skill Version(s):

1.2.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
