## Description: <br>
The trust layer for OpenClaw that verifies AI-written code, tool calls, plans, documents, and research answers using deterministic reality gates and model review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[verificate-dev](https://clawhub.ai/user/verificate-dev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to validate AI-generated code, tool calls, plans, documents, and research answers before treating them as finished. It can also provide advisory code analysis and gated code generation through the hosted Verificate MCP service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends code, documents, or plans selected for validation to Verificate's hosted MCP service for analysis. <br>
Mitigation: Use it only for material that may be shared with Verificate, and review the service privacy terms before routing sensitive work through the skill. <br>
Risk: The recommended always-validate workflow gives the hosted service a routine review role in agent interactions. <br>
Mitigation: Enable that workflow deliberately and inspect returned findings before acting on approvals, rejections, or generated code. <br>


## Reference(s): <br>
- [Server-resolved source repository](https://github.com/Verificate-Dev/verificate-clawhub-skill) <br>
- [ClawHub skill page](https://clawhub.ai/verificate-dev/skills/verificate-clawhub-skill) <br>
- [Verificate MCP homepage](https://verificate.ai/mcp) <br>
- [Verificate MCP server](https://mcp.verificate.ai/mcp) <br>
- [Verificate privacy policy](https://verificate.ai/privacy) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown or text responses with validation verdicts, severity-ranked findings, recommendations, generated code, setup commands, and configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Validation tools may return binary approve/reject outcomes; analysis tools provide advisory findings without a blocking verdict.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
