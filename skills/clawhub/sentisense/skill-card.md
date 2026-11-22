## Description:

Connects agents to SentiSense's read-only US equity market data for sentiment, prices, insider and institutional activity, options, analyst ratings, earnings, and AI insights.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use the skill to retrieve and summarize US equity market data, including prices, sentiment, filings, institutional activity, options, analyst views, and earnings. The data is informational and is not investment advice.

### Deployment Geography for Use:

Global (for US equity markets)

## Known Risks and Mitigations:

Risk: The security scan reports that setup runs unpinned downloaded software and uses permissions beyond those declared.

Mitigation: Review the setup instructions and the package/version being run before installation; prefer an existing API key and direct HTTPS data calls when possible.

Risk: The skill documents temporary API-key provisioning, which the security scan says conflicts with its read-only claim.

Mitigation: Use a user-provided key where available. If provisioning is considered, review the CLI or provisioning request first and keep the key and keep link private.

Risk: The scan was partial and could not resolve many local path-like references.

Mitigation: Inspect unresolved referenced files and review the complete package before relying on the scan as a full assessment.

## Reference(s):

- [SentiSense API documentation](https://sentisense.ai/docs/api/)
- [SentiSense website](https://sentisense.ai)
- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/sentisense)
- [Get an API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Market-data responses and concise summaries in JSON or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Coverage and access tiers vary by endpoint; results are informational, not investment advice.]

## Skill Version(s):

2.33.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
