## Description: <br>
Decentralized AI inference via Bittensor SN64 (43+ chat models) and SN19 (image gen) plus embeddings - OpenAI-compatible, paid in USDC on Base/Solana via Spraay x402. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[plagtech](https://clawhub.ai/user/plagtech) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external agents use this skill when they explicitly need decentralized Bittensor inference for chat completions, image generation, model listing, or embeddings through an OpenAI-compatible gateway. It is suited to Web3, crypto, RAG, content-generation, and A/B testing workflows where decentralized infrastructure is part of the requirement. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, documents, and image requests are sent to the Spraay gateway and routed to Bittensor miners. <br>
Mitigation: Do not send sensitive or proprietary content unless external processing by the gateway and miners is acceptable. <br>
Risk: Requests may spend real USDC through x402 micropayments. <br>
Mitigation: Use a dedicated low-balance wallet and review expected per-call costs before running workflows. <br>
Risk: Decentralized miner routing can produce variable quality, latency, and model availability. <br>
Mitigation: List available models first and validate outputs before using them in production decisions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/plagtech/skills/bittensor-x402) <br>
- [Spraay Gateway](https://gateway.spraay.app) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Text, Markdown, Code, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and OpenAI-compatible JSON request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses may include model lists, chat text, generated image URLs, or embedding vectors; requests require bash and curl and may spend USDC per call.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
