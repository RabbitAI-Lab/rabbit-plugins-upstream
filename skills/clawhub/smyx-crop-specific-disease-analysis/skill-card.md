## Description:

Expands the disease identification library to cover economic-crop-specific diseases such as corn northern and southern leaf blight, potato late blight, peanut leaf spot, and tomato viral disease for precise leaf-disease recognition.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agricultural-support agents use this skill to analyze crop leaf images or videos for crop-specific disease identification, confidence, symptoms, and report links. It is intended for visual screening of corn, potato, peanut, tomato, and related economic-crop leaf diseases, not for treatment recommendations or definitive diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crop images, videos, and report-history requests are sent to configured lifeemergence.com services.

Mitigation: Install only where that data sharing is acceptable, and constrain network access or data retention for shared and sensitive environments.

Risk: The security summary says the skill silently creates or reuses user identities and stores service tokens locally.

Mitigation: Review workspace storage, token handling, and identity behavior before deployment, especially on shared machines.

Risk: The skill provides visual disease screening results that may be incorrect or incomplete.

Mitigation: Use results as preliminary guidance and confirm important crop-health decisions with field conditions and qualified agricultural expertise.

## Reference(s):

- [Crop-specific disease API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-crop-specific-disease-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, JSON]

**Output Format:** [Structured analysis report or Markdown table; detailed mode may emit JSON-oriented content.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include disease type, confidence, symptom description, analysis time, and report links; optional output files can store the generated result.]

## Skill Version(s):

1.0.12 (source: server release metadata; artifact frontmatter lists 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
