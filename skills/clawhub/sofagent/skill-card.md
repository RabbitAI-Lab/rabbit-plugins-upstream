## Description:

Guides field deployment engineers through enterprise AI discovery, evaluation, delivery, and ongoing improvement while adding agent behavior constraints and change audits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kongfangxun](https://clawhub.ai/user/kongfangxun)

### License/Terms of Use:

MIT-0

## Use Case:

Field deployment engineers and enterprise teams use this skill to assess AI opportunities, quantify value, plan deployments, audit changes, and capture lessons for continued improvement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the full harness can modify agent integrations and persistent configuration beyond the FDE guidance workflow.

Mitigation: Review the installer and identify affected integrations and configuration files before installation; back up existing settings.

Risk: Connected tools can reach sensitive device data, cloud training, pull-request merges, and workflow changes.

Mitigation: Disable unneeded tools, restrict permissions to the task, and use least-privilege credentials and human approval for consequential actions.

Risk: Background monitoring and ongoing optimization can retain authority after initial setup.

Mitigation: Enable persistent services only when required and periodically review their access and activity.

## Reference(s):

- [FDE Skill on ClawHub](https://clawhub.ai/kongfangxun/skills/sofagent)
- [FDE Skill guide](artifact/SKILL.md)
- [FDE delivery guidance](artifact/skills/04-deliver.md)

## Skill Output:

**Output Type(s):** [Markdown, Configuration guidance, Shell commands]

**Output Format:** [Markdown with structured plans, audit summaries, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose enterprise-specific skill documents and deployment checklists.]

## Skill Version(s):

1.5.3 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
