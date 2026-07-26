## Description: <br>
多代理协同编排系统，帮助 agents plan fan-out, pipeline, and coordinator-style subagent workflows with task assignment, mailbox communication, and result aggregation guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lxr-666](https://clawhub.ai/user/lxr-666) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to decide when and how to split work across subagents, coordinate parallel or sequential tasks, and collect results without overusing multi-agent workflows for simple requests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Subagents may inherit the main agent's permissions and increase token or tool usage. <br>
Mitigation: Review delegation prompts before use, keep task descriptions precise, and reserve multi-agent workflows for requests that benefit from parallel or staged work. <br>
Risk: Broad triggers such as 'then' or 'assign tasks' can split work more aggressively than intended. <br>
Mitigation: Constrain the number of child agents and confirm the intended fan-out, pipeline, or coordinator pattern before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lxr-666/claude-code-orchestrator) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands] <br>
**Output Format:** [Markdown guidance with inline code blocks and orchestration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only guidance; no executable payload is included in the artifact.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
