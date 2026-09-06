## Description:

Send any transaction on Base with a wallet that holds USDC but no ETH. Pay the gas per operation in USDC over x402 (from $0.03) through an ERC-4337 paymaster; one endpoint for smart-wallet SDKs and plain wallets. No account, no API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[leftychris13](https://clawhub.ai/user/leftychris13)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to prepare Base mainnet transactions for wallets that hold USDC but lack ETH for gas. It guides plain wallets, smart accounts, and ERC-4337 SDKs through paying a per-operation USDC quote and signing the resulting sponsored operation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may sign an unintended payment or transaction if quote details, chain data, paymaster fields, or EIP-7702 authorization are not checked.

Mitigation: Before paying or signing, confirm the quote, USDC amount, payTo address, chain ID, transaction target, value, gas limits, paymaster address, and authorization match the requested operation.

Risk: The skill relies on a third-party Base paymaster and should only be installed when that external service is intended for use.

Mitigation: Install and invoke the skill only for workflows that intentionally use Liquid Agent's Base paymaster.

## Reference(s):

- [Liquid gas sponsor API](https://api.liquidagent.ai/v1/gas)
- [Liquid gas sponsor stats](https://api.liquidagent.ai/v1/gas/stats)
- [Gasless bring-your-own-operation example](https://github.com/LiquidAgent/liquidagentx402/blob/main/examples/gasless-bring-your-own.js)
- [Gasless Node example](https://github.com/LiquidAgent/liquidagentx402/blob/main/examples/gasless.js)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration instructions]

**Output Format:** [Markdown with inline bash code blocks and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl for command examples; users sign wallet operations and x402 payments locally.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
