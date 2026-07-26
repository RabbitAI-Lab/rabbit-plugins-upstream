## Description: <br>
Repo-aware router skill for AI coding CLIs: map tasks to the right repository, project skill or agent, and native CLI backend across OpenClaw, Claude Code, OpenCode, Codex, Cursor, and Hermes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wufei-png](https://clawhub.ai/user/wufei-png) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use AgentRepoRouter to route AI coding tasks to the intended repository, local project skill or agent, and native CLI backend while preserving host-specific conventions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The external runtime installer can modify local agent configuration. <br>
Mitigation: Review the linked repository source before installation and choose narrow options for repository discovery, target agent hosts, and execution CLIs. <br>
Risk: Routing guidance or selected CLI targets could send work to an unintended repository or backend. <br>
Mitigation: Review generated repository mappings and scan the installed runtime skill before deployment. <br>


## Reference(s): <br>
- [ClawHub AgentRepoRouter page](https://clawhub.ai/wufei-png/skills/agent-repo-router) <br>
- [Official repository listed by the install notice](https://github.com/wufei-png/AgentRepoRouter) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, configuration, shell commands] <br>
**Output Format:** [Markdown guidance with configuration and command-oriented instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The ClawHub package is a navigation-only install notice; the external runtime may create local repository mappings and link router skill files into selected agent-host directories.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
