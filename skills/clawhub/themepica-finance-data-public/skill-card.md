## Description:

Themepica Finance Data Public wraps Themepica public finance APIs for theme investing, hotspot rankings, ETF narratives, index quotes, and fund narrative data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yyri](https://clawhub.ai/user/yyri)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to call Themepica public financial data APIs for theme analysis, market hotspot discovery, ETF and fund narrative data, and index market data. The returned market signals should be treated as analytical data rather than financial advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API calls send the configured APPCODE and query parameters to Themepica.

Mitigation: Prefer the THEMEPICA_APPCODE environment variable, avoid committing real credentials in mcp_config.json, and run only intended requests.

Risk: Returned market signals may be mistaken for financial advice.

Mitigation: Treat responses as data for analysis and apply independent financial review before making investment decisions.

Risk: Invalid parameters can produce API errors or unnecessary quota usage.

Mitigation: Follow the documented required fields, date formats, and pagination limits before invoking each endpoint.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yyri/skills/themepica-finance-data-public)
- [Themepica homepage](https://www.themepica.com)
- [Theme API reference](artifact/references/themes.md)
- [Hotspot API reference](artifact/references/hotspot.md)
- [Board API reference](artifact/references/board.md)
- [Fund API reference](artifact/references/fund.md)
- [Index API reference](artifact/references/index.md)
- [ETF API reference](artifact/references/etf.md)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Code, Guidance]

**Output Format:** [JSON API responses with Markdown guidance and inline shell or JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided Themepica APPCODE; public API calls are routed to Themepica endpoints.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
