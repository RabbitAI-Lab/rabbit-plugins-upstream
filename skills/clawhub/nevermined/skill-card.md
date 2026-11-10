## Description:

Guides AI agent builders and developers in managing Nevermined payments and integrating x402 payment flows into TypeScript and Python services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nevermined-io](https://clawhub.ai/user/nevermined-io)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to buy or offer paid AI services, manage payment plans, delegations, credits, and revenue, and add x402 payment protection to application endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Autonomous payment guidance may allow an agent to spend delegated funds based on an endpoint's payment offer without checking it against an approved purchase policy.

Mitigation: Before creating or sending a payment token, require approval or a policy check for the endpoint, merchant, plan, and maximum charge, and set delegation limits.

Risk: Some workflows may send queries to OpenAI, which can expose query content.

Mitigation: Confirm this fits your privacy requirements and keep sensitive information out of queries unless its use is approved.

## Reference(s):

- [Nevermined skill documentation](https://nevermined.ai/docs/development-guide/build-using-nvm-skill)
- [Get a Nevermined API key](https://nevermined.ai/docs/agents-guide/get-api-key)
- [Card delegation guide](https://nevermined.ai/docs/solutions/card-delegation)
- [x402 protocol integration](artifact/references/x402-protocol.md)
- [Autonomous payment operations](artifact/references/autonomous-operations.md)
- [MCP server paywall integration](artifact/references/mcp-paywall.md)
- [Nevermined app and account setup](https://nevermined.app)

## Skill Output:

**Output Type(s):** [Guidance, API calls, Code, Shell commands, Configuration]

**Output Format:** [Markdown with REST examples, JSON payloads, TypeScript and Python snippets, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and setup instructions for Nevermined payment workflows and x402 integrations.]

## Skill Version(s):

1.0.14 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
