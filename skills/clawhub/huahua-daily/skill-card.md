## Description:

HuaHuaDailyMCP lets agents use HuahuaDaily MCP to query authorized portfolio, transaction, fund, market, backtest, screenshot, community, and App-confirmed trade or import workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[baiye1997](https://clawhub.ai/user/baiye1997)

### License/Terms of Use:

MIT-0

## Use Case:

External HuahuaDaily users and their agents use this skill to inspect authorized portfolio data, market data, transactions, strategy backtests, quant snapshots, screenshots, and community workflows. The skill can prepare trade or import requests for App confirmation and can perform selected community actions after explicit user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation guidance can run unpinned remote code while the skill uses a token that can access sensitive portfolio data.

Mitigation: Install only if the publisher and repository are trusted; prefer a pinned tag or commit and a reviewed lockfile.

Risk: The Agent Token can authorize access to portfolio, transaction, cost, return, and screenshot-derived data.

Mitigation: Use a dedicated HuahuaDaily Agent Token, keep it scoped to the intended agent, and revoke it when it is no longer needed.

Risk: The default full profile exposes more tools than many daily workflows require.

Mitigation: Use the core profile when possible to reduce the active MCP tool surface.

Risk: Community authorization, revocation, following, report saving, and quant snapshot writes can directly change backend state.

Mitigation: Require explicit user confirmation before allowing the agent to invoke direct-write tools.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/baiye1997/skills/huahua-daily)
- [README.md](artifact/README.md)
- [SKILL.md](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with MCP tool calls, JSON tool arguments, shell commands, and configuration snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a HuahuaDaily Agent Token; trade and import requests require App confirmation, while selected community actions are direct backend writes.]

## Skill Version(s):

4.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
