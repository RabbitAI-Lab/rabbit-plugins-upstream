## Description:

Governed tool access for AI agents: one Danube API key unlocks organization tools and a catalog of services over MCP or curl, with confirmation before actions that write, send, spend, store credentials, or delete.

This skill is ready for commercial/non-commercial use.

## Publisher:

[preston-thiele](https://clawhub.ai/user/preston-thiele)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use Danube to discover, inspect, and call organization-approved tools through MCP or REST. The skill is intended for agents that need governed access to external services while preserving confirmation gates for sensitive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad Danube tool access can reach services capable of writing, sending, deleting, spending funds, storing credentials, changing workflows, or changing skills.

Mitigation: Require explicit user confirmation with exact tool names and parameters before sensitive actions, and report what ran and what returned.

Risk: Credentials or API keys can be mishandled if the agent invents values, stores secrets without consent, or uses overly broad keys.

Mitigation: Use scoped Danube API keys where possible, prefer dashboard or OAuth connections, and store only credentials the user explicitly provides and confirms.

Risk: Workflow execution, paid tools, wallet funding, and spending limit changes can create cost or duplicate side effects.

Mitigation: Review tool parameters, spending limits, workflow execution status, and user intent before approval; do not retry long-running workflows blindly.

## Reference(s):

- [Danube OpenClaw Guide](https://docs.danubeai.com/sdk/openclaw)
- [Danube Documentation](https://docs.danubeai.com)
- [Danube API Reference](https://docs.danubeai.com/api-reference/introduction)
- [ClawHub Skill Page](https://clawhub.ai/preston-thiele/skills/danube)
- [Danube over plain HTTP](references/rest-api.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command, JSON, YAML, and REST examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires DANUBE_API_KEY and curl; MCP setup is optional.]

## Skill Version(s):

8.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
