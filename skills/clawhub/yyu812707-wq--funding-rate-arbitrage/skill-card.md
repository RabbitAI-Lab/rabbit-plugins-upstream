## Description: <br>
Monitor, evaluate, and operate a funding rate arbitrage strategy for crypto perpetual swaps. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yyu812707-wq](https://clawhub.ai/user/yyu812707-wq) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External traders and workflow operators use this skill to evaluate funding-rate arbitrage opportunities, review hedged perpetual-swap positions, and produce rule-based open, hold, close, or skip guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide live leveraged trading actions without a clear required confirmation before each order change. <br>
Mitigation: Use demo or read-only mode first, use least-privilege exchange API keys with withdrawals disabled, set hard notional and leverage limits, and require explicit confirmation before every live order, cancel, repost, or close action. <br>


## Reference(s): <br>
- [Funding Rate Arbitrage Strategy](references/strategy.md) <br>
- [ClawHub Listing Draft](references/clawhub-listing.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, shell commands] <br>
**Output Format:** [Markdown with structured summaries, rule checks, action plans, and occasional inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should use live exchange-returned values when financial decisions depend on current account or market state.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
