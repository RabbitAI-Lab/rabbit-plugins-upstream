## Description:

FDE Skill helps frontline deployment engineers guide enterprise AI rollout by constraining agent behavior, auditing changes, capturing operational knowledge, and supporting ongoing optimization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kongfangxun](https://clawhub.ai/user/kongfangxun)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, enterprise IT teams, and frontline deployment engineers use this skill to structure enterprise AI deployment work: discovery, workflow mapping, AI-node evaluation, delivery, audit, and post-deployment optimization. It is intended for broad deployment and audit harness behavior rather than lightweight documentation assistance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks for broad enterprise deployment, orchestration, local persistence, and activation authority.

Mitigation: Install it only when that operating posture is intended, and confirm where .sofagent, task/logs, knowledge, eval, and orchestrator data will be written before use.

Risk: Local records and generated knowledge may include sensitive enterprise workflow or audit information.

Mitigation: Enable redaction and retention policies before use, and avoid sensitive repositories until those controls are configured.

Risk: Activation, USB creation, git commits, model or workflow changes, and scheduled automation can materially change local systems or enterprise workflows.

Mitigation: Require explicit approval for these actions and preserve human review for high-impact automation decisions.

## Reference(s):

- [ClawHub sofagent release page](https://clawhub.ai/kongfangxun/skills/sofagent)
- [Agency Agents Chinese template collection](https://github.com/jnMetaCode/agency-agents-zh)
- [Minimal change engineer source template](https://github.com/jnMetaCode/agency-agents-zh/blob/main/engineering/engineering-minimal-change-engineer.md)
- [Code reviewer source template](https://github.com/jnMetaCode/agency-agents-zh/blob/main/engineering/engineering-code-reviewer.md)
- [DeepAgentsJS](https://github.com/langchain-ai/deepagentsjs)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with command examples, structured reports, configuration instructions, and generated skill or workflow content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide local persistence, audit logs, knowledge files, task logs, workflow files, and operational handoff materials when the user enables the related tools.]

## Skill Version(s):

1.3.8 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
