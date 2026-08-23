## Description:

Governed tool access for agents through one Danube API key, with discovery, inspection, and execution over MCP or curl and explicit confirmation before actions that write, send, spend, store credentials, or delete.

This skill is ready for commercial/non-commercial use.

## Publisher:

[preston-thiele](https://clawhub.ai/user/preston-thiele)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to let an agent search Danube's visible tool catalog, inspect schemas, configure access, and execute selected tools with user confirmation for sensitive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Danube API key can provide access to organization tools and connected services.

Mitigation: Install only when the publisher and Danube account are trusted, protect DANUBE_API_KEY, and review requested tool calls before execution.

Risk: Some available tools can write, send, spend funds, store credentials, change limits, or delete data.

Mitigation: Require explicit user confirmation with the exact tool and parameters before sensitive or batch execution.

Risk: Tool calls can disclose unnecessary personal or business data to connected services.

Mitigation: Pass only the parameters needed for the requested task and avoid forwarding unrelated data.

Risk: Stale tool identifiers, missing credentials, rate limits, or spending caps can cause failed or unintended calls.

Mitigation: Search and inspect tool schemas before execution, follow auth-required and rate-limit guidance, and do not raise limits or fund wallets unless the user explicitly asks.

## Reference(s):

- [Danube OpenClaw Guide](https://docs.danubeai.com/sdk/openclaw)
- [Danube Docs](https://docs.danubeai.com)
- [REST API Reference](references/rest-api.md)
- [Troubleshooting](references/troubleshooting.md)
- [ClawHub Skill Page](https://clawhub.ai/preston-thiele/skills/danube)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, API Calls]

**Output Format:** [Markdown with inline bash, JSON, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DANUBE_API_KEY and curl; native MCP setup is optional.]

## Skill Version(s):

8.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
