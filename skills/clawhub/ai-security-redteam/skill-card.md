## Description:

A hands-on AI security and red-teaming playbook that helps agents map AI attack surfaces, generate authorized test cases, grade findings, produce report templates, and suggest remediation for prompt injection, agent overreach, privacy leakage, hallucination, supply-chain, and denial-of-service risks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers, AI engineers, security testers, and security leaders use this skill to plan and document authorized AI red-team assessments. It provides attack-surface mapping, prompt-injection and agent-overreach test cases, privacy and hallucination checks, vulnerability grading, reporting templates, and remediation guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill contains bypass, privacy, escape, and denial-of-service examples that could be misused outside an authorized assessment.

Mitigation: Use examples only as controlled test cases for systems the user owns or is explicitly authorized to assess, with written scope and safeguards.

Risk: Checklist and report outputs may be mistaken for a final security conclusion.

Mitigation: Have qualified security reviewers validate scope, evidence, findings, and remediation before relying on results.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhaoxinghua09-cell/skills/ai-security-redteam)
- [AI Security Risk Overview](references/01-AI安全风险全景.md)
- [AI Red-Team Testing Workflow](references/02-红队测试流程.md)
- [Prompt Injection Testing](references/03-提示注入测试.md)
- [Overreach and Escape Testing](references/04-越权与逃逸测试.md)
- [Data and Privacy Testing](references/05-数据与隐私测试.md)
- [Hallucination and Quality Testing](references/06-幻觉与质量测试.md)
- [Supply Chain and Denial-of-Service Testing](references/07-供应链与拒绝服务.md)
- [Reporting and Remediation](references/08-报告与修复.md)
- [FAQ](references/09-FAQ.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with optional local Python CLI commands and text templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local, zero-dependency toolkit; security evidence states it does not automate attacks against real systems.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
