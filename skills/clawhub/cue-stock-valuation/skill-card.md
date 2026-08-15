## Description:

This skill helps an agent run Cue-powered stock valuation and price analysis across short-term market sentiment, medium-term earnings drivers, and long-term valuation models.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Investors, analysts, and agents researching public equities use this skill to request structured valuation reports for individual stocks, holdings reviews, new-stock research, and peer comparisons. The reports preserve source links and combine funding-flow, earnings, valuation, safety-margin, and risk-factor analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uses a Cue API key and sends stock research queries to cuecue.cn.

Mitigation: Confirm trust in the Cue service and referenced runner repository before installing or running the workflow, and avoid including sensitive information in queries.

Risk: Generated valuation reports may be mistaken for investment advice.

Mitigation: Treat generated reports as research input, preserve source links, and review the evidence before making investment decisions.

Risk: Cue service availability and external market-data sources can affect report freshness or completeness.

Mitigation: Run the documented health checks before research tasks and review any source-availability notes in generated reports.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-stock-valuation)
- [Cue runner repository](https://github.com/sensedeal/cue-skills)
- [Cue API key setup](https://cuecue.cn/hub/api-key)
- [Cue sample valuation report](https://cuecue.cn/share/NMJ36JGzIwOx8SPJXB_WR)

## Skill Output:

**Output Type(s):** [markdown, text, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with inline shell commands, configuration notes, and source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated Markdown reports can be converted to DOCX or PDF with pandoc when the optional conversion tools are installed.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
