## Description: <br>
Query and trade on Polymarket prediction markets, including odds, trending markets, order books, trades, orders, and positions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mvanhorn](https://clawhub.ai/user/mvanhorn) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External developers and agent users use this skill to browse Polymarket markets, inspect prices and order books, and manage trades or positions from an agent-assisted terminal workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Trading commands can execute real-money Polymarket transactions using USDC on Polygon. <br>
Mitigation: Review market, side, price, amount, and wallet context before adding --confirm; use preview mode by default. <br>
Risk: Wallet private-key configuration can expose funds if mishandled. <br>
Mitigation: Protect ~/.config/polymarket/config.json, restrict file access, and avoid sharing the configured environment. <br>
Risk: The external Polymarket CLI installer and CLI behavior affect trading operations. <br>
Mitigation: Review the CLI installer and installed binary before use, and keep trading amounts within the user's risk tolerance. <br>


## Reference(s): <br>
- [ClawHub Polymarket skill page](https://clawhub.ai/mvanhorn/skills/polymarket) <br>
- [Polymarket](https://polymarket.com) <br>
- [Polymarket CLI](https://github.com/Polymarket/polymarket-cli) <br>
- [Polymarket Gamma API](https://gamma-api.polymarket.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and terminal text with optional JSON from wrapped CLI commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only market queries work without wallet setup; trading actions require explicit confirmation.] <br>

## Skill Version(s): <br>
1.2.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
