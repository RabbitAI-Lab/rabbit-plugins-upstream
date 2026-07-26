## Description: <br>
HeartFlow is a local JavaScript cognitive engine that converts user input into structured cognition, memory, emotion, reasoning, decision, and code-execution signals for agent pipelines. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yun520-1](https://clawhub.ai/user/yun520-1) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to add a local preprocessing layer that turns raw user input into structured cognitive state for downstream LLM decision making. It can also expose CLI and MCP workflows for status checks, cognitive analysis, and agent integration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can provide local code and shell execution features. <br>
Mitigation: Keep code execution disabled unless needed, review proposed commands before running them, and avoid untrusted code inputs. <br>
Risk: The skill can persist local memory and conversation-derived data. <br>
Mitigation: Use it only with conversations and local data you are comfortable storing, and review the configured data directory before deployment. <br>
Risk: The skill can expose a localhost MCP server and use network-capable features when configured. <br>
Mitigation: Set MCP authentication before using the server, review API keys and environment variables, and enable network features only when required. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/yun520-1/skills/heartflow-engine) <br>
- [README](README.md) <br>
- [Skill definition](SKILL.md) <br>
- [Installation guide](INSTALL.md) <br>
- [Security and code audit report v5.3.0](docs/audit-report-v5.3.0.md) <br>
- [Benchmark report v5.5.1](docs/benchmark-report-v5.5.1.md) <br>
- [Inner OS protocol reference](references/inner-os-protocol.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Structured cognitive state, Markdown guidance, JavaScript APIs, CLI commands, and MCP tool responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May persist local memory and expose localhost MCP tools when configured.] <br>

## Skill Version(s): <br>
5.7.3 (source: server release evidence and package.json, released 2026-07-04) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
