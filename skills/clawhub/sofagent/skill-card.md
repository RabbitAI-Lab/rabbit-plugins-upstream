## Description:

FDE Skill helps frontline deployment engineers guide enterprise AI rollouts by constraining agent behavior, auditing changes, capturing lessons, and running a structured diagnosis and delivery workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kongfangxun](https://clawhub.ai/user/kongfangxun)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, field deployment engineers, and enterprise AI teams use this skill to interview stakeholders, map workflows and business ontology, quantify automation candidates, produce enterprise-specific skills or workflows, and manage audit and continuous-improvement handoffs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill describes installation of a persistent enterprise agent governance layer that may change local files and platform configuration.

Mitigation: Review the missing install script or package before running it, and confirm what files and platform configs will be modified.

Risk: The skill describes broad MCP tool access, background services, webhooks, model training, and corpus export capabilities.

Mitigation: Limit MCP roles with SOFAGENT_MCP_ROLES and disable or avoid daemon, webhook, model-training, and corpus-export features unless they are needed.

Risk: The skill may create logs, knowledge records, and generated skills as part of enterprise deployment workflows.

Mitigation: Verify where logs, knowledge, and generated skills are stored, and apply data handling review before use with sensitive enterprise data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kongfangxun/skills/sofagent)
- [Agency Agents minimal change engineer template](https://github.com/jnMetaCode/agency-agents-zh/blob/main/engineering/engineering-minimal-change-engineer.md)
- [Agency Agents code reviewer template](https://github.com/jnMetaCode/agency-agents-zh/blob/main/engineering/engineering-code-reviewer.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, structured checklists, and configuration instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose MCP tool use and enterprise-specific skill or workflow artifacts; human review is expected for deployment, destructive actions, and sensitive data handling.]

## Skill Version(s):

1.4.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
