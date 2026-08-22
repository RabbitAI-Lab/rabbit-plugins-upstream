## Description:

FDE Skill helps frontline deployment engineers guide enterprise AI adoption by constraining agent behavior, auditing changes, preserving deployment knowledge, and supporting continuous improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kongfangxun](https://clawhub.ai/user/kongfangxun)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, enterprise AI deployment teams, and frontline deployment engineers use this skill to structure enterprise AI discovery, workflow diagnosis, governance checks, deployment handoff, and post-delivery optimization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad deployment, orchestration, persistence, and local-execution behavior can affect enterprise AI environments if installed without review.

Mitigation: Review the skill before installation, constrain sofagent CLI and MCP permissions, and require human approval for high-impact actions.

Risk: Persistent data and operating state may be stored in .sofagent or OpenClaw locations.

Mitigation: Confirm storage locations, retention expectations, and access controls before activation.

Risk: Sustain mode and generated skill promotion can change future agent behavior.

Mitigation: Disable or explicitly approve daemon sustain mode, and review and scan generated or promoted skills before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kongfangxun/skills/sofagent)
- [Agency Agents Chinese templates](https://github.com/jnMetaCode/agency-agents-zh)
- [DeepAgentsJS](https://github.com/langchain-ai/deepagentsjs)
- [Minimal change engineer template](https://github.com/jnMetaCode/agency-agents-zh/blob/main/engineering/engineering-minimal-change-engineer.md)
- [Code reviewer template](https://github.com/jnMetaCode/agency-agents-zh/blob/main/engineering/engineering-code-reviewer.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and structured audit reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce audit reports, deployment handoff notes, configuration guidance, and skill promotion recommendations.]

## Skill Version(s):

1.3.9 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
