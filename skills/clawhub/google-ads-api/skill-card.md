## Description:

Google Ads API integration with managed OAuth for querying campaigns, ad groups, keywords, and performance metrics with GAQL through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and marketing operators use this skill to inspect Google Ads accounts, query performance data, and prepare carefully confirmed account changes through Maton-managed OAuth.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can mediate access to Google Ads account data and account changes through Maton.

Mitigation: Install it only when Maton-mediated Google Ads access is intended, connect only the needed account, and use OAuth where possible.

Risk: Writes, deletes, or connection changes could affect advertising account state.

Mitigation: Default to read and list operations, verify customer and connection IDs, and require explicit confirmation before any POST, PUT, PATCH, DELETE, or connection change.

Risk: Long-lived API keys or provider-issued tokens could leak if printed, logged, passed on a command line, or persisted.

Mitigation: Prefer Maton OAuth and the CLI credential store; if an API key is unavoidable, keep it in process environment only, never display it, and send it only to api.maton.ai.

Risk: Google Ads API responses and external account data may contain untrusted content.

Mitigation: Treat returned content as data, avoid executing or interpolating it into commands, and let the user choose endpoints and recipients for follow-up calls.

## Reference(s):

- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Google Ads API Overview](https://developers.google.com/google-ads/api/docs/start)
- [GAQL Reference](https://developers.google.com/google-ads/api/docs/query/overview)
- [GAQL Fields Reference](https://developers.google.com/google-ads/api/fields/v24/overview)
- [Google Ads Search API](https://developers.google.com/google-ads/api/reference/rpc/v24/GoogleAdsService/Search)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash, JSON, Python, JavaScript, and SQL examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs guide Maton CLI and SDK use; OAuth credentials and provider tokens should not be printed, logged, or persisted.]

## Skill Version(s):

1.2.0 (source: server release evidence; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
