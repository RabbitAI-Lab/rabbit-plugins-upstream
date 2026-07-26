## Description: <br>
Specifies an autonomous or tool-using AI agent before implementation, including its goals and scope, tool permissions, control loop, guardrails, memory, escalation path, evaluation plan, and failure handling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and teams use this skill to specify autonomous or tool-using AI agents before implementation, including the agent's scope, tools, permissions, control loop, guardrails, escalation path, evaluation plan, and failure handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated agent specifications may propose agents with real tools, durable memory, outbound actions, spending, or irreversible operations. <br>
Mitigation: Review the specification before implementation and require explicit human approval gates for irreversible, outbound, spending, or otherwise high-risk actions. <br>
Risk: An agent design may allow unbounded loops or unclear stopping conditions. <br>
Mitigation: Include hard max-step and max-cost budgets, clear escalation triggers, and a safe default of stopping to ask when uncertain. <br>


## Reference(s): <br>
- [Agent Spec ClawHub Skill](https://clawhub.ai/mohitagw15856/skills/agent-spec) <br>
- [Agent Spec Homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/agent-spec.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a structured agent specification with sections for goals, tools, permissions, control loop, guardrails, memory, escalation, evaluation, and failure handling.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
