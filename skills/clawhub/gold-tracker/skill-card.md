## Description: <br>
Gold Tracker helps agents fetch gold prices and USD/CNY rates, validate and log source-backed market analysis, detect price breakouts, archive records, and generate concise briefings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jeromeex](https://clawhub.ai/user/jeromeex) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and finance-focused agent operators use this skill to gather current gold market data, enforce source-backed market reasoning, track price movements, and produce briefings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent scheduled jobs may continue fetching data and writing local files after installation. <br>
Mitigation: Review the crontab entries before enabling them, confirm the skill directory is not writable by untrusted parties, and remove the cron entries when the skill is no longer needed. <br>
Risk: Financial market briefings can be misleading if sources are stale, missing, or invented. <br>
Mitigation: Require recorded web_fetch URLs, at least two independent source domains, and successful validate.py and check_analysis.py runs before accepting an analysis. <br>
Risk: External price and exchange-rate sources can fail or return out-of-range data. <br>
Mitigation: Use the built-in range validation and cache or state fallback behavior, and disclose stale data whenever current fetches fail. <br>


## Reference(s): <br>
- [ClawHub Gold Tracker release](https://clawhub.ai/jeromeex/skills/gold-tracker) <br>
- [Publisher profile](https://clawhub.ai/user/jeromeex) <br>
- [Gold price data source](https://goldpricez.com) <br>
- [USD/CNY exchange-rate source](https://open.er-api.com/v6/latest/USD) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown briefings, YAML analysis logs, JSON state and alert files, and shell command sequences] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses local files for state, cache, logs, alerts, and archives; price data is cached for 5 minutes.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence; artifact/skill.yaml reports 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
