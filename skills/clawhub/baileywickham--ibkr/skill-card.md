## Description: <br>
Trade and research options on Interactive Brokers via a local CLI (chains, quotes, Greeks, single-leg and vertical orders). Use when the user asks about option chains, option quotes, or wants to place/cancel option orders on IBKR. Requires IB Gateway running locally. Paper account is the default; live needs --live. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[baileywickham](https://clawhub.ai/user/baileywickham) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to research IBKR option chains, quotes, positions, and execute user-approved paper or live orders through a local IBKR CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Live mode can place real financial orders. <br>
Mitigation: Use paper mode first, review every preview, and require fresh explicit user approval before executing each live trade. <br>
Risk: Limit prices may be based on delayed market data. <br>
Mitigation: Surface delayed-data warnings, prefer realtime subscriptions for live trades, and only allow delayed live pricing when the user explicitly understands the stale quote risk. <br>
Risk: Incorrect or duplicate closing orders can change the account's exposure. <br>
Mitigation: Check open orders and positions before closing, use limit orders only, and rely on the preview-confirm-execute flow before submitting orders. <br>
Risk: The skill could be mistaken for personalized investment advice. <br>
Mitigation: Limit assistance to research, data presentation, and execution of the user's decisions. <br>
Risk: IB Gateway credentials and account access are sensitive. <br>
Mitigation: Keep IB Gateway login under the user's control and do not attempt to enter credentials for the user. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/baileywickham/skills/ibkr) <br>
- [IBKR CLI repository](https://github.com/baileywickham/ibkr) <br>
- [uv](https://github.com/astral-sh/uv) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON command output summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include order previews, account status summaries, quotes, positions, and explicit approval prompts before live execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
