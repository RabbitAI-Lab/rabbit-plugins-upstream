## Description:

AI Ethics Check is a compliance checklist skill that helps users assess AI technology ethics review readiness against the 2026 China MIIT trial measures, with offline preview and cloud-scored reporting options.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wwumit](https://clawhub.ai/user/wwumit)

### License/Terms of Use:

MIT-0

## Use Case:

External users and compliance practitioners use this skill to preview 10 AI ethics review checks, answer compliance questions, and generate a local report for self-assessment. It is explicit opt-in because scored runs send the user's answers to compliancehub.cn.

### Deployment Geography for Use:

Global, with content focused on China AI ethics review requirements

## Known Risks and Mitigations:

Risk: Scored checks transmit the user's compliance answers to compliancehub.cn.

Mitigation: Use --non-interactive or --non-interactive-json for an offline preview, and run scored checks only when the user accepts that data transfer.

Risk: API keys are used for cloud scoring and could be exposed if stored carelessly.

Mitigation: Store the key only in COMPLIANCEHUB_API_KEY or the documented ~/.config/compliancehub key file with private file permissions.

Risk: The generated report is based on self-reported answers and is not a legal or regulatory conclusion.

Mitigation: Treat the report as compliance guidance and have qualified reviewers or counsel validate decisions before relying on it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wwumit/skills/ai-ethics-check)
- [Publisher profile](https://clawhub.ai/user/wwumit)
- [complianceHub account page](https://compliancehub.cn/account.html?skill=ai-ethics-check)

## Skill Output:

**Output Type(s):** [text, json, html, shell commands, configuration, guidance]

**Output Format:** [Text, JSON, or HTML reports with shell command examples and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scored runs submit answers to compliancehub.cn; non-interactive preview modes remain offline.]

## Skill Version(s):

1.0.0 (source: server release evidence, package.json, _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
