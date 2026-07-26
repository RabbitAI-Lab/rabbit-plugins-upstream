## Description: <br>
Operate the Moltrade trading bot for configuration, backtesting, test-mode runs, Nostr signal broadcast, exchange adapters, and strategy integration in OpenClaw. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ai-chen2050](https://clawhub.ai/user/ai-chen2050) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and trading operators use this skill to configure and run Moltrade workflows, including backtests, test-mode trading, live trading after explicit approval, exchange adapter setup, and Nostr or Binance Square signal publishing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can assist with workflows that place real trades or swaps. <br>
Mitigation: Start with paper, dry-run, backtest, or testnet workflows; require explicit user approval before live trading and review keys, risk limits, symbols, and order details before execution. <br>
Risk: Trading, wallet, Nostr, Binance, Square, and exchange credentials are sensitive. <br>
Mitigation: Use least-privilege API keys, disable withdrawal permissions where possible, store secrets outside chat and repository files, and mask credentials whenever they are displayed. <br>
Risk: The skill can help publish public trading signals or social posts. <br>
Mitigation: Review and approve each Nostr or Binance Square post before publishing, and use the documented pure-text and rate-limit constraints for Square posting. <br>


## Reference(s): <br>
- [Moltrade homepage](https://github.com/hetu-project/moltrade.git) <br>
- [ClawHub release page](https://clawhub.ai/ai-chen2050/skills/moltrade) <br>
- [Binance Spot Skill](binance/spot/SKILL.md) <br>
- [Binance Spot Authentication](binance/spot/references/authentication.md) <br>
- [Binance Square Post Skill](binance/square-post/SKILL.md) <br>
- [Moltrade website](https://www.moltrade.ai/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, API calls] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON configuration snippets, code-oriented instructions, and API call examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include redacted credential handling guidance, backtest metrics, planned configuration diffs, command sequences, and public post URLs.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
