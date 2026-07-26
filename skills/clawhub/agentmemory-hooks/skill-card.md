## Description: <br>
The agentmemory plugin hooks capture observations automatically across the agent session lifecycle for explaining memory capture, debugging missing observations, and tuning what gets recorded. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rohitg00](https://clawhub.ai/user/rohitg00) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to understand and troubleshoot automatic memory capture in the agentmemory Claude Code plugin, including hook registration, observed events, and optional summarization or context injection settings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automatic memory capture may record prompts, tool-use activity, session boundaries, and commit context by default. <br>
Mitigation: Review plugin configuration, storage location, retention behavior, and capture limits before using it with secrets or regulated data; disable or limit capture where needed. <br>


## Reference(s): <br>
- [Agentmemory Hooks source](https://github.com/rohitg00/agentmemory/tree/main/plugin/skills/agentmemory-hooks) <br>
- [Agentmemory Hooks on ClawHub](https://clawhub.ai/rohitg00/skills/agentmemory-hooks) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May refer to local plugin settings and the local observation monitor.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
