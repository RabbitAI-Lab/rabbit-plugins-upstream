## Description:

A practical AI agent governance playbook covering agent risk identification, lifecycle governance, accountability, compliance mapping, least-privilege guardrails, incident response workflows, and a local checklist and scoring toolkit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Executives, compliance teams, legal teams, security teams, and AI engineering leaders use this skill to assess AI agent risks, design permission guardrails, create governance workflows, assign accountability, and plan incident response.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Legal or regulatory guidance may become outdated or may not fit a specific compliance obligation.

Mitigation: Independently verify legal and regulatory claims against official sources and qualified advisors before relying on them for compliance decisions.

Risk: The package includes a local Python helper that executes code when invoked.

Mitigation: Run the helper only when local code execution is intended, and review the command inputs and output before applying recommendations.

## Reference(s):

- [01 Agent 与风险全景](references/01-Agent与风险全景.md)
- [02 Agent 生命周期治理](references/02-Agent生命周期治理.md)
- [03 Agent 权限与护栏](references/03-Agent权限与护栏.md)
- [04 Agent 责任分配](references/04-Agent责任分配.md)
- [05 Agent 监管与合规](references/05-Agent监管与合规.md)
- [06 Agent 治理制度模板](references/06-Agent治理制度模板.md)
- [07 Agent 治理 FAQ](references/07-FAQ.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, text, shell commands]

**Output Format:** [Markdown guidance with optional local shell commands and text reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The local helper uses Python standard library commands for risk, permission, maturity, liability, and regulation checks.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
