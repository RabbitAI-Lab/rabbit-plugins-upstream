## Description: <br>
Agent Team Kit is a process framework that helps AI agent teams manage work queues, roles, discovery, and heartbeat-driven operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ryancampbell](https://clawhub.ai/user/ryancampbell) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators of multi-agent workflows use this skill to set up self-service intake, backlog, role, status, and heartbeat processes for agent teams. It is most useful when agents need clear ownership and recurring checks to keep work moving without constant human triage. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can cause agents to coordinate, claim, or spawn work repeatedly without enough approval boundaries. <br>
Mitigation: Define which repositories and queues are in scope, cap agent spawning, and require human approval for destructive, deployment, public, financial, account, or credential-related actions. <br>
Risk: Self-service Ready queues and heartbeat checks can move work forward before a human has reviewed priority, scope, or downstream impact. <br>
Mitigation: Keep Ready criteria explicit, review queue changes before committing them, and route strategic decisions or blocked work to a human lead. <br>


## Reference(s): <br>
- [Agent Team Kit on ClawHub](https://clawhub.ai/ryancampbell/skills/agent-team-kit) <br>
- [OpenClaw](https://github.com/openclaw/openclaw) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown templates with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes process templates for intake, roles, backlog, opportunities, status tracking, and heartbeat checks.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
