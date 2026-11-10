## Description:

Use when the user needs a model, data source, or tool API through OpenAny and has authorized that spend. Connect the lite MCP server, then search APIs, inspect the API details and live price, and run it only after user approval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[comunionio](https://clawhub.ai/user/comunionio)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use OpenAny to find model, data, and tool APIs, review their schemas and prices, and invoke a selected API after approving its cost.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Task content sent during API search may disclose confidential or personal information to OpenAny.

Mitigation: Avoid including sensitive details unless you are comfortable sharing them with OpenAny, and provide only the information needed to find an API.

Risk: Running an API may charge the user's balance or cause side effects, and the result or charge state may be unclear.

Mitigation: Review the API details and live price, obtain user approval before running it, and do not retry when execution or charging status is unknown.

## Reference(s):

- [Server-resolved source repository](https://github.com/ComunionIO/openany-skill)
- [OpenAny ClawHub release](https://clawhub.ai/comunionio/skills/openany)
- [OpenAny website](https://openany.si)
- [OpenAny lite MCP endpoint](https://mcp.openany.si/mcp-lite)

## Skill Output:

**Output Type(s):** [Guidance, Configuration]

**Output Format:** [Markdown instructions with a JSON configuration example]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires OPENANY_API_KEY; API invocation can incur charges or have side effects.]

## Skill Version(s):

0.1.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
