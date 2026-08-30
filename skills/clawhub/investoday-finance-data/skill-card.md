## Description:

Fetches Chinese financial-market data and investment research across A-shares, Hong Kong stocks, funds, indices, financials, announcements, research reports, macro data, and other structured datasets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kenneth-bro](https://clawhub.ai/user/kenneth-bro)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, and developers use this skill to locate and call InvestToday financial-data endpoints for market quotes, fundamentals, fund data, announcements, research, macro indicators, and structured research exports. It supports research workflows but is not for personalized trading advice, automated order execution, or inventing conclusions when data is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API key setup may persist credentials or expose them through command-line arguments.

Mitigation: Prefer interactive initialization, avoid passing real API keys directly on the command line, check the CLI config path, and remove stored credentials when done.

Risk: Background updates may modify installed skill or CLI assets.

Mitigation: Prefer --no-auto-update or review update behavior before enabling automatic updates.

Risk: Financial examples or generated analysis may be mistaken for personalized investment advice.

Mitigation: Treat outputs as research inputs, avoid direct buy or sell recommendations, and state data limits when results are unavailable or incomplete.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/kenneth-bro/skills/investoday-finance-data)
- [English Skill Overview](artifact/SKILL_EN.md)
- [API Reference Index](artifact/docs/references-index.en.md)
- [Market Data Reference](artifact/references/市场数据.md)
- [A-share Financial Data Reference](artifact/references/沪深京数据/财务数据/三大报表当期数据.md)
- [Fund Reference](artifact/references/基金/基金财务数据.md)
- [Hong Kong Stock Reference](artifact/references/港股/基础数据.md)
- [Macro Economy Reference](artifact/references/宏观经济/国内宏观.md)
- [Research Report Reference](artifact/references/研报/基础数据.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or text with CLI commands and structured financial-data summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include endpoint names, required parameters, command examples, returned data summaries, and limitation statements when data is unavailable.]

## Skill Version(s):

1.8.77 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
