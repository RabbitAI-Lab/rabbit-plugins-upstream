## Description: <br>
Provides pay-per-call x402 API tools for agents to run LLM inference, persistent wallet-scoped memory, uptime monitoring, exact calculations, web analysis, code linting, and live crypto conversion without managing separate API accounts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[webberdesign](https://clawhub.ai/user/webberdesign) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agents use this skill to discover and call paid x402 endpoints for one-off inference, persistent scratchpad storage, monitoring checks, exact calculations, web intelligence, linting, and crypto conversion using a funded wallet. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Paid API calls are tied to a wallet identity and can spend wallet funds. <br>
Mitigation: Use a dedicated low-balance wallet and review live MCP or OpenAPI-discovered tools before allowing automatic paid calls. <br>
Risk: LLM, memory, scraping, and lint endpoints may receive sensitive prompts, stored notes, URLs, or code. <br>
Mitigation: Avoid sending secrets, regulated data, or confidential code, and review payloads before calling the service. <br>
Risk: Wallet-scoped memory can persist across sessions and machines. <br>
Mitigation: Store only non-sensitive state and overwrite or remove scratchpad content when it is no longer needed. <br>


## Reference(s): <br>
- [x402 Agent Tools homepage](https://x402.webbersites.com) <br>
- [OpenAPI catalog](https://api.webbersites.com/openapi.json) <br>
- [x402 discovery document](https://api.webbersites.com/.well-known/x402) <br>
- [Endpoint examples](https://x402.webbersites.com/llms.txt) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, API calls] <br>
**Output Format:** [Markdown guidance with endpoint paths, request examples, and API responses from x402 services.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Endpoint-specific pricing, payload limits, and response caps apply.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
