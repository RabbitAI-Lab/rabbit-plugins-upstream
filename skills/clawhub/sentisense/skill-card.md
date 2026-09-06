## Description:

SentiSense gives agents read-only access to US stock market data, including sentiment, ratings, filings, institutional flows, options positioning, analyst ratings, earnings calendars, AI market insights, and delayed prices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to retrieve read-only US equity market intelligence for financial research workflows, including sentiment monitoring, market dashboards, screening, and earnings or disclosure analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional CLI path can run a downloaded npm package with the user's API key and store that key on disk.

Mitigation: Prefer direct HTTPS REST examples with SENTISENSE_API_KEY in the environment; use the CLI auth flow only after reviewing and trusting the exact npm package version and knowing how to rotate or revoke the key.

Risk: The personalized user insights endpoint can expose account-personalized data.

Mitigation: Call /api/v1/insights/user only for explicit personalized-analysis requests.

## Reference(s):

- [SentiSense API Docs](https://sentisense.ai/docs/api/)
- [SentiSense Homepage](https://sentisense.ai)
- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/sentisense)
- [SentiSense Python SDK](https://github.com/SentiSenseApp/sentisense)
- [SentiSense Node.js SDK](https://github.com/SentiSenseApp/sentisense-node)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with REST examples, shell commands, code snippets, and JSON API response descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY; direct HTTPS REST calls are preferred over optional SDK or CLI use.]

## Skill Version(s):

2.12.17 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
