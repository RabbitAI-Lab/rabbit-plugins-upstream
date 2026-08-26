## Description:

Earnings analysis for US stocks, organized by fiscal quarter with reported results, KPI highlights and year-over-year deltas, management guidance, earnings-call summaries, SEC risk-factor diffs, AI earnings signals, recent reporters, and upcoming earnings calendar context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and financial-research agents use this skill to assemble read-only US stock earnings briefs that keep each claim tied to its fiscal period and report date. It supports single-ticker earnings reviews, recent-reporting sweeps, and pre-earnings previews without trading or write operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends the SentiSense API key to SentiSense for authenticated read-only data calls.

Mitigation: Use an appropriate SentiSense API key, keep it out of shared transcripts and logs, and rotate it if exposure is suspected.

Risk: Financial summaries and AI-generated earnings signals may be incomplete, stale, or unsuitable as a basis for investment decisions.

Mitigation: Treat outputs as research data, verify important claims against source disclosures, and do not present the output as investment advice.

Risk: Optional User-Agent guidance can identify the calling agent or integration.

Mitigation: Use a minimal User-Agent when integration identity is sensitive and avoid including unnecessary agent-specific identifiers.

Risk: Coverage, tier shaping, and empty API responses can make an earnings readout narrower than a reader expects.

Mitigation: State the coverage actually returned, including fiscal periods, dates, preview limits, absent quarters, missing call summaries, and unavailable guidance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/stock-earnings-analysis)
- [SentiSense website](https://sentisense.ai)
- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense API key signup](https://app.sentisense.ai/get-api-key)
- [Publisher profile](https://clawhub.ai/user/thesentitrader)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown earnings-analysis report with fiscal periods, report dates, coverage notes, attribution, and disclaimer.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only financial research output; no trading, purchase, write, or wallet operations.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
