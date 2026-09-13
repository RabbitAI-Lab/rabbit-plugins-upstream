## Description:

Provides read-only SentiSense API guidance for assembling US stock earnings reports by fiscal quarter, including reported results, call summaries, KPI highlights, guidance, SEC risk-factor diffs, earnings signals, calendars, ranked reporters, beat-rate baselines, and measured price reactions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, analysts, and research agents use this skill to build US stock earnings readouts that organize reported results, call summaries, KPI highlights, guidance, filing changes, AI signals, calendar data, ranked reporters, beat-rate context, and price reactions by fiscal quarter. The skill is for research summaries and explicitly excludes trading, purchase, wallet, persistence, and write behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Earnings summaries and price-reaction data may be mistaken for personalized investment advice or trading recommendations.

Mitigation: Use the skill for research summaries only and include the required not-investment-advice disclaimer in earnings readouts.

Risk: The skill depends on an external SentiSense API key and sends read-only HTTPS requests to SentiSense.

Mitigation: Provide SENTISENSE_API_KEY only in trusted host environments and confirm that host output and branding policies take precedence where presentation requirements differ.

Risk: A readout can mislead users if it omits API coverage limits, delayed or unavailable call summaries, preview-tier shaping, or pending price reactions.

Mitigation: State fiscal periods, report dates, coverage, unavailable data, preview limits, attribution, and reaction-pending status exactly as returned by the API.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/stock-earnings-analysis)
- [SentiSense website](https://sentisense.ai)
- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense API key page](https://app.sentisense.ai/get-api-key)
- [Publisher profile](https://clawhub.ai/user/thesentitrader)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown earnings readouts with dated fiscal-period claims, API-sourced citations, coverage notes, SentiSense attribution, and investment-disclaimer text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY for read-only HTTPS calls to SentiSense; no shell, local file, trading, purchase, wallet, persistence, or write behavior.]

## Skill Version(s):

1.4.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
