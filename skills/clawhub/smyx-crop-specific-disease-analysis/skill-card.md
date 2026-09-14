## Description:

Identifies crop-specific leaf diseases in images or videos for crops such as corn, potatoes, peanuts, and tomatoes, returning structured disease findings and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agricultural support workflows can use this skill to screen images or videos of economic-crop leaves for crop-specific disease labels, confidence, symptoms, and report links. Outputs are for visual screening and should be paired with field judgment or expert confirmation for diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crop images or videos and report history may be sent to the publisher's service.

Mitigation: Use only with data the user is comfortable sharing with the publisher service, and disclose the external processing and report-history behavior before deployment.

Risk: The security evidence reports insecure HTTP development endpoints and plaintext local identity or token storage.

Mitigation: Require HTTPS-only production endpoints and secure credential storage before treating the skill as low risk.

Risk: Visual disease recognition can be incomplete or misleading if images are poor quality or symptoms overlap across diseases.

Mitigation: Present results as screening output and recommend confirmation against field conditions or expert review for consequential crop decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-crop-specific-disease-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Crop-specific disease API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands]

**Output Format:** [Structured text or JSON; history results may be formatted as a Markdown table.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include disease type, confidence, symptom description, analysis time, and report links.]

## Skill Version(s):

1.0.11 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
