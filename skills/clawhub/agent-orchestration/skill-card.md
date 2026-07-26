## Description: <br>
Agent Orchestration helps users spawn and manage sub-agents with structured prompts, tracking templates, and learning loops. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clawdnw](https://clawhub.ai/user/clawdnw) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to structure prompts, delegate work to builder, research, and review agents, track active sub-agents, and capture lessons from completed work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sub-agents may act outside the intended workspace, command budget, or research scope if prompts are left broad. <br>
Mitigation: Set explicit workspace paths, command limits, research boundaries, and approval rules before using the templates. <br>
Risk: Tracking and learning notes may expose secrets, credentials, private customer data, or confidential project details. <br>
Mitigation: Do not write sensitive data into active-agents.md, LEARNINGS.md, or derived tracking documents. <br>
Risk: Agent outputs can contain incorrect or misleading guidance even when the template is followed. <br>
Mitigation: Review agent outputs and scan generated skills or artifacts before deployment. <br>


## Reference(s): <br>
- [Agent Orchestration on ClawHub](https://clawhub.ai/clawdnw/skills/agent-orchestration) <br>
- [Active Agents Tracking Template](examples/active-agents.md) <br>
- [Builder Agent Template](templates/builder-agent.md) <br>
- [Research Agent Template](templates/research-agent.md) <br>
- [Review Agent Template](templates/review-agent.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with reusable prompt templates and inline shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces prompt structures, tracking-table templates, review criteria, and operational guidance for managing sub-agents.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter declares 2.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
