## Description: <br>
Consent-gated autonomous trading agent for Robinhood agentic accounts with pluggable signal sources, long-options execution, and user-configured sizing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[traderhc123](https://clawhub.ai/user/traderhc123) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to install, configure, and run an autonomous options-trading agent connected to a user-controlled Robinhood Agentic account. The skill is not investment advice and keeps position sizing as the human user's decision. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent can execute real-money options trades in a connected brokerage account. <br>
Mitigation: Require the human-only consent gate, keep sizing user-chosen, and confirm how to stop the agent before running it. <br>
Risk: The setup command uses an unpinned remote installer. <br>
Mitigation: Audit the GitHub repository and installer contents before installation. <br>
Risk: External signal sources or paid feed credentials can influence trading behavior. <br>
Mitigation: Use only trusted signal sources, start with small user-chosen limits, and review account and feed access before enabling live runs. <br>


## Reference(s): <br>
- [ClawHub listing](https://clawhub.ai/traderhc123/skills/agentic-trader) <br>
- [Project repository](https://github.com/traderhc123/agentic-trader) <br>
- [BOOT.md assistant instructions](https://github.com/traderhc123/agentic-trader/blob/main/BOOT.md) <br>
- [AgentHC day-trade ideas track record](https://api.traderhc.com/api/v1/trading/day-trade-ideas/track-record) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes consent-gated setup and run commands; the human must accept the disclaimer and choose position sizing.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
