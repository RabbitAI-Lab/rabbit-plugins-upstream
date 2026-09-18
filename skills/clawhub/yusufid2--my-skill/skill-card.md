## Description:

AI trading bot untuk BTC, ETH, dan SOL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yusufid2](https://clawhub.ai/user/yusufid2)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to check BTC, ETH, and SOL prices, generate simple trading signals, and run paper-trade simulations from a Node.js CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package has a suspicious security verdict due to inconsistent metadata and an unrelated shell-based chat runner with command-injection risk.

Mitigation: Review the package before installing and do not run artifact/index. with untrusted input.

Risk: The included run.sh script starts an endless local paper-trading loop.

Mitigation: Use run.sh only when continuous local paper-trading is intended and monitor or stop the process explicitly.

Risk: Trading signals and paper-trade results can be incorrect or misleading.

Mitigation: Treat outputs as simulation guidance and validate results against independent market data before acting on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yusufid2/skills/my-skill)
- [Binance ticker price API](https://api.binance.com/api/v3/ticker/price?symbol=${symbol}USDT)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration]

**Output Format:** [Markdown guidance with CLI command examples and JSON-like CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads and writes local JSON state files and may call the Binance ticker API.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata; artifact frontmatter 1.0.0 and package.json 1.1.0 differ)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
