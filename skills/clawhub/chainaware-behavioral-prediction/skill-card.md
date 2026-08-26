## Description:

Connects agents to ChainAware's remote MCP service for wallet fraud screening, behavioral analysis, rug-pull forecasting, credit scoring, token ranking, token auditing, and AI-agent trust checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chainaware](https://clawhub.ai/user/chainaware)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, DeFi operators, compliance reviewers, and agent builders use this skill to send wallet, contract, token, batch, job, or agent identifiers to ChainAware for remote scoring and to receive risk, behavior, trust, or ranking guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends wallet, contract, token, batch, job, and agent identifiers to ChainAware for remote scoring.

Mitigation: Install only when that data transfer is intended; review ChainAware's privacy policy and document consent or regulatory requirements for your use case.

Risk: The security review flags the skill for wallet profiling in high-impact contexts such as lending, onboarding, eligibility, AML, and personalized treatment decisions.

Mitigation: Require human review, local policy checks, and compliance approval before using outputs for consequential decisions.

Risk: API keys and job_id/signature values can grant access to paid calls or batch results if exposed.

Mitigation: Use restricted API keys, prefer header-based authentication where supported, avoid URL-based keys when possible, and protect job_id/signature values as sensitive credentials.

## Reference(s):

- [ChainAware Behavioral Prediction MCP](https://github.com/ChainAware/behavioral-prediction-mcp)
- [ChainAware MCP Server Endpoint](https://prediction.mcp.chainaware.ai/sse)
- [ChainAware Privacy Policy](https://chainaware.ai/privacy)
- [Fraud Detection Accuracy Reference](https://chainaware.ai/scam-db)
- [Rug Pull Detection Verification](https://chainaware.ai/resources/rugpull-verification)
- [ClawHub Skill Page](https://clawhub.ai/chainaware/skills/chainaware-behavioral-prediction)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or text guidance with MCP tool calls, configuration snippets, shell commands, and JSON-like result interpretation.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include risk labels, scores, job identifiers, signatures, network-specific caveats, and human-review recommendations.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
