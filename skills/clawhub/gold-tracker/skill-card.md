## Description: <br>
Gold Tracker helps AI agents fetch and validate gold prices and USD/CNY exchange rates, manage alerts and archives, and generate market briefings from agent-authored analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jeromeex](https://clawhub.ai/user/jeromeex) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to let an AI agent maintain a lightweight gold price tracking workflow: fetching price and FX data, recording market analysis, detecting price moves, and producing briefings for review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill recommends persistent cron jobs that run unattended. <br>
Mitigation: Require explicit user opt-in before installing cron entries, show the exact entries first, and keep uninstall commands available. <br>
Risk: Maintenance commands can mutate or delete local alert and archive files. <br>
Mitigation: Run cleanup and archive commands only after reviewing retention settings and keeping backups of important logs. <br>
Risk: Market data and exchange-rate fetches depend on external services and may be unavailable or stale. <br>
Mitigation: Use the skill's validation, cache, and state checks, and label analysis clearly when data falls back to cached or last-known values. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jeromeex/skills/gold-tracker) <br>
- [Publisher profile](https://clawhub.ai/user/jeromeex) <br>
- [Goldpricez data source](https://goldpricez.com) <br>
- [USD exchange-rate data source](https://open.er-api.com/v6/latest/USD) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON, YAML, cron, and shell command snippets; bundled scripts emit JSON, Markdown summaries, and console text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates or updates local state, logs, alerts, archives, and cache files during use.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata; artifact skill.yaml says 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
