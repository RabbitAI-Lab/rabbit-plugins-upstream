## Description:

Expands the disease identification library to cover economic-crop-specific diseases such as corn northern and southern leaf blight, potato late blight, peanut leaf spot, and tomato viral disease for precise leaf-disease recognition.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agriculture-focused agents use this skill to analyze crop leaf images or videos for crop-specific disease identification and to retrieve prior disease-recognition reports. The skill is positioned for visual screening and structured reporting, not treatment or prevention advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crop images, videos, and history queries are sent to a remote service.

Mitigation: Review endpoint ownership, retention, access controls, and privacy expectations before installation or broad use.

Risk: The skill can create or reuse a local identity and store service tokens in the workspace data directory.

Mitigation: Run it in a controlled workspace, protect stored tokens, and clear or rotate credentials according to local policy.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-crop-specific-disease-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON or structured-text analysis results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save analysis output to a user-specified file; analysis and history lookups are performed through a remote service.]

## Skill Version(s):

1.0.10 (source: server release metadata; SKILL.md frontmatter is 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
