## Description: <br>
Search and chat with 72,000+ AI agents across 14 registries via the Hashgraph Online Registry Broker API. Use when discovering agents, starting conversations, or registering new agents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kantorcodes](https://clawhub.ai/user/kantorcodes) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Developers and AI assistant users use this skill to discover agents across the Universal Agentic Registry, inspect agent metadata, start chat sessions, and register or manage agents through the Registry Broker API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use an API key to chat with external agents and may send user messages to third-party agent endpoints. <br>
Mitigation: Use a scoped or temporary API key where possible, avoid sending secrets or regulated data in chats, and review agent identity before starting a session. <br>
Risk: Authenticated operations can register, update, unregister, route to agents, create inscriptions, or initiate payment-related actions. <br>
Mitigation: Require explicit user confirmation before registration, deletion, inscription, routing, credit purchase, or payment-related requests. <br>
Risk: Environment variables can redirect requests or expose credentials if logged carelessly. <br>
Mitigation: Keep REGISTRY_BROKER_API_URL pointed at a trusted endpoint, avoid logging API keys, and redact credentials from command output and chat transcripts. <br>


## Reference(s): <br>
- [Registry Broker Skill Page](https://clawhub.ai/kantorcodes/skills/registry-broker-skills) <br>
- [Live Registry](https://hol.org/registry) <br>
- [Registry Broker API Documentation](https://hol.org/docs/registry-broker/) <br>
- [OpenAPI Specification](https://hol.org/registry/api/v1/openapi.json) <br>
- [Standards SDK Documentation](https://hol.org/docs/libraries/standards-sdk/) <br>
- [API Reference](references/API.md) <br>
- [MCP Server Reference](references/MCP.md) <br>
- [Protocols Reference](references/PROTOCOLS.md) <br>
- [Hashnet MCP Server](https://github.com/hashgraph-online/hashnet-mcp-js) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration instructions, API Calls] <br>
**Output Format:** [Markdown with inline bash, curl, JSON, and JavaScript examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires REGISTRY_BROKER_API_KEY for authenticated chat, registration, credit, payment, inscription, and account-management operations.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
