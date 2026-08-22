## Description:

Analyzes fixed-camera footage of an elder's water-cup area to count cup pickup events as an indirect drinking-frequency signal and produce dehydration-risk reminders for caregivers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, elder-care operators, and developers use this skill to analyze home or facility camera footage for cup-pickup frequency, long intervals without drinking, and directional reminders. It supports monitoring workflows but does not provide a medical diagnosis or direct measurement of actual fluid intake.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads sensitive in-home elder-care footage and stores or retrieves historical reports through cloud services.

Mitigation: Use only with clear consent from the monitored person or legal guardian, confirm service endpoints, retention terms, and report-access controls before processing real footage.

Risk: Reports are associated with hidden local or cloud identity state.

Mitigation: Confirm which account identity is used, separate test and production accounts, and review historical report visibility before deployment.

Risk: Cup pickup counts are an indirect proxy and may not prove actual water intake or dehydration.

Mitigation: Present outputs as directional care reminders, combine them with caregiver observation and personal baselines, and seek medical advice when symptoms or repeated concerns appear.

Risk: Camera placement, shared cups, guests, caregivers, poor lighting, or missing cup-region setup can reduce counting accuracy.

Mitigation: Use stable camera coverage of the cup area, define the cup ROI where supported, prefer privacy-preserving outline/object-box modes, and review uncertain results with caregivers.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-elderly-drinking-frequency-analysis)
- [API Interface Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown or JSON structured analysis report with risk labels, caregiver reminder text, report links, and optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May query cloud report history and return Markdown tables for prior reports.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
