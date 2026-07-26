## Description: <br>
Mirror congressional stock trades with automated broker execution and risk management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mainfraame](https://clawhub.ai/user/mainfraame) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External developers and trading automation users use this skill to configure and operate an agent workflow that monitors congressional trade disclosures, creates trading recommendations, and can place scaled E*TRADE orders with risk controls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Live brokerage automation may place real orders and cause financial loss. <br>
Mitigation: Use sandbox or paper trading first, keep live order execution disabled until strategy settings and risk limits are reviewed, and start with very small trade sizing if enabling production use. <br>
Risk: Broker and Telegram credentials may be stored locally in plaintext configuration or token files. <br>
Mitigation: Keep credentials outside the repository where possible, restrict file permissions, avoid committing generated secret files, and rotate any credentials that may have been exposed. <br>
Risk: Persistent cron or systemd scheduling can continue running after setup. <br>
Mitigation: Confirm installed scheduled jobs, document disable steps before enabling automation, and monitor logs and notifications after every scheduled run. <br>
Risk: External congressional disclosure data may be delayed, unavailable, or parsed incorrectly. <br>
Mitigation: Verify source filings and generated recommendations before enabling automated trade execution. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/mainfraame/skills/etrade-pelosi-bot) <br>
- [Congressional Data System Documentation](docs/CONGRESSIONAL_DATA.md) <br>
- [Senate eFD Search](https://efdsearch.senate.gov/search/) <br>
- [House Financial Disclosure Reports](https://disclosures-clerk.house.gov/FinancialDisclosure) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON configuration, and Python code references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can create local configuration files, scheduled jobs, logs, SQLite state, and brokerage API calls when executed.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
