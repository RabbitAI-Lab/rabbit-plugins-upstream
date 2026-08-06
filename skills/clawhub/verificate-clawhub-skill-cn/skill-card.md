## Description: <br>
Verificate Cn connects OpenClaw to Verificate's hosted MCP validation service to review AI outputs, code, tool calls, research answers, and plans with deterministic gates and model review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[verificate-dev](https://clawhub.ai/user/verificate-dev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to validate AI-generated code, documentation, plans, tool calls, and research responses before accepting or shipping the work. It can return binary validation decisions, ordered issue lists, advisory code analysis, generated code, and setup guidance for the hosted Verificate MCP service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Code, documentation, plans, or AI outputs may be sent to Verificate's hosted MCP service for review. <br>
Mitigation: Install only for projects where external hosted review is acceptable, and review the provider's privacy and pricing terms before use. <br>
Risk: Always-on validation instructions can block or shape when the agent considers work complete. <br>
Mitigation: Use explicit agent instructions for rejected results, require fixes before resubmission, and keep human review available for blocked completions. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/verificate-dev/skills/verificate-clawhub-skill-cn) <br>
- [Server-resolved GitHub provenance](https://github.com/Verificate-Dev/verificate-clawhub-skill-cn) <br>
- [Verificate MCP homepage](https://verificate.ai/mcp) <br>
- [Verificate MCP endpoint](https://mcp.verificate.ai/mcp) <br>
- [Verificate MCP quickstart clients](https://github.com/Verificate-Dev/verificate-mcp-quickstart) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown and plain text with inline commands, verdicts, ordered issue lists, analysis, and optional generated code] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Validation outputs may include pass or reject decisions; advisory analysis provides scoring and conclusions without blocking.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
