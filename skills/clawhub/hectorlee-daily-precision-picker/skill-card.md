## Description:

Screens Chinese A-share candidates through a four-layer volume-price, fundamentals, capital-flow, and sector-quality funnel to produce daily tiered stock watchlists or no-pick guidance when candidates do not qualify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiyanjun](https://clawhub.ai/user/xiyanjun)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to screen a candidate pool of Chinese A-share stocks and produce daily selected, preferred, and watchlist tiers with scoring details, sector distribution, exclusions, and a non-advisory risk note.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Malformed stock-code input can influence local shell command execution in the helper script.

Mitigation: Run only with trusted candidate lists until a fixed version validates ticker format and invokes subprocess with an argument list and shell=False.

Risk: Finance outputs may be misleading when market, fundamental, fund-flow, sector, or historical signal data is unavailable or stale.

Mitigation: Review the report's data availability markers and treat no-data or degraded-mode scores as lower-confidence screening output, not investment advice.

## Reference(s):

- [Research Findings](references/research_findings.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Analysis, Guidance]

**Output Format:** [Markdown report with tables, scoring breakdowns, sector distribution, command guidance, and risk notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are based on candidate stock codes and available market, fundamental, fund-flow, sector, and historical signal data; missing data is disclosed and may lower confidence.]

## Skill Version(s):

0.1.3 (source: server release metadata; artifact frontmatter and manifest report 2.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
