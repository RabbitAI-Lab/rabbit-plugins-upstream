## Description:

Tracks U.S. congressional stock-trade disclosures by recent activity, ticker, member, and trading frequency using House Clerk and Senate eFD filing data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to answer questions about U.S. congressional trading activity, including recent disclosures, ticker-specific histories, and member profiles. It is informational only and does not support trading, order entry, wallet access, or personalized financial advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends a SentiSense API key to app.sentisense.ai for read-only congressional trading data.

Mitigation: Use a dedicated, revocable API key, keep it in the environment, and avoid placing it in query strings or user-facing output.

Risk: The optional CLI path executes the third-party sentisense npm package.

Mitigation: Use the documented curl workflows if you do not want to execute npm package code; otherwise treat sentisense@0.52.0 like any third-party dependency.

Risk: Congressional disclosure data can be misread as precise transaction values or personalized trading guidance.

Mitigation: Report amount ranges, distinguish transaction dates from disclosure dates, and present results as informational context rather than buy or sell recommendations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/politicians-stock-tracker)
- [SentiSense](https://sentisense.ai)
- [SentiSense API application](https://app.sentisense.ai)
- [SentiSense API key page](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and summarized API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only informational output; API responses are wrapped JSON envelopes and may be preview-limited depending on account tier.]

## Skill Version(s):

1.1.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
