## Description:

Ticker Pipeline coordinates specialized agents to research a stock ticker and date, combining fundamentals, valuation, market activity, news, sentiment, macro context, and an independent risk veto into a structured investment research report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fize](https://clawhub.ai/user/fize)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run a multi-agent equity research workflow for a selected ticker and date. It produces a decision-oriented Markdown report only when required market, financial, technical, and news data are available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Financial analysis may rely on broad market and web data that can be incomplete, stale, or unavailable.

Mitigation: Verify key market, financial, technical, and news data against authoritative sources, and halt report generation when core data is missing.

Risk: The report can include prescriptive ratings or trading-oriented guidance.

Mitigation: Treat outputs as informational research and require human review before any investment decision or trade.

Risk: The workflow can create report files using ticker-derived names.

Mitigation: Confirm the write location and sanitize ticker or company-name inputs before creating files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fize/skills/ticker-pipeline)
- [ClawHub publisher profile](https://clawhub.ai/user/fize)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown report with structured JSON fact blocks and optional workspace report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and market or authoritative web data; core data gaps halt report generation.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
