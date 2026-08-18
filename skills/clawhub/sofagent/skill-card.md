## Description:

SKILL helps frontline deployment engineers structure enterprise AI rollouts by constraining agent behavior, auditing changes, capturing lessons, and guiding phased discovery, quantification, delivery, and handoff.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kongfangxun](https://clawhub.ai/user/kongfangxun)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, deployment engineers, and enterprise AI teams use this skill to diagnose business workflows, define AI deployment nodes, apply agent operating constraints, run compliance-oriented audits, and preserve lessons for future sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent business-knowledge storage and session reuse can expose sensitive enterprise information if logs, audit reports, ontology data, or summaries are retained too broadly.

Mitigation: Confirm storage locations before installation, enable redaction, set retention limits, and avoid use where broad local business data should not be indexed or reused.

Risk: Automation, deployment actions, subagents, and operational controls have loose scoping and may perform impactful local actions.

Mitigation: Require explicit approval for install, activation, USB writes, snapshot or model changes, and daemon sustain mode before running them in a real enterprise environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kongfangxun/skills/sofagent)
- [Agency Agents Chinese templates](https://github.com/jnMetaCode/agency-agents-zh)
- [Minimal-change engineer template](https://github.com/jnMetaCode/agency-agents-zh/blob/main/engineering/engineering-minimal-change-engineer.md)
- [Code reviewer template](https://github.com/jnMetaCode/agency-agents-zh/blob/main/engineering/engineering-code-reviewer.md)
- [DeepAgentsJS](https://github.com/langchain-ai/deepagentsjs)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with command examples and configuration/file-writing instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents to create or update local knowledge, audit, task, and configuration files.]

## Skill Version(s):

1.3.6 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
