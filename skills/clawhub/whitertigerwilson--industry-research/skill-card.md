## Description:

Industry Research v1.3.2 helps agents produce structured industry, commodity, and equity research reports using CLI-based market data collection, multi-source fallback, ETF linkage, technical indicators, valuation checks, institutional flow signals, and Bocha/Bing news search.

This skill is ready for commercial/non-commercial use.

## Publisher:

[whitertigerwilson](https://clawhub.ai/user/whitertigerwilson)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and finance research agents use this skill to gather public market data, compare related equities and ETFs, analyze technical and valuation signals, and draft industry or commodity research reports. Outputs should be reviewed before investment, commercial, or operational decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill makes direct web and API requests, including Bocha API usage and market data calls.

Mitigation: Install only when direct external requests are acceptable, use HTTPS data sources where possible, and review network behavior before relying on outputs.

Risk: The skill handles API keys and includes a credential environment checker.

Mitigation: Avoid running credential-checking utilities with real secrets and keep API keys out of shared logs, reports, and archives.

Risk: The skill writes local archives, ETF caches, and generated reports.

Mitigation: Treat generated files as untrusted when inputs come from users or external sources, and review storage paths and retained data before deployment.

Risk: The security verdict is suspicious and the evidence says the skill contains unsafe implementation details.

Mitigation: Review and scan the skill before deployment, pin dependencies, and require human review before using research outputs for decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/whitertigerwilson/skills/industry-research)
- [Industry research reference manual](references/research_manual.md)
- [Bocha web search API](https://api.bochaai.com/v1/web-search)
- [Eastmoney quote data source](https://quote.eastmoney.com/)
- [Tencent quote data source](https://qt.gtimg.cn/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown research reports, HTML report files, JSON search results, and CLI text output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write local archives, ETF caches, and generated reports; report content depends on public web and market data source availability.]

## Skill Version(s):

1.3.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
