## Description:

Helps an agent plan and orchestrate Uniswap V2/V3/V4 liquidity actions, including adding liquidity, removing liquidity, and collecting fees.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use this skill to guide Uniswap liquidity workflows, including pool selection, token approvals, deposits, withdrawals, and fee collection. Because these are value-bearing blockchain actions, users should independently verify all transaction details before signing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill covers value-bearing Uniswap liquidity operations, and the security summary says its instructions are too broad and mismatched for those operations.

Mitigation: Use only with a wallet setup that requires explicit signing, and verify every token address, pool, position ID, amount, network, gas estimate, and slippage setting before approving any transaction.

Risk: The release requests broad read, execute, and write capabilities while the security guidance warns against broad command or file access.

Mitigation: Run in a restricted workspace and deny broad command or file access unless the publisher narrows the scope and the requested operation is necessary for the liquidity task.

Risk: The artifact contains unrelated template and marketing content that can reduce confidence in the stated behavior.

Mitigation: Review the skill instructions before installation and rely only on sections that directly support the intended Uniswap liquidity workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/manage-liquidity)

## Skill Output:

**Output Type(s):** [guidance, text, shell commands, configuration]

**Output Format:** [Markdown guidance with JSON result examples and shell snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include transaction workflow recommendations, execution logs, status summaries, and configuration checks.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
