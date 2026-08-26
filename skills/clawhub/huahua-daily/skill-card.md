## Description:

Queries and analyzes HuahuaDaily fund holdings, market data, transactions, quantitative context, and community data, and creates trade or import requests that require user confirmation in the HuahuaDaily App.

This skill is ready for commercial/non-commercial use.

## Publisher:

[baiye1997](https://clawhub.ai/user/baiye1997)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to inspect HuahuaDaily portfolio, fund, market, quantitative, report, and community information, and to prepare App-confirmed trade or import requests. The skill is intended for users who can provide a HuahuaDaily Agent Token and need agent-assisted financial data review without bypassing App confirmation for trades and imports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive investment data and HuahuaDaily Agent Tokens.

Mitigation: Install only if the publisher is trusted, keep the Agent Token in environment configuration, and avoid exposing or repeating the token in chat.

Risk: Broad dependency ranges for mcp and pydantic need review before high-trust deployment.

Mitigation: Review dependencies before installation and ask the publisher to pin or raise dependency versions for stricter production controls.

Risk: Community, report, and quantitative write actions can change backend state.

Mitigation: Confirm the user's intent before these actions, reuse idempotency IDs on retries where supported, and prefer read-only analysis unless the user explicitly asks for a write.

Risk: Trades and imports prepared by the agent may be mistaken for completed portfolio changes.

Mitigation: Treat trade and import tools as request creation only and tell the user that completion still requires confirmation in the HuahuaDaily App.

Risk: Incomplete, stale, timeout, or unavailable market and portfolio data can produce misleading financial conclusions.

Mitigation: Disclose freshness and completeness limits, distinguish official net values from intraday estimates or night-session references, and do not present missing data as zero movement.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/baiye1997/skills/huahua-daily)
- [Portfolio reference](references/portfolio.md)
- [Fund and market reference](references/fund-market.md)
- [Trade and import reference](references/trade-import.md)
- [Quant reference](references/quant.md)
- [Community and reports reference](references/community-reports.md)
- [Date safety reference](references/date-safety.md)
- [CLI artifacts reference](references/cli-artifacts.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON, shell commands, and concise guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create App-confirmed requests, invoke MCP tools, or write local CLI result/export files when the user provides explicit paths.]

## Skill Version(s):

4.1.0 (source: frontmatter, pyproject dynamic version, runtime version, and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
