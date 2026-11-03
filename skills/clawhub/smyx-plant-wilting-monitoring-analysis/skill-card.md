## Description:

Early monitoring of plant wilting based on hyperspectral imaging and computer vision, captures early wilting signs before visible symptoms, provides early warning for precision irrigation and disease control.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Growers and plant health teams use the skill to analyze plant images or videos for early wilting signs, distinguish environmental stress from possible disease, and inform irrigation or follow-up assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account enrollment and credential storage are not clearly disclosed, and upload controls may not govern data disclosure.

Mitigation: Review before installing. Request clear account-enrollment disclosure and protected credential storage before using sensitive media or a shared workspace; do not rely on --api-url or --export-env-only to control disclosure.

Risk: Cloud deletion and specialized analysis claims are unverified.

Mitigation: Do not assume uploaded media is deleted; avoid sensitive media until retention behavior is confirmed, and treat analysis as an early warning for field follow-up.

Risk: A monitoring result could be mistaken for a definitive plant-health diagnosis.

Mitigation: Confirm findings against field conditions and consult a plant-health expert for diagnosis.

## Reference(s):

- [API Interface Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-wilting-monitoring-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured analysis results and report links; historical report listings can be presented as Markdown tables.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts plant media for analysis and can retrieve historical reports. Treat results as early warnings and confirm diagnoses in the field.]

## Skill Version(s):

1.0.18 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
