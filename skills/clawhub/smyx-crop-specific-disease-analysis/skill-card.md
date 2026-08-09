## Description:

Expands the disease identification library to cover economic-crop-specific diseases such as corn northern and southern leaf blight, potato late blight, peanut leaf spot, and tomato viral disease for precise leaf-disease recognition.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agricultural operators use this skill to analyze images, videos, local files, or URLs of crop leaves for crop-specific disease identification. It returns visual disease classifications, confidence, symptom descriptions, report links, and cloud history tables for economic crops such as corn, potato, peanut, and tomato.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Provided crop images, videos, local files, or URLs are sent to a cloud service for analysis.

Mitigation: Use only non-sensitive crop media and avoid private or signed URLs unless the publisher has clarified data handling and retention.

Risk: The skill can automatically create or reuse an identity, store tokens locally, and query cloud report history.

Mitigation: Review identity, token storage, retention, and cleanup behavior before installation, especially on shared workspaces.

Risk: Disease recognition results are visual analysis outputs and may not be a final field diagnosis.

Mitigation: Treat results as screening guidance and confirm important disease or treatment decisions with field conditions and an agricultural expert.

## Reference(s):

- [API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-crop-specific-disease-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, files]

**Output Format:** [Markdown or JSON analysis results, with optional saved text output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes disease type, confidence, symptom description, report link, and Markdown history tables when listing prior reports.]

## Skill Version(s):

1.0.7 (source: ClawHub release metadata; artifact frontmatter says 1.0.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
