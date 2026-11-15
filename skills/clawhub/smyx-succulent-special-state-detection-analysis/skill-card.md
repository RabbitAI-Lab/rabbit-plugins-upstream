## Description:

Analyzes succulent images or videos to identify black rot, water-soaked leaves, and stretching, with severity grading and confidence information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Succulent owners, greenhouse operators, and flower shops can use the skill to classify visible black rot, water-soaked or translucent leaves, and stretching from plant images or video, with severity and confidence information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags account registration, credential storage and forwarding, and network behavior that does not match the stated plant image analysis purpose.

Mitigation: Avoid installation unless you have independently reviewed and accepted these behaviors; use only credentials you are comfortable exposing to the skill.

Risk: Images and videos are uploaded for analysis, and the security scan was partial because a referenced local path was missing.

Mitigation: Submit only media you are authorized to share, and review the referenced resources before use.

## Reference(s):

- [API Documentation](references/api_doc.md)
- [Skill introduction demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured analysis results as JSON or Markdown text, with a report link when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Classifies succulent condition and reports severity and confidence; accepts image or video input.]

## Skill Version(s):

1.0.17 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
