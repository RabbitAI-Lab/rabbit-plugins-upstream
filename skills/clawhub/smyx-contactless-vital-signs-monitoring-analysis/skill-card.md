## Description:

Analyzes camera footage without wearables to estimate heart rate, respiration, blood oxygen, and heart rate variability.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Users can submit camera footage to receive estimated vital signs and query earlier monitoring reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Camera footage may contain sensitive health and identity information and may be processed remotely.

Mitigation: Submit only footage you are authorized to share, and confirm how the service handles it before processing.

Risk: The security assessment flags possible undeclared account and credential handling, privacy concerns, and account-sharing risks.

Mitigation: Review account and credential handling before installation; avoid exposing identifiers or secrets in prompts and reports.

Risk: Scanner coverage was partial, so some referenced material was not assessed.

Mitigation: Review the full package and relevant service documentation before installation or use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-contactless-vital-signs-monitoring-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API documentation](artifact/references/api_doc.md)
- [Analysis API errors and formats](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown]

**Output Format:** [Structured vital-sign analysis reports and Markdown tables of prior reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include risk notes, recommendations, and report links; results are for health reference and do not replace medical diagnosis.]

## Skill Version(s):

1.0.22 (source: server-resolved release; bundled SKILL.md says 1.0.25)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
