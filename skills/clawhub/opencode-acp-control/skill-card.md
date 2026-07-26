## Description: <br>
Control OpenCode directly via the Agent Client Protocol (ACP). Start sessions, send prompts, resume conversations, and manage OpenCode updates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bjesuiter](https://clawhub.ai/user/bjesuiter) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use this skill to control OpenCode through ACP, including starting sessions, sending prompts, resuming prior conversations, and coordinating OpenCode updates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The update workflow can stop OpenCode processes broadly. <br>
Mitigation: Before using the update workflow, ask the agent to list exactly which OpenCode processes it would stop and approve only the intended restarts. <br>
Risk: The skill recommends a manual installer command that pipes a remote script into bash. <br>
Mitigation: Prefer a verified release or inspect the installer before running it. <br>
Risk: Using OpenCode through ACP can grant project file and terminal access. <br>
Mitigation: Install only when you trust OpenCode and are comfortable granting the expected project and terminal access. <br>


## Reference(s): <br>
- [ACP Protocol Docs for Agents and LLMs](https://agentclientprotocol.com/llms.txt) <br>
- [GitHub Repository](https://github.com/bjesuiter/opencode-acp-skill) <br>
- [Issue Tracker](https://github.com/bjesuiter/opencode-acp-skill/issues) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON-RPC examples and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance can include process-control steps for OpenCode ACP sessions and update checks.] <br>

## Skill Version(s): <br>
1.0.2 (source: SKILL.md metadata and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
