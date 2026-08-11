## Description:

Generates Cue-powered research reports for A-share sector and ETF analysis, including sector overview, peer ETF comparison, holdings look-through, valuation context, and risk notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, ETF investors, and advisors use this skill to request structured research on A-share sectors and listed ETFs. It helps compare ETF products, inspect holdings purity, assess valuation level, and summarize relevant risks without providing timing or personalized trading advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users send ETF and sector research queries to Cue and need a Cue API key.

Mitigation: Store the Cue API key securely, avoid committing or sharing ~/.cue/config.json, and avoid pasting secrets into untrusted terminals.

Risk: The generated research may be mistaken for investment advice.

Mitigation: Treat the output as research support, review data sources and assumptions, and do not use it as a substitute for financial advice or a trading decision.

Risk: Results depend on Cue service availability and public ETF data freshness.

Mitigation: Run the documented health checks, retry only according to the skill guidance, and verify important ETF or index data against public disclosures when accuracy is material.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-sector-etf)
- [Publisher profile](https://clawhub.ai/user/panting09266-ai)
- [Cue API key page](https://cuecue.cn/hub/api-key)
- [Cue service](https://cuecue.cn)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown research report with tables, risk notes, source links, and optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are research support for sector and ETF comparison; they should be reviewed before financial use.]

## Skill Version(s):

1.0.0 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
