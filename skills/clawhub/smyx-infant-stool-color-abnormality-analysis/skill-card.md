## Description:

Analyzes infant diaper or stool images for concerning colors and provides risk alerts and suggested next steps without making a diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers and pediatric care teams use images of infant diapers or stool to review color classifications, risk alerts and suggested follow-up. The skill can also retrieve prior cloud reports; its results are not medical diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Infant diaper or stool images may be sent to a cloud service.

Mitigation: Obtain explicit guardian consent and share only the images needed for screening.

Risk: A reused identity and locally stored authentication tokens can link sensitive reports across sessions.

Mitigation: Protect local credentials, use an isolated test identity when evaluating the skill, and avoid history queries unless the records returned are understood.

Risk: Image-based color screening may be mistaken for a medical diagnosis.

Mitigation: Treat alerts as prompts for professional assessment, especially when concerning colors are flagged.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-stool-color-abnormality-analysis)
- [Stool color analysis API reference](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Structured analysis report or JSON; Markdown table for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Color classifications, risk alerts, suggested actions and report links; optional cloud history. Not a diagnosis.]

## Skill Version(s):

1.0.11 (source: ClawHub server release; bundled frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
