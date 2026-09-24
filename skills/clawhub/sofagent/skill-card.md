## Description:

FDE Skill helps frontline deployment engineers guide enterprise AI rollout by constraining agent behavior, auditing changes, preserving lessons learned, and supporting ongoing optimization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kongfangxun](https://clawhub.ai/user/kongfangxun)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, deployment engineers, and enterprise AI teams use this skill to structure FDE discovery, quantify automation opportunities, prepare deployment artifacts, and apply audit and human-review gates around broad agent operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad persistent tool access can modify local setup, register devices, move data, merge PRs, automate browsers, and run cloud-training workflows.

Mitigation: Deploy only when a broad enterprise agent harness is intended, test first in a controlled environment, and review MCP roles and tool allowlists before enabling the skill.

Risk: Installation and MCP configuration may change local agent setup and expose more operational capabilities than a simple guidance-only skill.

Mitigation: Verify the install.sh source before running it and keep device data movement, browser tools, PR merge, cloud training, daemon/webhook, and session-push features disabled unless explicitly approved.

Risk: Enterprise workflow and ontology outputs can influence business processes if accepted without review.

Mitigation: Require human review for deployment artifacts, data-boundary decisions, destructive operations, and automation affecting money, rights, compliance, HR, medical, or legal contexts.

## Reference(s):

- [FDE Skill on ClawHub](https://clawhub.ai/kongfangxun/skills/sofagent)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose local installation, MCP configuration, audit reports, and enterprise deployment artifacts for human review.]

## Skill Version(s):

1.5.1 (source: artifact/SKILL.md frontmatter and evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
