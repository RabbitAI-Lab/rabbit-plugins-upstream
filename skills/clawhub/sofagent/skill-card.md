## Description:

FDE Skill helps frontline deployment engineers guide enterprise AI rollout by constraining agent behavior, auditing changes, retaining lessons, and supporting continuous optimization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kongfangxun](https://clawhub.ai/user/kongfangxun)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, frontline deployment engineers, and enterprise AI teams use this skill to diagnose business workflows, identify AI deployment nodes, build operational knowledge, and produce deployable enterprise-specific agent skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run orchestration workflows and affect deployed systems.

Mitigation: Restrict enabled tools and require human approval for workflow execution and deployed-system changes.

Risk: The skill can persist memory and generated skills.

Mitigation: Configure offline mode, storage paths, retention policy, and review of generated files before deployment.

Risk: The skill references CLI, MCP server, installer, activation, model, and snapshot operations.

Mitigation: Verify the referenced runtime components before use and require human approval for evolve, snapshot restore, model changes, USB creation, and activation.

## Reference(s):

- [FDE Skill on ClawHub](https://clawhub.ai/kongfangxun/skills/sofagent)
- [sofagent Agent Library](artifact/AGENTS.md)
- [Entry Phase Guide](artifact/skills/01-entry.md)
- [Discovery Phase Guide](artifact/skills/02-discovery.md)
- [Quantification Phase Guide](artifact/skills/03-quantify.md)
- [Delivery Phase Guide](artifact/skills/04-deliver.md)
- [Exit Phase Guide](artifact/skills/05-exit.md)
- [Agency Agents Minimal Change Engineer Template](https://github.com/jnMetaCode/agency-agents-zh/blob/main/engineering/engineering-minimal-change-engineer.md)
- [Agency Agents Code Reviewer Template](https://github.com/jnMetaCode/agency-agents-zh/blob/main/engineering/engineering-code-reviewer.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured handoff reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce audit reports, deployment checklists, business workflow summaries, knowledge-base entries, and enterprise-specific skill handoff material.]

## Skill Version(s):

1.4.0 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
