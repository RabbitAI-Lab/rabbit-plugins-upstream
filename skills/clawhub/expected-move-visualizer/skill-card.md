## Description:

Expected Move Visualizer turns SentiSense options data for a stock or ETF into a self-contained HTML chart of modeled 30, 60, and 90 day expected-move ranges, IV rank context, skew, and upcoming earnings context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and external users can use this skill to generate an offline HTML expected-move visualization for a chosen stock or ETF from a bound SentiSense market-data snapshot. The output is educational market context, not investment advice or a trading recommendation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated HTML has a script-injection hardening gap in the data-binding path.

Mitigation: Install only after review, prefer trusted SentiSense data snapshots, and update the binding flow to serialize JSON safely for script contexts before broader deployment.

Risk: Generated reports include unavoidable SentiSense promotion.

Mitigation: Disclose the promotional content to users and make promotion optional or clearly separated from the analytical output.

Risk: Users may overread modeled expected-move bands as predictions or trading advice.

Mitigation: Present the HTML output as educational market context, keep the modeled and delayed-data caveats visible, and avoid buy, sell, target, or support/resistance language.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/expected-move-visualizer)
- [Publisher profile](https://clawhub.ai/user/thesentitrader)
- [SentiSense](https://sentisense.ai)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown instructions with shell commands and generated self-contained HTML files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY for read-only market-data requests at build time; generated HTML is intended to render offline.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
