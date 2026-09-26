## Description:

Helps agents look up U.S. congressional stock disclosures by member or ticker and summarize reported trades, amounts, and disclosure delays through the read-only SentiSense API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, developers, and other users can investigate public U.S. congressional trading disclosures by member or ticker, compare disclosure and transaction dates, and summarize reported activity without placing trades or receiving personalized investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The SentiSense API receives the user's API key; an optional User-Agent may identify the agent runtime.

Mitigation: Keep the key in the environment, send it only to app.sentisense.ai, and omit optional runtime identifiers if disclosure is unwanted.

Risk: Public disclosure data can be incomplete or misread as a trading signal or financial advice.

Mitigation: Label preview and partial results, distinguish trade dates from filing dates, quote reported amount ranges, and avoid personalized trading recommendations.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/thesentitrader/skills/politicians-stock-tracker)
- [SentiSense](https://sentisense.ai)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown summaries and example HTTP GET commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summaries should distinguish transaction from disclosure dates, preserve reported amount ranges, and identify preview or partial results.]

## Skill Version(s):

1.1.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
