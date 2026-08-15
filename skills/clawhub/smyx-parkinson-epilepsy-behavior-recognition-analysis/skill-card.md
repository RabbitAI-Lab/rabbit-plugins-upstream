## Description:

Identifies abnormal behaviors such as limb tremors, convulsions, stiffness, and gait abnormalities through video recognition, assisting in home risk monitoring for patients with chronic conditions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and care-support agents use this skill to analyze home monitoring images or videos for possible Parkinson's- or epilepsy-related abnormal movement events and to retrieve prior cloud-generated reports. The result is for monitoring support and does not replace professional medical diagnosis or clinical judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Health-related home video or image content and generated reports are sent to configured lifeemergence.com services.

Mitigation: Use only with consent for cloud processing, avoid unnecessary sensitive media, and confirm the publisher's privacy, retention, and deletion practices before deployment.

Risk: The skill silently creates or reuses an identity and stores tokens locally.

Mitigation: Run in an isolated workspace and avoid shared or default accounts for medical history or report retrieval.

Risk: The analysis may be mistaken for a medical diagnosis.

Mitigation: Present results as monitoring support only and route frequent or concerning events to qualified medical professionals.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-parkinson-epilepsy-behavior-recognition-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON analysis report text, with optional report links and command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local file input, public URL input, and cloud history lookup for prior reports.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter reports 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
