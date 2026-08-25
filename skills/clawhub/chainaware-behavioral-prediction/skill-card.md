## Description:

Connects agents to ChainAware's remote MCP service for blockchain wallet, token, contract, liquidity-pool, and AI-agent risk, behavior, trust, and holder-quality analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chainaware](https://clawhub.ai/user/chainaware)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use this skill to screen blockchain wallets, smart contracts, liquidity pools, tokens, airdrop lists, borrowers, and registered AI agents for fraud, rug-pull, AML, credit, behavioral, and trust signals through ChainAware's MCP endpoint.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends blockchain addresses, token or contract identifiers, batch wallet lists, job handles, agent IDs, and an API key or x402 payment flow to ChainAware's remote MCP service.

Mitigation: Use a restricted or dedicated API key where possible, avoid putting keys in URLs unless required by the host, and review ChainAware's privacy policy before use.

Risk: Fraud, AML, credit, lending, and account-blocking decisions can be materially harmful if based only on model scores.

Mitigation: Use the scores as decision support and require human review, policy checks, and independent evidence for regulated or high-impact decisions.

Risk: Batch results depend on retaining both job_id and signature and waiting until the job is completed or partial.

Mitigation: Store both returned values, poll job status first, and retrieve results only after the service reports completed or partial status.

## Reference(s):

- [ChainAware Behavioral Prediction MCP](https://github.com/ChainAware/behavioral-prediction-mcp)
- [ChainAware MCP Endpoint](https://prediction.mcp.chainaware.ai/sse)
- [ChainAware Privacy Policy](https://chainaware.ai/privacy)
- [ChainAware Fraud Detection Backtesting](https://chainaware.ai/scam-db)
- [ChainAware Rug Pull Verification](https://chainaware.ai/resources/rugpull-verification)
- [ChainAware Examples](https://github.com/ChainAware/examples)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and plain-text guidance with MCP tool-call inputs and summarized risk results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include wallet, contract, token, batch-job, network, and agent trust score fields returned by ChainAware's remote service.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
