## Description: <br>
Integrates MCP tool server orchestration, persistent state, and session synchronization utilities for OpenClaw/Clawdbot agents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[enderfga](https://clawhub.ai/user/enderfga) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers building OpenClaw, Clawdbot, or Claude Code integrations use this skill to configure and operate MCP tool servers, call tools, persist state, and merge sessions across devices. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Spawned MCP tool servers may receive broad command and environment access. <br>
Mitigation: Use only trusted MCP servers, run with minimal secrets, and prefer explicit per-server environment allowlists. <br>
Risk: Configuration examples include token-bearing environment variables. <br>
Mitigation: Avoid hardcoding real tokens in config files and load credentials from a controlled secret source. <br>
Risk: Persistent state and session sync may retain sensitive chat, config, or project data. <br>
Mitigation: Confirm what data is stored or synced before using the skill with sensitive projects. <br>
Risk: The security guidance recommends dependency upgrades before broader use. <br>
Mitigation: Upgrade flagged dependencies and rescan the release before production deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/enderfga/skills/claude-code-skill) <br>
- [npm package](https://www.npmjs.com/package/openclaw-claude-code-skill) <br>
- [Model Context Protocol specification](https://spec.modelcontextprotocol.io/) <br>


## Skill Output: <br>
**Output Type(s):** [code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with TypeScript, JSON, and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include MCP server configuration examples, TypeScript API usage, and state persistence guidance.] <br>

## Skill Version(s): <br>
0.2.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
