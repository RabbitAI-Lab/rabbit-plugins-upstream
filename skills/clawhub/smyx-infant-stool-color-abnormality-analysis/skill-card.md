## Description:

Analyzes infant diaper or stool images to classify stool color, flag clay-pale or bloody findings, and return risk reminders with suggested next actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, pediatric clinics, postpartum care centers, and developers integrating infant-care workflows can use this skill to screen diaper or stool images for visual color abnormalities and receive structured risk guidance. It is screening support only and does not replace clinician assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive infant health images and identity-linked report history.

Mitigation: Review the cloud processor, retention policy, guardian-consent flow, and account model before using real infant images or report history.

Risk: Default development HTTP endpoints and plaintext token storage could expose credentials, images, or report data.

Mitigation: Remove development endpoints, enforce HTTPS before sending credentials or images, and protect token storage or make it explicitly opt-in.

Risk: Visual stool-color classification can be mistaken for a medical diagnosis.

Mitigation: Present results as screening guidance only and direct users to pediatric or pediatric-surgery evaluation for clay-pale, bloody, or otherwise high-risk results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-stool-color-abnormality-analysis)
- [Infant stool color API documentation](artifact/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Guidance]

**Output Format:** [Markdown text containing structured JSON analysis, risk guidance, report links, or history tables; optional saved output file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports basic, standard, and json detail modes plus a history-list mode.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
