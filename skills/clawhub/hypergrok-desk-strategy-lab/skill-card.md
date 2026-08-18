## Description:

HyperGrok Desk Strategy Lab helps an agent turn a user's trading idea into explicit rules, honest Hyperliquid backtests, documented research artifacts, and testnet paper-trade proposals without executing real orders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galleonlabs](https://clawhub.ai/user/galleonlabs)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to structure a trading idea into rules, collect Hyperliquid data, run readable backtests with documented caveats, and compare testnet paper trades against the backtest before risking money.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Backtest or paper-trade output may be mistaken for trading advice.

Mitigation: Treat outputs as research and paper-trading support only; review generated backtest code, data requests, assumptions, costs, drawdowns, and out-of-sample results before relying on them.

Risk: Real account credentials or live execution could be introduced outside the intended workflow.

Mitigation: Keep real account credentials out of the workflow unless separately required by trusted tools, use the testnet paper-trading path, and do not allow unattended execution or real order submission.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/galleonlabs/skills/hypergrok-desk-strategy-lab)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with code and shell-command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local research artifacts such as RULES.md, data.md, backtest.py, run notes, and POSTMORTEM.md when the agent follows the workflow.]

## Skill Version(s):

1.0.0 (source: server evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
