## Description:

Sentinel Transaction Safety lets autonomous agents submit unsigned Base transaction payloads to sentinel-agent.dev for a paid pre-execution SAFE/UNSAFE/UNKNOWN verdict, score, and signed receipt before signing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[teodorofodocrispin-cmyk](https://clawhub.ai/user/teodorofodocrispin-cmyk)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and autonomous agent operators use this skill to check Base transactions before signing, especially when they need a paid pre-flight risk verdict, score, and independently verifiable receipt.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unsigned transaction payloads and potentially sensitive calldata are sent to sentinel-agent.dev for evaluation.

Mitigation: Use the skill only when third-party transmission is acceptable; avoid air-gapped workflows and transactions whose calldata must remain local.

Risk: Autonomous wallets may sign x402 USDC payment authorizations for each guard call.

Mitigation: Set wallet spending controls and have the agent pay only the exact amount quoted in the 402 challenge.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/teodorofodocrispin-cmyk/skills/sentinel-public)
- [SENTINEL Guard Endpoint](https://sentinel-agent.dev/v1/guard)
- [Health Endpoint](https://sentinel-agent.dev/health)
- [Pricing](https://sentinel-agent.dev/pricing)
- [LLM-Readable Documentation](https://sentinel-agent.dev/llms.txt)
- [MCP Server](https://sentinel-agent.dev/mcp)
- [Homepage](https://github.com/teodorofodocrispin-cmyk/sentinel-public)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Remote service returns JSON verdicts, risk reasons, scores, transaction digests, and ed25519-signed receipts after x402 payment.]

## Skill Version(s):

1.1.0 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
