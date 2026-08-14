## Description:

AI Persona Check helps agents run a 10-item compliance checklist for AI persona-based interactive services under China's Interim Measures and produce local preview or scored compliance reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wwumit](https://clawhub.ai/user/wwumit)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and compliance reviewers use this skill to preview AI-persona compliance checks offline or submit self-reported answers for cloud scoring and report generation. It is intended for services assessing obligations under China's AI persona-based interactive service rules.

### Deployment Geography for Use:

Global, for services assessing obligations under China's AI persona-based interactive service rules.

## Known Risks and Mitigations:

Risk: Scored runs send self-reported compliance answers, and optionally an API key or anonymous trial ID, to compliancehub.cn.

Mitigation: Use the non-interactive preview modes for offline review, and run cloud scoring only after the user explicitly opts in to sending the answers.

Risk: The generated compliance report is based on self-reported answers and is not a regulatory, audit, or legal conclusion.

Mitigation: Treat the output as general compliance guidance and have qualified counsel or compliance staff review it before relying on it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wwumit/skills/ai-persona-check)
- [complianceHub account and API key page](https://compliancehub.cn/account.html?skill=ai-persona-check)
- [complianceHub service endpoint](https://compliancehub.cn)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance]

**Output Format:** [Plain text, JSON, or HTML compliance report with command-line guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can write reports to a user-selected output file; offline preview modes avoid network submission.]

## Skill Version(s):

1.0.0 (source: server release metadata, package.json, _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
