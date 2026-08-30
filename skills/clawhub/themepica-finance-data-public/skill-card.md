## Description:

Provides access to Themepica public financial data APIs for theme investing, hotspot rankings, ETF narratives, index market data, and fund narratives.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yyri](https://clawhub.ai/user/yyri)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to query Themepica public financial-data APIs for market themes, hotspots, rankings, ETF, index, and fund narrative signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API queries and the APPCODE are sent to Themepica.

Mitigation: Use the THEMEPICA_APPCODE environment variable, avoid committing credentials in mcp_config.json, and review whether submitted queries are appropriate for the deployment context.

Risk: Returned financial analytics may be incomplete, stale, or unsuitable as trading instructions.

Mitigation: Treat results as informational research signals and require human review before investment or trading decisions.

Risk: External API access can fail because of authentication, quota, billing, rate limits, or service availability.

Mitigation: Handle non-200 responses and documented API error codes before relying on output in downstream workflows.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/yyri/skills/themepica-finance-data-public)
- [Themepica homepage](https://www.themepica.com)
- [Theme API reference](artifact/references/themes.md)
- [Hotspot API reference](artifact/references/hotspot.md)
- [Board API reference](artifact/references/board.md)
- [Index API reference](artifact/references/index.md)
- [ETF API reference](artifact/references/etf.md)
- [Fund API reference](artifact/references/fund.md)

## Skill Output:

**Output Type(s):** [text, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JavaScript and shell command examples; API responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Themepica APPCODE supplied through THEMEPICA_APPCODE or local configuration.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
