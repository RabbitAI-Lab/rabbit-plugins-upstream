## Description:

FDE Skill helps front-line deployment engineers guide enterprise AI implementation by constraining agent behavior, auditing changes, preserving operational knowledge, and supporting sustained optimization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kongfangxun](https://clawhub.ai/user/kongfangxun)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, enterprise IT teams, and front-line deployment engineers use this skill to structure enterprise AI rollout work, identify AI-ready workflow nodes, produce deployment guidance, run compliance-oriented audits, and maintain operational knowledge after handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide enterprise deployment and audit activity from broad triggers.

Mitigation: Activate deployment or audit modes only after explicit human approval and a clearly scoped task.

Risk: The artifact includes shell-oriented deployment, audit, and USB creation examples that can affect local systems or target media.

Mitigation: Review each command, arguments, and target paths before execution, especially USB targets and installer or activation commands.

Risk: Sustain, model, snapshot, workflow, and self-evolution actions can change runtime behavior over time.

Mitigation: Keep these actions behind human approval, disable or narrowly scope daemon sustain behavior unless it is required, and retain audit logs for review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kongfangxun/skills/sofagent)
- [Agency Agents Chinese templates](https://github.com/jnMetaCode/agency-agents-zh)
- [Engineering minimal-change engineer template](https://github.com/jnMetaCode/agency-agents-zh/blob/main/engineering/engineering-minimal-change-engineer.md)
- [Engineering code reviewer template](https://github.com/jnMetaCode/agency-agents-zh/blob/main/engineering/engineering-code-reviewer.md)
- [DeepAgentsJS](https://github.com/langchain-ai/deepagentsjs)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples and structured audit or deployment reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference MCP tools, local files, deployment checklists, audit reports, and human approval gates.]

## Skill Version(s):

1.3.7 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
