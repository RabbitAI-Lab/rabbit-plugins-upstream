## Description:

Analyzes fixed-camera video of an older adult at rest to estimate respiratory rate and produce structured tachypnea or dyspnea alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, care-platform operators, and developers use this skill to analyze resting chest or abdominal video from an elderly-care setting, estimate respiratory rate, classify risk level, and retrieve historical respiratory-monitoring reports. It is an assistive monitoring workflow and should not be used as a medical diagnosis or emergency triage system.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bedroom health videos or video URLs may be sent to configured cloud services.

Mitigation: Use only with informed consent from the monitored person or guardian, minimize captured media, and apply the organization's privacy, retention, and access controls before deployment.

Risk: The skill can automatically create or reuse an identity, query cloud history, and persist access tokens locally.

Mitigation: Review token storage and account-linking behavior before installation, restrict filesystem and network access, and rotate or revoke credentials when the skill is removed.

Risk: Respiratory alerts may be mistaken for medical diagnosis or emergency triage.

Mitigation: Present outputs as assistive monitoring only and require human verification and appropriate medical follow-up for urgent or concerning results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-elderly-tachypnea-detection-analysis)
- [API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON analysis report with optional shell command examples and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include respiratory rate, respiratory pattern, signal quality, risk level, alert text, follow-up guidance, and historical report links.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter states 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
