## Description:

A Chinese-language diabetes product pipeline skill for dietary-fiber blood glucose management businesses, covering knowledge monitoring, product and service-package design, multi-audience content, CGM-based validation reporting, and sales activation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangjiaocheng](https://clawhub.ai/user/wangjiaocheng)

### License/Terms of Use:

MIT-0

## Use Case:

External operators and developers in dietary-fiber glucose-management businesses use this skill to run an end-to-end workflow from diabetes-domain knowledge updates through product, content, validation, and sales materials. It is intended for commercial workflow support and requires medical, legal, privacy, and compliance review before real patient-data or customer-facing use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can process sensitive glucose-monitoring and patient context data.

Mitigation: Use only with explicit consent, data minimization, de-identification, retention limits, access controls, and jurisdiction-specific health-data compliance in place.

Risk: Generated health guidance or validation reports could be interpreted as individualized diabetes advice or clinical evidence.

Mitigation: Require clinician oversight, preserve evidence grading and uncertainty labels, and prevent outputs from replacing medical decisions or medication guidance.

Risk: Sales outreach and public content may create privacy, opt-out, advertising, or medical-claim compliance exposure.

Mitigation: Run legal and platform compliance review before publication or outreach, honor opt-out handling, and avoid claims not supported by reviewed evidence packages.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wangjiaocheng/skills/quanmi-fiber-pipeline)
- [Task catalog and dependency topology](artifact/references/qfp-catalog.md)
- [Task requirements](artifact/references/qfp-requirements.md)
- [Output exemplars catalog](artifact/references/qfp-exemplars.md)
- [Optional role definitions](artifact/references/qfp-roles.md)
- [Generic-to-specific substitution table](artifact/references/脱敏前后对照表.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown, markdown tables, JSON snippets, YAML snippets, workflow checklists, reports, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include medical, marketing, validation, and sales content; artifact guidance requires evidence labels, compliance checks, human review at calibration points, and de-identification for patient data.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
