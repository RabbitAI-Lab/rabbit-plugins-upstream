## Description: <br>
TradingBot installs, updates, builds, starts, and health-checks the paoosi/tradingbot local grid trading bot while keeping first-run use in mock or demo mode. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[frederica123](https://clawhub.ai/user/frederica123) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to install and run a local TradingBot instance on macOS or Linux, verify its health, update it, and troubleshoot it without configuring live trading by default. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Building and running third-party TradingBot code locally can expose the user to upstream software and trading-domain risk. <br>
Mitigation: Install only when the user trusts the upstream project, report the exact commit, and keep first-run use in mock or demo mode. <br>
Risk: Live exchange credentials or application secrets could be exposed if they are requested, printed, logged, or captured in screenshots. <br>
Mitigation: Do not ask for or display exchange API keys, API secrets, JWT secrets, or APP_SECRET_KEY values; keep generated local secrets in the user's private configuration file. <br>
Risk: The local service listens on a port and could be unsafe if exposed to the public internet. <br>
Mitigation: Use the local URL only, keep the system firewall enabled, and do not configure public forwarding or firewall openings for the service. <br>


## Reference(s): <br>
- [TradingBot upstream repository](https://github.com/paoosi/tradingbot) <br>
- [ClawHub TradingBot skill page](https://clawhub.ai/frederica123/skills/tradingbot) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, local configuration notes, and status summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands are expected to run locally; secrets should not be requested, printed, logged, or included in screenshots.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
