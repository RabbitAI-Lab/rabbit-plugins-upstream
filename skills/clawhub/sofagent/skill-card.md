## Description:

Guides frontline deployment engineers through enterprise AI assessment, delivery, audit, and ongoing improvement with agent behavior constraints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kongfangxun](https://clawhub.ai/user/kongfangxun)

### License/Terms of Use:

MIT-0

## Use Case:

Frontline deployment engineers and enterprise AI teams use this skill to assess workflows, quantify opportunities, guide AI deployment, audit changes, and maintain knowledge after delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation and enabled tools can grant broad administrative access.

Mitigation: Verify the installer source and enable only the MCP roles and tools needed for the deployment.

Risk: Persistent automation and external data movement can expose enterprise information.

Mitigation: Disable daemon, webhook, and data-push features unless required; confirm where local data and knowledge are stored and approve external transfers.

Risk: Restore, PR merge, model switching, registration, and training can affect production assets.

Mitigation: Require human approval for these operations before execution.

## Reference(s):

- [ClawHub FDE Skill release](https://clawhub.ai/kongfangxun/skills/sofagent)
- [FDE deployment stages](skills/01-entry.md)
- [FDE delivery guidance](skills/04-deliver.md)
- [FDE ongoing improvement guidance](skills/05-exit.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Configuration instructions, Shell commands]

**Output Format:** [Markdown guidance and reports with optional configuration and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include workflow assessments, deployment plans, audit results, and knowledge updates.]

## Skill Version(s):

1.5.8 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
