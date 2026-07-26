## Description: <br>
Blave Quant Skill gives agents a documentation-based reference for Blave market alpha data, Taiwan market data, CME/ICE futures OHLCV, and spot, futures, margin, funding, and account workflows across supported exchanges. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[blave-wei](https://clawhub.ai/user/blave-wei) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and trading-focused agent users use this skill to fetch market data, build analysis, and prepare exchange API calls for supported venues. It is also used to guide order, funding, and transfer workflows that require explicit user confirmation before any write action. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: High-authority exchange API credentials can place trades, manage positions, submit funding actions, or transfer funds when write permissions are enabled. <br>
Mitigation: Use dedicated least-privilege API keys, disable withdrawals, enable IP allowlists, and only add exchange credentials for venues the user intends to use. <br>
Risk: Marketplace strategy downloads can result in local Python code execution near trading credentials. <br>
Mitigation: Review and security scan downloaded strategy code, isolate it in a sandbox, and do not run it on the host or near live trading credentials without approval. <br>
Risk: Trading or funding actions can cause financial loss if executed unintentionally or with incorrect parameters. <br>
Mitigation: Require the user to reply exactly CONFIRM for each write action, present a one-screen action summary first, and verify the result after execution. <br>


## Reference(s): <br>
- [Blave Quant Skill on ClawHub](https://clawhub.ai/blave-wei/skills/blave-quant-skill) <br>
- [Blave homepage](https://blave.org) <br>
- [Blave API reference](artifact/references/blave-api.md) <br>
- [Blave indicator guide](artifact/references/blave-indicator-guide.md) <br>
- [TradingView stream reference](artifact/references/tradingview-stream.md) <br>
- [Marketplace reference](artifact/references/marketplace.md) <br>
- [Gate.io reference](artifact/references/gateio-skill.md) <br>
- [Binance reference](artifact/references/binance-skill.md) <br>
- [BitMart futures reference](artifact/references/bitmart-futures-skill.md) <br>
- [TWSE/TPEX reference](artifact/references/twse-skill.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with API request examples, configuration snippets, and optional code or shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read operations can be described directly; write operations require one explicit CONFIRM per action.] <br>

## Skill Version(s): <br>
1.15.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
