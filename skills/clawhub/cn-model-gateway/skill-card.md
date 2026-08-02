## Description: <br>
cn-model-gateway is a Python MCP gateway that lets agent frameworks call multiple Chinese large-model providers through JSON-RPC tools, resources, prompts, CLI commands, and framework adapters. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fyniujin](https://clawhub.ai/user/fyniujin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to connect Claude Code, Cursor, Cline, n8n, and other agent workflows to configured model-provider APIs through a unified MCP interface. It also supports provider comparison, health checks, local usage statistics, benchmark runs, token-price tracking, and non-MCP framework adapters. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts are routed through configured third-party model-provider APIs. <br>
Mitigation: Install only when that routing is intended, review provider terms, and avoid sending secrets or sensitive data unless those terms allow it. <br>
Risk: API keys are provided through local configuration. <br>
Mitigation: Keep config.json private and do not commit or publish files that contain provider credentials. <br>
Risk: compare_models can fan out the same prompt to several providers. <br>
Mitigation: Use comparison mode only for prompts that are appropriate to share with every selected provider. <br>
Risk: Local usage databases may contain operational metadata about model calls. <br>
Mitigation: Protect the local usage database and align retention or cleanup with the user's privacy requirements. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/cn-model-gateway) <br>
- [README](README.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown, JSON-RPC responses, CLI text, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May route the same prompt to one or more configured third-party model providers; local usage data is stored in SQLite.] <br>

## Skill Version(s): <br>
1.3.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
