## Description:

Research crypto tokens, tracked traders, wallets, and smart-money activity using StalkChain's connected MCP tools. Use for StalkChain setup or requests about on-chain holdings, trader PnL, token holders, buy/sell flow, and token risk. This skill does not place trades or manage funds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[assistant-design](https://clawhub.ai/user/assistant-design)

### License/Terms of Use:

MIT-0

## Use Case:

External users can use the skill to set up StalkChain and research on-chain token, wallet, and tracked-trader activity. It helps answer questions about holdings, PnL, flows, and risk signals without placing trades or managing funds.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting authorizes OAuth access to the hosted StalkChain service, which receives the tool names and arguments sent to it.

Mitigation: Connect only if you trust the service and are comfortable with the OAuth approval; never provide a seed phrase or wallet private key.

Risk: Research lookups can spend StalkChain credits.

Mitigation: Check current pricing and returned usage information, and limit lookups to what is needed for the question.

## Reference(s):

- [StalkChain documentation](https://stalkchain.com/docs)
- [OpenClaw setup guide](https://stalkchain.com/ai/openclaw)
- [StalkChain pricing](https://stalkchain.com/pricing)
- [StalkChain machine-readable guide](https://data.stalkchain.com/llms.txt)
- [StalkChain plugin repository](https://github.com/StalkC/stalkchain-plugin)
- [StalkChain support](https://stalkchain.com/support)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Text]

**Output Format:** [Markdown or plain text, with setup commands when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Research summaries should identify the chain, address or handle, time window, and data freshness when available.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
