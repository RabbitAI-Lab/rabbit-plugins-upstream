## Description: <br>
Build, run, test, and publish local-first ContextUI visual workflows with React TSX, localhost Python backends, scoped UI automation, and optional Exchange operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[midz99](https://clawhub.ai/user/midz99) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to create, inspect, run, automate, and publish ContextUI workflows on a local desktop installation. It is intended for local workflow development with optional marketplace operations when a ContextUI API key is provided. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give an agent broad local workflow control, including file edits, UI actions, local server management, and MCP server connections. <br>
Mitigation: Install only from a trusted publisher, review requested actions before execution, and use an isolated VM, container, or dedicated user account for untrusted workflows. <br>
Risk: Local Python backends and workflow servers can expose data or behavior beyond the intended workflow if configured loosely. <br>
Mitigation: Keep backends bound to 127.0.0.1, avoid wildcard CORS for real workflows, and monitor package installs and model downloads. <br>
Risk: Exchange helper commands accept user-provided text and require an API key for marketplace operations. <br>
Mitigation: Inspect scripts/exchange.sh before use, avoid passing untrusted text through helper commands, and provide CONTEXTUI_API_KEY only when Exchange features are needed. <br>


## Reference(s): <br>
- [ContextUI website](https://contextui.ai) <br>
- [ContextUI YouTube](https://www.youtube.com/@ContextUI) <br>
- [Contextui on ClawHub](https://clawhub.ai/midz99/skills/contextui) <br>
- [Security Model](SECURITY.md) <br>
- [ContextUI MCP Tools](references/mcp-tools.md) <br>
- [Workflow Building Guide](references/workflow-guide.md) <br>
- [ServerLauncher Python Backend Pattern](references/server-launcher.md) <br>
- [ContextUI Exchange API](references/exchange-api.md) <br>
- [HuggingFace Cache Monitoring](references/cache-monitoring.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline JSON, bash, TypeScript, and Python examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are intended for local ContextUI workflows and may include instructions for localhost Python backends, UI automation, and optional Exchange API use.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
