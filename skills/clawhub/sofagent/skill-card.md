## Description:

FDE Skill helps frontline deployment engineers guide enterprise AI rollout by constraining agent behavior, auditing changes, preserving lessons learned, and supporting continuous optimization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kongfangxun](https://clawhub.ai/user/kongfangxun)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, deployment engineers, and enterprise AI governance teams use this skill to structure FDE discovery, workflow analysis, compliance auditing, knowledge capture, and delivery of organization-specific AI agent practices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can direct broad orchestration, persistent knowledge/history storage, local project writes, and long-lived workflow activation in an enterprise environment.

Mitigation: Install it only in a dedicated enterprise deployment context with administrative approval, scoped local directories, reviewed triggers, and explicit retention rules for profile and knowledge data.

Risk: Workflow activation and deployment guidance may affect enterprise AI nodes or operational processes.

Mitigation: Require confirmation before activating workflows or making deployment-impacting changes, and run the skill's audit path before release or handoff.

Risk: The skill includes guidance for maintaining knowledge and reflection files that may capture sensitive operational context.

Mitigation: Apply data minimization, redact sensitive content, and limit MCP tool access to approved repositories and knowledge stores.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kongfangxun/skills/sofagent)
- [Agency Agents Chinese templates](https://github.com/jnMetaCode/agency-agents-zh)
- [Engineering minimal-change engineer template](https://github.com/jnMetaCode/agency-agents-zh/blob/main/engineering/engineering-minimal-change-engineer.md)
- [Engineering code reviewer template](https://github.com/jnMetaCode/agency-agents-zh/blob/main/engineering/engineering-code-reviewer.md)
- [DeepAgentsJS](https://github.com/langchain-ai/deepagentsjs)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured audit or deployment reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce enterprise deployment notes, audit reports, workflow guidance, knowledge-base instructions, and follow-up optimization recommendations.]

## Skill Version(s):

1.3.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
