## Description: <br>
股票九剑 analyzes Chinese A-share stock codes by fetching market data, computing technical indicators, matching nine short-term trading patterns, and producing a structured judgment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yhc2026](https://clawhub.ai/user/yhc2026) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to analyze Chinese A-share stock codes, review short-term technical signals, generate optional charts, and receive structured risk-aware trading analysis. Outputs should be treated as automated market analysis rather than financial advice. <br>

### Deployment Geography for Use: <br>
Global; analysis is specific to Chinese A-share market data. <br>

## Known Risks and Mitigations: <br>
Risk: Queried stock codes may be sent to third-party public market-data providers. <br>
Mitigation: Use the skill only when this data sharing is acceptable, and avoid submitting sensitive private watchlists or confidential trading intent. <br>
Risk: Automated buy/sell, position, confidence, and risk outputs may be incorrect or misleading. <br>
Mitigation: Treat outputs as market analysis rather than financial advice, and verify against independent sources before making trades. <br>
Risk: Optional chart generation writes image files locally. <br>
Mitigation: Review local chart output paths and remove generated images when they are no longer needed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/yhc2026/skills/gupiaojiujiang) <br>
- [独孤九剑 Framework](knowledge/framework.md) <br>
- [MCP Platform Configuration Guide](mcp_server/PLATFORM_CONFIGS.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Files, Guidance] <br>
**Output Format:** [Markdown-style analysis reports, JSON MCP tool responses, shell command snippets, configuration examples, and optional PNG chart files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May query third-party public market-data providers and may write chart images locally when chart generation is requested.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
