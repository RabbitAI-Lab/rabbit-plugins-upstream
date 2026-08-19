## Description:

BridgeNode gives agents OpenAI-compatible chat completions and MCP access without API keys, paid per request with Solana USDC through x402.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bridgenode](https://clawhub.ai/user/bridgenode)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External agents and developers use BridgeNode when they need pay-per-request LLM inference without maintaining provider API keys or subscriptions. The skill is most relevant for OpenAI-compatible or MCP-capable agents that can approve and sign x402 Solana USDC payments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests can spend real Solana USDC through x402 payments.

Mitigation: Use a dedicated low-balance wallet, check the quoted 402 amount before signing, and configure per-call or daily spend limits where the client supports them.

Risk: Wallet credentials such as SVM_PRIVATE_KEY can expose funds if committed, logged, or shared.

Mitigation: Keep private keys out of repositories and logs, store them in local secret management, and rotate the wallet if exposure is suspected.

Risk: The exact pricing scheme charges against the requested max_tokens budget, so over-large requests can cost more than intended.

Mitigation: Fetch live prices from the models endpoint before use and set max_tokens conservatively for each request.

## Reference(s):

- [BridgeNode homepage](https://bridgenode.cc)
- [BridgeNode ClawHub skill](https://clawhub.ai/bridgenode/skills/bridgenode)
- [Models and live pricing](https://bridgenode.cc/v1/models)
- [OpenAI-compatible API base](https://bridgenode.cc/v1)
- [BridgeNode MCP endpoint](https://bridgenode.cc/mcp)
- [Agent install map](https://bridgenode.cc/llms.txt)
- [x402 documentation](https://docs.x402.org)
- [BridgeNode source repository listed in metadata](https://github.com/applefanaimail-blip/bridgenode-skill)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with API request examples, shell commands, and Python, TypeScript, curl, and MCP usage snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill teaches agents how to call paid inference endpoints and MCP tools; outputs can lead to real USDC payments when followed by a payment-capable client.]

## Skill Version(s):

1.0.21 (source: server release metadata; artifact frontmatter reports 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
