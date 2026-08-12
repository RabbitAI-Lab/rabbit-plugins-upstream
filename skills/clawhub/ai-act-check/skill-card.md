## Description:

AI Act Check is a bilingual EU AI Act compliance self-check skill that previews 12 checklist items offline or sends responses to the CQDev cloud scoring service to generate text, JSON, or HTML reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wwumit](https://clawhub.ai/user/wwumit)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and compliance teams use this skill to assess an AI system against 12 EU AI Act checklist items and generate a scored report with risk level and remediation guidance. It is a self-check aid and not legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scored checks transmit EU AI Act checklist answers to compliancehub.cn for cloud scoring.

Mitigation: Run the offline preview mode for local-only review, and run scored checks only when the user is comfortable sending the answers to the cloud service.

Risk: API keys may be exposed if stored carelessly on shared systems.

Mitigation: Prefer the COMPLIANCEHUB_API_KEY environment variable or a private 0600 key file under ~/.config/compliancehub.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wwumit/skills/ai-act-check)
- [ComplianceHub cloud scoring service](https://compliancehub.cn)

## Skill Output:

**Output Type(s):** [text, json, html, shell commands, configuration, guidance]

**Output Format:** [CLI text output, JSON, or HTML report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scored runs send checklist answers to compliancehub.cn; non-interactive preview mode remains offline.]

## Skill Version(s):

1.0.2 (source: server release metadata and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
