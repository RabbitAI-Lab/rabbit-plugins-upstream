## Description:

Look up ERC-8004 agents in the on-chain identity index and read their Cybercentry verification results before trusting them.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cybercentry](https://clawhub.ai/user/cybercentry)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, security reviewers, and agent operators use this skill to check public ERC-8004 agent identity records and Cybercentry verification results before deciding whether to interact with an agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Some MCP lookups cost USDC per call.

Mitigation: Review x402/payment settings before use, prefer the free listing and index-stat tools first, and confirm before requesting the higher-cost full report.

Risk: Unverified agents can be misread as dangerous if numeric risk scores are interpreted without the risk level.

Mitigation: Judge agent status by risk_level and report which verification checks have actually run.

Risk: API-key use can draw from a subscription quota.

Mitigation: Provide an API key only when the user intends to use subscription quota instead of per-call x402 payment.

## Reference(s):

- [ERC-8126: AI Agent Verification](https://eips.ethereum.org/EIPS/eip-8126)
- [ERC-8004: Trustless Agents](https://eips.ethereum.org/EIPS/eip-8004)
- [ERC-8126scan MCP endpoint](https://erc8126scan.ai/api/mcp)
- [ERC-8126scan ClawHub page](https://clawhub.ai/cybercentry/skills/erc-8126-scan)
- [Cybercentry ClawHub profile](https://clawhub.ai/user/cybercentry)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text]

**Output Format:** [Markdown with inline shell commands and MCP usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide read-only MCP lookups that disclose per-call USDC pricing before paid requests.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
