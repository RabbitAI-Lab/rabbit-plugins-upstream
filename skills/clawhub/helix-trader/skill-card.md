## Description: <br>
Helix Trader guides an agent through installing and safely operating a self-hosted crypto trading bot with testnet-first configuration, read-only diagnostics, configuration previews, and explicit confirmations before trading actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[frederica123](https://clawhub.ai/user/frederica123) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Use this skill when a user wants help setting up Helix Trader locally, checking environment health, choosing OKX or Binance, selecting a strategy, previewing bot configuration, saving credentials locally, starting the bot after confirmation, checking status, or stopping while preserving or explicitly closing bot-managed positions. <br>

### Deployment Geography for Use: <br>
User-managed local deployment; no geography restriction is stated in the provided evidence. <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles exchange credentials and trading actions, so leaked keys or unreviewed commands could affect a user's trading account. <br>
Mitigation: Keep exchange keys out of chat, use local environment variables or interactive CLI input, report only whether credentials are configured, and require explicit confirmation before saving credentials or starting the bot. <br>
Risk: Setup guidance may expose a local web UI or backend using common default admin credentials. <br>
Mitigation: Change default admin credentials and JWT secrets, bind services to localhost unless network access is deliberate, and review local service exposure before use. <br>
Risk: Trading actions can create or close positions and may cause financial loss. <br>
Mitigation: Use testnet by default, run diagnostics and configuration preview first, require explicit confirmation before live trading, and require separate confirmation before closing positions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/frederica123/skills/helix-trader) <br>
- [Publisher profile](https://clawhub.ai/user/frederica123) <br>
- [Project homepage](https://github.com/trade-upnow/helix-trader) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Conversational setup and operations guidance with command examples, configuration summaries, status explanations, and confirmation prompts.] <br>
**Output Parameters:** [Exchange selection, strategy selection, testnet or live mode, symbol, leverage, position sizing, stop-loss and take-profit values, drawdown limits, order and position notional limits, credential-save confirmation, live-trading confirmation, and stop or close-position confirmations.] <br>
**Other Properties Related to Output:** [The skill should avoid requesting or echoing secrets, prefer read-only checks before state-changing actions, preserve positions by default when stopping, and never promise trading returns.] <br>

## Skill Version(s): <br>
1.0.0 <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
