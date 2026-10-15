## Description:

Compare matched public event forecasts across Polymarket, Kalshi, and Metaculus while preserving resolution rules, outcome labels, scales, timestamps, liquidity, and methodological differences.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and other users compare precisely matched public event forecasts to prepare source-attributed consensus briefs and dated divergence analyses, without placing trades.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Crawlora API key is required, and forecast search terms and route parameters are sent to Crawlora.

Mitigation: Confirm that the key and requested data may be shared with Crawlora; scope requests to the needed comparison.

Risk: Different resolution rules, timing, scales, or liquidity may make forecast gaps misleading if interpreted as actionable trading signals.

Mitigation: Verify proposition and outcome matches, show source dates and comparability limits, and do not treat the analysis as trading advice or automation.

## Reference(s):

- [Skill release on ClawHub](https://clawhub.ai/crawlora-org/skills/forecast-consensus-comparison)
- [Forecast endpoint reference](reference/endpoints.md)
- [Crawlora API](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown tables and narrative]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Source-attributed proposition matches, dated snapshots or history, divergence calculations when comparable, and uncertainty notes.]

## Skill Version(s):

1.0.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
