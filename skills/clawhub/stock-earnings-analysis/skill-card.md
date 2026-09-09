## Description:

Provides read-only US stock earnings analysis organized by fiscal quarter, including reported results, KPI highlights, guidance language, earnings call summaries, SEC risk-factor diffs, earnings signals, recent reporters, and upcoming report dates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External analysts, investors, and agent builders use this skill to assemble SentiSense API data into quarter-centric earnings readouts, recent-reporter briefs, and pre-earnings previews for US stocks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends stock ticker queries and the SentiSense API key to app.sentisense.ai.

Mitigation: Use a scoped SentiSense API key from the environment, disclose the outbound API host, and avoid granting credentials with trading, write, wallet, or account-modification scope.

Risk: Financial earnings summaries can be mistaken for personalized investment advice.

Mitigation: Preserve the fixed attribution, coverage, and not-investment-advice disclaimer, and avoid recommendations to buy or sell securities.

Risk: API responses may be partial, delayed, or shaped by account tier.

Mitigation: Carry fiscal periods, report dates, generated timestamps, free-preview limits, and explicit absence statements in the output.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/stock-earnings-analysis)
- [SentiSense API Reference](https://sentisense.ai/skill.md)
- [SentiSense Website](https://sentisense.ai)
- [SentiSense API Key Signup](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Guidance]

**Output Format:** [Markdown earnings readouts with API-sourced fields, coverage notes, attribution, and disclaimer text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY; performs read-only HTTPS calls to app.sentisense.ai; does not write files, execute shell commands, trade, purchase, or modify accounts.]

## Skill Version(s):

1.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
