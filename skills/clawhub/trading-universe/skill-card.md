## Description: <br>
Use for deterministic ICT market scans, validated intraday order-plan tickets, structure reads, macro bias boards, the local Trading Universe dashboard, and automatic candle-replayed trade tracking. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[illimitedenterprise](https://clawhub.ai/user/illimitedenterprise) <br>

### License/Terms of Use: <br>
MIT No Attribution (MIT-0) <br>


## Use Case: <br>
External traders and agent users use this skill to generate deterministic trading-analysis plans, market-structure reads, macro bias summaries, local dashboard views, alerts, and trade-lifecycle tracking for covered FX, metals, and index instruments. The skill produces order plans and educational analysis only; it does not place trades, connect to brokers, or provide position-sizing or leverage advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may mistake order-plan output for trade execution or investment advice. <br>
Mitigation: Keep the documented boundary clear: the skill produces plans and educational market analysis only, never places trades, never connects to brokers, and should end user-facing trading outputs with the not-financial-advice disclaimer. <br>
Risk: The local dashboard writes private runtime data, including trade logs, alerts, settings, backups, and optionally a saved reasoning-provider key. <br>
Mitigation: Use the default private local data directory intentionally, avoid saving API keys unless needed, and review the data directory before sharing, backing up, or moving the environment. <br>
Risk: Market scans poll public market and news sources and optional reasoning integrations may send selected ticket or fundamentals data to an external provider. <br>
Mitigation: Review provider terms before enabling NVIDIA NIM, OpenAI, OpenRouter, Claude, or Codex integrations, and enable only the integrations needed for the workflow. <br>
Risk: Background alerts and notification delivery can continue polling or sending updates when auxiliary scripts are run. <br>
Mitigation: Run watcher and alert-sender scripts only when background alerts or Telegram/OpenClaw notification delivery are desired. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/illimitedenterprise/skills/trading-universe) <br>
- [README](README.md) <br>
- [ICT intraday playbook](references/playbook.md) <br>
- [Trading Universe Dashboard reference](references/dashboard.md) <br>
- [Asset map, watchlist, queries, sources](references/asset-map.md) <br>
- [Wyckoff engine reference](references/wyckoff.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Chat-friendly Markdown cards, JSON from CLI scripts, shell commands, local configuration, and dashboard files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces financial-analysis plans and local dashboard state; order execution remains outside the skill.] <br>

## Skill Version(s): <br>
1.8.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
