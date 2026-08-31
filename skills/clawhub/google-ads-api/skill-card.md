## Description:

Google Ads API integration with managed OAuth for querying campaigns, ad groups, keywords, and performance metrics with GAQL through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to connect to Google Ads through Maton, inspect account and campaign data, run GAQL queries, and prepare changes to campaigns, ads, keywords, budgets, or other account resources with explicit user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill grants Maton-mediated access to a Google Ads account.

Mitigation: Prefer OAuth, review the selected account and scopes carefully, and connect only the accounts needed for the current task.

Risk: Write operations can change campaigns, ads, keywords, budgets, or other account data.

Mitigation: Default to read and list calls, then require explicit user confirmation of the target resource, payload, and intended effect before any create, update, or delete operation.

Risk: Long-lived API keys or provider-issued tokens could be exposed through logs, files, shell history, or command-line arguments.

Mitigation: Use OAuth and the operating system credential store when possible; if raw HTTP is unavoidable, do not print or persist the key and pass authorization through stdin as documented.

Risk: Ambiguous Maton profiles, Google Ads connections, or manager accounts could send requests to the wrong account.

Mitigation: Specify the intended profile, connection, customer ID, and manager login customer ID whenever more than one account or connection may exist.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-ads-api)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Google Ads API Overview](https://developers.google.com/google-ads/api/docs/start)
- [GAQL Reference](https://developers.google.com/google-ads/api/docs/query/overview)
- [GAQL Fields Reference](https://developers.google.com/google-ads/api/fields/v24/overview)
- [Google Ads Search Method](https://developers.google.com/google-ads/api/reference/rpc/v24/GoogleAdsService/Search)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Configuration, Guidance, Code]

**Output Format:** [Markdown with bash, JSON, SQL, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and explicit confirmation before creating connections or modifying Google Ads data.]

## Skill Version(s):

1.1.0 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
