## Description:

FDE Skill guides front-line deployment engineers through enterprise AI rollout by constraining agent behavior, auditing changes, capturing lessons, and producing enterprise-specific deployment assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kongfangxun](https://clawhub.ai/user/kongfangxun)

### License/Terms of Use:

MIT-0

## Use Case:

Front-line deployment engineers, enterprise IT teams, and agent operators use this skill to assess business workflows, identify AI automation or augmentation nodes, build ontology-backed knowledge structures, guide deployment, run audit checks, and hand off an enterprise AI operating model.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Enterprise deployment, MCP configuration changes, local logging, daemon behavior, and broad automation tools can affect local systems and enterprise data handling.

Mitigation: Install only in an enterprise-controlled environment after reviewing installer behavior, MCP configuration changes, daemon behavior, log locations, retention policy, and enabled tool categories.

Risk: Broad tool categories such as model operations, browser automation, publishing, USB deployment, rollback, deletion, and persistent knowledge capture can create operational or data-governance exposure if enabled unnecessarily.

Mitigation: Use least privilege, disable unneeded capabilities, and require explicit human approval for deployment, training, rollback, deletion, external posting, and persistent knowledge capture.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kongfangxun/skills/sofagent)
- [Agency Agents minimal-change engineer template](https://github.com/jnMetaCode/agency-agents-zh/blob/main/engineering/engineering-minimal-change-engineer.md)
- [Agency Agents code reviewer template](https://github.com/jnMetaCode/agency-agents-zh/blob/main/engineering/engineering-code-reviewer.md)
- [DeepAgentsJS](https://github.com/langchain-ai/deepagentsjs)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Code, Text]

**Output Format:** [Markdown guidance with inline shell commands, structured checklists, reports, and configuration-oriented instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide creation of enterprise profiles, workflow and ontology descriptions, audit reports, deployment handbooks, custom rules, and local operating records.]

## Skill Version(s):

1.4.2 (source: artifact/SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
