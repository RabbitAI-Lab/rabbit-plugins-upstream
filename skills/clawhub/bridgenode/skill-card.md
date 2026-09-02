## Description:

BridgeNode provides x402 pay-per-request AI inference for agents through an OpenAI-compatible API and MCP server, using Solana USDC payments without API keys or registration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bridgenode](https://clawhub.ai/user/bridgenode)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and AI agents use this skill to call LLM chat completions when they want pay-per-request inference without managing provider API keys. It is suited for OpenAI-compatible clients, MCP clients, and x402-capable SDKs that can sign per-request Solana USDC payments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can cause agents to spend real Solana USDC for inference requests.

Mitigation: Use a dedicated low-balance wallet, check the quoted 402 amount before signing, and configure per-call and daily spending limits where supported.

Risk: Wallet private keys may be exposed if stored in source control or shared environments.

Mitigation: Keep SVM_PRIVATE_KEY in local environment files or secret stores, exclude it from commits, and rotate the wallet if exposure is suspected.

Risk: Unattended autonomous use can accumulate costs through repeated paid calls.

Mitigation: Test payment controls before unattended use and require review or local budget enforcement for autonomous workflows.

Risk: Reasoning models can consume the max_tokens budget and return little or no answer while still charging for the request.

Mitigation: Use adequate max_tokens values, prefer streaming for longer responses, and check live model pricing before each workflow.

## Reference(s):

- [BridgeNode ClawHub Skill](https://clawhub.ai/bridgenode/skills/bridgenode)
- [BridgeNode Website](https://bridgenode.cc)
- [Models and Live Pricing](https://bridgenode.cc/v1/models)
- [OpenAI-Compatible API Base](https://bridgenode.cc/v1)
- [BridgeNode MCP Server](https://bridgenode.cc/mcp)
- [Agent Install Map](https://bridgenode.cc/llms.txt)
- [x402 Documentation](https://docs.x402.org)
- [Python SDK](https://pypi.org/project/bridgenode-llm)
- [TypeScript SDK](https://www.npmjs.com/package/@bridgenode/llm)
- [MCP Wrapper](https://www.npmjs.com/package/@bridgenode/mcp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with API request examples, shell commands, code snippets, and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or guide paid API and MCP calls that return model text, streaming responses, JSON receipts, and settlement metadata.]

## Skill Version(s):

1.0.28 (source: server release metadata; artifact frontmatter reports 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
