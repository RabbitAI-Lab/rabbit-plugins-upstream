## Description:

Using a fixed camera above the baby-changing table or a smartphone, the skill captures high-resolution images of the diaper area or stool and uses AI visual analysis to identify normal and abnormal infant stool colors, including clay-pale, bright red, dark red, and tarry black.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, pediatric care teams, postpartum care centers, and developers can use this skill to run image-based infant stool color screening, receive risk reminders, and retrieve prior cloud reports. It is intended as a visual screening aid and should not replace professional pediatric evaluation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive infant health media or image URLs may be sent to lifeemergence cloud services.

Mitigation: Use only with guardian informed consent, and confirm the service destination and retention expectations before submitting images.

Risk: Analyses may be linked to a persistent local or cloud identity and later retrieved as report history.

Mitigation: Avoid shared workspaces unless identity separation is acceptable, and review local identity and cloud history behavior before deployment.

Risk: Lighting, filters, or image quality can make visual stool color classification unreliable.

Mitigation: Capture clear images under natural or cool white light, avoid filters, and treat abnormal or uncertain results as prompts for professional pediatric review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-stool-color-abnormality-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Infant stool color API documentation](artifact/references/api_doc.md)
- [SMYX analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown and JSON-style structured analysis reports with risk reminders, recommended actions, report links, and optional Markdown tables for history queries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include links to cloud-hosted reports and history retrieved from lifeemergence services.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
