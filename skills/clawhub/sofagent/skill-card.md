## Description:

FDE Skill helps frontline deployment engineers guide enterprise AI rollout by constraining agent behavior, auditing changes, building knowledge and ontology context, and sustaining post-deployment improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kongfangxun](https://clawhub.ai/user/kongfangxun)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, enterprise AI deployment teams, and frontline deployment engineers use this skill to structure business-process discovery, identify AI-ready workflow nodes, configure agent constraints, and guide deployment, audit, and handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad local enterprise-agent authority may affect deployment, orchestration, persistence, and configuration.

Mitigation: Review the installer before use, confirm the enabled MCP tools, and install only where that authority is intended.

Risk: Local memory, logs, and knowledge data may contain sensitive enterprise information.

Mitigation: Decide where ~/.sofagent and .sofagent data are stored, enable log sanitization, and apply retention limits.

Risk: High-impact actions such as deployment, model switching, browser actions, USB creation, snapshot restore, and destructive operations can change local systems.

Mitigation: Require explicit human approval for these actions and keep audit trails for review.

Risk: Long-running daemon or sustain-mode operation can continue acting after initial deployment.

Mitigation: Define ownership, schedules, monitoring, and shutdown procedures before enabling continuous operation.

## Reference(s):

- [FDE Skill on ClawHub](https://clawhub.ai/kongfangxun/skills/sofagent)
- [engineering-minimal-change-engineer](https://github.com/jnMetaCode/agency-agents-zh/blob/main/engineering/engineering-minimal-change-engineer.md)
- [engineering-code-reviewer](https://github.com/jnMetaCode/agency-agents-zh/blob/main/engineering/engineering-code-reviewer.md)
- [DeepAgentsJS](https://github.com/langchain-ai/deepagentsjs)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and structured checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include staged deployment plans, audit summaries, ontology and workflow drafts, and handoff checklists.]

## Skill Version(s):

1.4.1 (source: frontmatter, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
